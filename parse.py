import csv
import getopt
import os
import re
import sys
from cStringIO import StringIO
from urllib2 import urlopen

import pandas as pd
import spacy
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage


def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    infile = file('Resumes/{}'.format(fname), 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text


def extract_name(text):
    reload(sys)
    sys.setdefaultencoding('utf8')
    nlp = spacy.load('xx')
    doc = nlp(unicode(text))
    for ent in doc.ents:
        if ent.label_ == 'PER':
            return ent.text


def extract_skills(lookup, text):
    skills = []
    for word in text.split(' '):
        if word in lookup.keys():
            skills.append(word)
    return (list(set(skills)))


def main():

    # Console Log (start)
    print '\nParsing is beginning...\n============================'

    # Reads CSV and creates dictionary of technical skills and their skills type.
    skills_dict = {}
    profiles = []

    # Console log (20)
    print 'Loading...\t\t15%\n'

    with open('techskills.csv', 'r') as ts:
        for skill in ts:
            line = skill.split(',')
            skills_dict[line[1].replace('\r\n', '')] = line[0]
    del skills_dict['']

    # Console log (30)
    print 'Loading...\t\t30%\n'

    # Console Logging benchmark
    load = 40

    # Parse each candidate's resume.
    for f in os.listdir('uploads'):
        if f != '.DS_Store':
            # New entry
            candidate = ''
            # Convert to raw text
            text = convert(f)
            name = extract_name(text).rstrip()
            text = text.lower().replace(',', '')
            # Candidate name
            candidate += '\nName: {}'.format(name)
            # Contact information
            candidate += '\nEmail: ' + re.findall('\S+@\S+', text)[0]
            sites = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
            if sites:
                candidate += '\nSite: {}'.format(sites[0])
            else:
                candidate += '\nSite: N/A'
            # Technical skills
            candidate += '\nTechnical skills: '
            for s in extract_skills(skills_dict, text):
                candidate += (str(s) + " ")
            candidate += '\n'
            profiles.append(candidate)

            # Console log (40-100)
            load += 15
            print 'Loading...\t\t{}%\n'.format(load)

    # Console log (complete)
    print 'Parsing complete!'
    return profiles


if __name__ == '__main__':
    main()

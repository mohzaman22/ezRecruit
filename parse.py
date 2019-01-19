#!/usr/bin/env python

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

    # Reads CSV and creates dictionary of technical skills and their skills type.
    skills_dict = {}
    profiles = []

    with open('techskills.csv', 'r') as ts:
        for skill in ts:
            line = skill.split(',')
            skills_dict[line[1].replace('\r\n', '')] = line[0]
    del skills_dict['']

    # Parse each candidate's resume.
    for f in os.listdir('uploads'):
        if f != '.DS_Store':
            # Convert to raw text
            text = convert(f)
            name = extract_name(text).rstrip()
            text = text.lower().replace(',', '')
            # Candidate name
            print 'Name: {}'.format(name)
            # Contact information
            print 'Email: ' + re.findall('\S+@\S+', text)[0]
            sites = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
            if sites:
                print 'Site: {}'.format(sites[0])
            else:
                print 'Site: N/A'
            # Technical skills
            print 'Technical skills: '
            print extract_skills(skills_dict, text)


if __name__ == '__main__':
    main()

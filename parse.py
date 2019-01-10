import os
import textract

def getcontent(file):
    return textract.process(('Resumes/{}').format(file))

def main():

    for file in os.listdir('Resumes'):
        # Extract content of Resume
        pdfText = getcontent(file)

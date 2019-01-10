import os
import scrape
import textract

def main():
    applicants = {}
    for file in os.listdir('Resumes'):
        # Extract content of Resume
        pdfText = scrape.getcontent(file)
        # Resume Author
        content = re.findall('\w+',pdfText)
        candidate = scrape.getname(content)
        # Process skill matches and assign a score to this candidate;
        # store entry in dictionary to be analyzed after processing
        # all candidates.
    return applicants

if __name__ == '__main__': main()

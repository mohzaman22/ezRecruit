import re
import textract

def getcontent(file):
    return textract.process(('Resumes/{}').format(file))

def getname(words):
    if re.match('\w.',words[1]) != None or re.match('\w',words[1]) != None:
        name = str(words[0] + ' ' + words[2])
    else:
        name = str(words[0] + ' ' + words[1])
    return name

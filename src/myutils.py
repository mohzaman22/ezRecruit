import os

def cleardir():
    for f in os.listdir('uploads'):
        os.remove('uploads/{}'.format(f))
# ezRecruit
ezRecruit is an easy, automated way to recruit Software Engineering talent. Through ezRecruit, one seeking talent will specify a job listing they are recruiting for. Based on the listing's requirements/qualifications and a repository of collected resumes, ezRecruit will find highly qualified candidates, gather contact information on these candidates and potentially automate contacting them to expedite the hiring process.
## About
When candidates' resumes are reviewed, upon loading the results screen you will see each candidate's information ranked from most to least qualified. This application will allow you to connect with candidates by automating the resume review process and provides contact information for each candidate.
<p align="center">
  <img src="https://i.ibb.co/zrmJdMW/Screen-Shot-2019-02-02-at-2-07-58-AM.png" alt="Results" width="325" height="200">
</p>

## Requirements
ezRecruit was developed under [Python 2.7](https://www.python.org/downloads).

Before you can run the application, you will need to install a few Python dependencies.

Note: Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include pip by default, so you may have pip already. Otherwise, you can install [easy_install](https://pythonhosted.org/setuptools/easy_install.html) `sudo apt-get install python-setuptools` to install [pip](https://pypi.python.org/pypi/pip) `sudo easy_install pip`.

- [pdfminer](https://pypi.org/project/pdfminer/), for pdf parsing: `pip install pdfminer`
- [spaCy](https://spacy.io/), for Natural Language Processing: `pip install spacy`

## Run
Once you have installed the required dependencies, navigate to the project's directory and run the application

- Change directory: `cd /././ezRecruit/src`
- Run the app locally: `php -S localhost:8080`


## Results
<a href="https://gifyu.com/image/wtON"><img src="https://s2.gifyu.com/images/Recording.gif" alt="Recording.gif" border="0" /></a>

## Enhancements
Please feel free to message me or open an issue if you have an idea for an enhancement! Seems like people are starting to use this and I would like to improve it.

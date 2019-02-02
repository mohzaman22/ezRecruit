# ezRecruit
ezRecruit is an easy, automated way to recruit Software Engineering talent. Through ezRecruit, one seeking talent will specify a job listing they are recruiting for. Based on the listing's requirements/qualifications and a repository of collected resumes, ezRecruit will find highly qualified candidates, gather contact information on these candidates and potentially automate contacting them to expedite the hiring process.
## About
When you view user's profile in LinkedIn they get notified that you have looked at their profile. This bot will allow you to view user's profiles thus increasing your visibility in your suggested LinkedIn network.
<p align="center">
  <img src="https://i.ibb.co/zrmJdMW/Screen-Shot-2019-02-02-at-2-07-58-AM.png" alt="Results" width="325" height="200">
</p>

## Requirements
**Important:** make sure that you have your [Profile Viewing Setting](https://www.linkedin.com/settings/?trk=nav_account_sub_nav_settings) changed from 'Anonymous' to  'Public' so LinkedIn members can see that you have visited them and can visit your profile in return.
You also must change your language setting to **English**.

ezRecruit was developed under [Pyhton 2.7](https://www.python.org/downloads).

Before you can run the bot, you will need to install a few Python dependencies.

Note: Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include pip by default, so you may have pip already. Otherwise, you can install [easy_install](https://pythonhosted.org/setuptools/easy_install.html) `sudo apt-get install python-setuptools` to install [pip](https://pypi.python.org/pypi/pip) `sudo easy_install pip`.

- [pdfminer](https://pypi.org/project/pdfminer/), for pdf parsing: `pip install pdfminer`
- [spaCy](https://spacy.io/), for Natural Language Processing `pip install spacy`

## Run
Once you have installed the required dependencies, navigate to the project's directory and run the application

- Change directory `cd /././ezRecruit`
- Run the app locally `php -S 127.0.0.1:8080`


## Results

![ezRecruit Demo gif](http://g.recordit.co/xPh4gK70lz.gifhh)


## Enhancements
Please feel free to message me or open an issue if you have an idea for an enhancement! Seems like people are starting to use this and I would like to improve it.

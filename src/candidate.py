''' This class is to create independent Candidate objects to store 
    each resume's respective attributes in order to most easily sort 
    and access this information '''


class Candidate:

    def __init__(self, name, site, email, skills, score):
        self.name = name
        self.site = site
        self.email = email
        self.skills = skills
        self.score = score

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_site(self, site):
        self.site = site

    def get_site(self):
        return self.site

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_skills(self, skills):
        self.skills = skills

    def get_skills(self):
        return self.skills

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

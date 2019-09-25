class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
    
    def year_category_student(self):
        if self.major == "Sales":
            return "5 years"
        elif self.major == "Purchase":
            return "3 years"
        else:
            return "No defined"
# This file is used in the 1_classes_and_objects file and 3_object_functions

class Student:

    def __init__(self, name, age, gender, is_studying):
        self.name = name
        self.age = age 
        self.gender = gender
        self.is_studying = is_studying
    
    def student_under_20(self):
        if self.is_studying:
            status = "is studying"
        else:
            status = "is not studying"

        if self.age < 20:
            age_group = "under 20"
        else:
            age_group = "20 or older"

        return f"{self.name} {status}, and is {age_group} ({self.age} years old)."
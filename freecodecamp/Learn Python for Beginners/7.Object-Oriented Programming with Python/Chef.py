# This file is used in the 4_inheritance file
class Chef:

    special_dish = "bbq ribs"

    def make_chicken(self):
        print(f"The chef makes the chicken")
    
    def make_salad(self):
        print(f"The chef makes a salad")
    
    def make_special_dish(self):
        print(f"The chef makes the {self.special_dish}")
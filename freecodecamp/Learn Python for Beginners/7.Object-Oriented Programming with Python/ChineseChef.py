# This file is used in the 4_inheritance file
from Chef import Chef
class ChineseChef(Chef):
    
    special_dish = "3 delight rice"

    def make_fried_rice(self):
        print(f"The chef makes fried rice")

# =========================================================
# LAB: BUILD AN RPG CHARACTER
# =========================================================
#
# OBJECTIVE
# ---------------------------------------------------------
# Practice the basics of Python by building a small app
# that creates a character for an RPG adventure.
#
# The goal is to fulfill the user stories and pass all tests.
#
# =========================================================
# REQUIREMENTS
# =========================================================
#
# Function name:
#
# create_character
#
# Parameters, in order:
#
# name
# strength
# intelligence
# charisma
#
# =========================================================
# NAME VALIDATION
# =========================================================
#
# 1. If name is not a string:
#
#     return "The character name should be a string"
#
# ---------------------------------------------------------
#
# 2. If name is an empty string:
#
#     return "The character should have a name"
#
# ---------------------------------------------------------
#
# 3. If name is longer than 10 characters:
#
#     return "The character name is too long"
#
# ---------------------------------------------------------
#
# 4. If name contains spaces:
#
#     return "The character name should not contain spaces"
#
# =========================================================
# STATS VALIDATION
# =========================================================
#
# 1. If one or more stats are not integers:
#
#     return "All stats should be integers"
#
# ---------------------------------------------------------
#
# 2. If one or more stats are less than 1:
#
#     return "All stats should be no less than 1"
#
# ---------------------------------------------------------
#
# 3. If one or more stats are greater than 4:
#
#     return "All stats should be no more than 4"
#
# ---------------------------------------------------------
#
# 4. If the sum of all stats is different than 7:
#
#     return "The character should start with 7 points"
#
# =========================================================
# OUTPUT FORMAT
# =========================================================
#
# If all values pass the validations, the function should
# return a string with four lines:
#
# Line 1: character name
# Line 2: STR followed by a space and the strength dots
# Line 3: INT followed by a space and the intelligence dots
# Line 4: CHA followed by a space and the charisma dots
#
# Each stat must have:
#
# - full dots equal to the stat value
# - empty dots until reaching 10 total dots
#
# Example:
#
# create_character("ren", 4, 2, 1)
#
# Expected:
#
# ren
# STR ●●●●○○○○○○
# INT ●●○○○○○○○○
# CHA ●○○○○○○○○○
#
# =========================================================
# NOTE
# =========================================================
#
# While str and int are common abbreviations for the stats,
# they are reserved keywords in Python and should not be used
# as variable names.
#
# =========================================================
# SOLUTION
# =========================================================

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    elif not name:
        return "The character should have a name"
    elif len(name) > 10:
        return "The character name is too long"
    elif " " in name:
        return "The character name should not contain spaces"

    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    elif (strength + intelligence + charisma) != 7:
        return "The character should start with 7 points"

    def str_dots():
        str_result = ""
        str_result = (str_result + full_dot) * strength

        while len(str_result) < 10:
            str_result = str_result + empty_dot

        return str_result

    def int_dots():
        int_result = ""
        int_result = (int_result + full_dot) * intelligence

        while len(int_result) < 10:
            int_result = int_result + empty_dot

        return int_result

    def cha_dots():
        cha_result = ""
        cha_result = (cha_result + full_dot) * charisma

        while len(cha_result) < 10:
            cha_result = cha_result + empty_dot

        return cha_result

    return f"{name}\nSTR {str_dots()}\nINT {int_dots()}\nCHA {cha_dots()}"


full_dot = "●"
empty_dot = "○"

print(create_character("ren", 4, 2, 1))

# =========================================================
# TEST RESULTS
# =========================================================
#
# Passed: 1. You should have a function named create_character.
# Passed: 2. Non-string name returns the correct error.
# Passed: 3. String name does not return the non-string error.
# Passed: 4. Empty string name returns the correct error.
# Passed: 5. Non-empty name does not return the empty-name error.
# Passed: 6. Name longer than 10 characters returns the correct error.
# Passed: 7. Valid length name does not return the too-long error.
# Passed: 8. Name with spaces returns the correct error.
# Passed: 9. Name without spaces does not return the spaces error.
# Passed: 10. Non-integer stats return the correct error.
# Passed: 11. Integer stats do not return the non-integer error.
# Passed: 12. Stats lower than 1 return the correct error.
# Passed: 13. Stats no less than 1 do not return the lower-than-1 error.
# Passed: 14. Stats higher than 4 return the correct error.
# Passed: 15. Stats no more than 4 do not return the higher-than-4 error.
# Passed: 16. Stats that do not sum to 7 return the correct error.
# Passed: 17. Stats that sum to 7 do not return the wrong-sum error.
# Passed: 18. create_character("ren", 4, 2, 1) returns the expected output.
# Passed: 19. Valid values output the character stats as required.
#
# =========================================================
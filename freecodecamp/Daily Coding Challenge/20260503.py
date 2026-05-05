#-----------
# Good Day -
#-----------

# Given a time string in "HH:MM" format (24-hour clock), return:
# - "Good morning" for times 05:00 to 11:59
# - "Good afternoon" for times 12:00 to 17:59
# - "Good evening" for times 18:00 to 21:59
# - "Good night" for times 22:00 to 04:59

# Tests:
# 1. get_greeting("06:30") should return "Good morning".
# 2. get_greeting("12:00") should return "Good afternoon".
# 3. get_greeting("21:59") should return "Good evening".
# 4. get_greeting("00:01") should return "Good night".
# 5. get_greeting("11:30") should return "Good morning".

def get_greeting(s):

    # Takes the 2 first numbers from the string
    hour = int(s[:2])

    if 5 <= hour <= 11:
        return "Good morning"
    elif 12 <= hour <= 17:
        return "Good afternoon"
    elif 18 <= hour <= 21:
        return "Good evening"
    else:
        return "Good night"


print(get_greeting("06:30"))
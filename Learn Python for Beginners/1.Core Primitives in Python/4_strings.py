
# \n me permite hacer saltos de linea
lines = "STRING\nLINES"

# \" me permite ñadir las "
quotes = "use of \"quotes"

phrase = lines + " " + quotes

print(f"{lines.lower()} and {quotes.upper()}")
print(f"{lines.isupper()} and {quotes.isupper()}")
print(f"{len(phrase)} is the length of the phrase")
print(f"{phrase[0]} is the first letter")
print(f"{phrase.index("G")} is where the letter is")
print(f"{phrase.replace("quotes", "comillas")} is the change of quotes")
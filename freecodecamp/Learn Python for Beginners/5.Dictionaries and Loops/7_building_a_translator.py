#ANDER language: all vowels are g

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Insert the phrase that you want to translate:")))
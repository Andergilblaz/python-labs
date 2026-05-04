
secret_word = "Lando"
guess = ""
count = 0
limit = 5
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if count<limit:
        if guess != "":
            print(f"Error, try again")
        guess = input("Guess the word:")
        count += 1

    else:
        out_of_guesses = True
        

if out_of_guesses:
    print(f"You have reached the maximum number of attempts")
else:
    print(f"Great! You got it!")

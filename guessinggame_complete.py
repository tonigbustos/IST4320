import random
#Because the random module is already installed within python #programming we do not need to install it externally with a pip #command, therefore we can simply import it and continue

top_of_range = input("Type a number: ")
#making sure that the user inputs an actual number

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
#default when a user types an input it would ne returned to us as a #string therefore .isdigit helps us make sure that it is returned as #an number. This function will help us convert that string into a #number
    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
#going to check if it is greater than 0, making sure that the user #inputs a number larger than 0
else:
    print('Please type a number next time.')
    quit()
#making sure that the user types in a digit, if they have not typed #in a digit this will print or tell the user that they need to type a #number
random_number = random.randint(0, top_of_range)
#will generate random number that they just typed in

guesses = 0

while True:
    guesses+= 1
    #we will be counting how many times the user guessess until correctly therefore everytime there is an input it will add a one
    user_guess = input("Make a guess: ")
#creating a loop to allow the user to keep guessing until guessed #correctly
    if user_guess.isdigit():
      user_guess = int(user_guess)
      #will be making sure  the user is typing a number and not a str
    else:
      print('Please type a number next time.')
      continue

    if user_guess == random_number:
      print('You got it!')
      break
      #break allows the program to end successfully if and when the         #guess is guessed correctly
    elif user_guess > random_number:
          print('You were above the number!')
      #elif is something that happens the statement, we would be            #cleaning the code and cleaned it up to look nicer
    else:
          print('You were below the number!')
      #want to tell the user whether they were above or below the           #number to narrow down the guesses and help the user out.

print("You got it in", guesses, "guesses")
#printing multiple things together and adding the amount of guesses #it took to guess correctly
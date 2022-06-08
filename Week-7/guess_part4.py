import random

continue_to_play = "yes"

while continue_to_play == "yes":
  magic_number = random.randint(1, 100)
  guess_number = int(input("What is your guess? "))
  guess_attempt = 1   

  while magic_number != guess_number:

    if magic_number < guess_number:
     print("Lower")
    elif magic_number > guess_number:
     print("Higher")
    guess_number = int(input("What is your guess? "))
    guess_attempt += 1
  print(f"You guessed it in {guess_attempt} attempts! ")
  continue_to_play = input("Do you want to play again? ")  

print("Game over")
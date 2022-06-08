import random


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
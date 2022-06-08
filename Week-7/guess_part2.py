magic_number = int(input("What is the magic number? "))
guess_number = int(input("What is your guess? "))


while magic_number != guess_number:
  if magic_number < guess_number:
    print("Lower")
  elif magic_number > guess_number:
     print("Higher")
  guess_number = int(input("What is your guess? "))
print("You guessed it!")
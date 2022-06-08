magic_number = int(input("What is the magic number? "))
guess_number = int(input("What is your guess? "))

if magic_number < guess_number:
  print("Lower")
elif magic_number > guess_number:
  print("Higher")
else:
  print("You guessed it!")
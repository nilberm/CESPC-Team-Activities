word = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the holy ghost."

run_again = "yes"



while run_again == "yes":
  number = int(input("Please enter a number: "))
  for i, letter in enumerate(word):
    if (i % number == 0):
      print(letter.upper(), end="")
    else:
      print(letter, end="")
  run_again = input("\n\nWould you like to enter another number? ").lower()
print("Goodbye")
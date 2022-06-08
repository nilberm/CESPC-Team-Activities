word = "commitment"
letter = input("What is your favorite letter? ").lower()
for i in word:
  if i == letter:
    print("_", end="")
  else:
    print(i, end="")
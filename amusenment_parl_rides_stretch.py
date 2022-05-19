age_rider_one = int(input("What is the age of the first rider?\n"))
if age_rider_one >= 12 and age_rider_one <= 17:
  golden_passport_one = input("Do you have a golden passport (yes/no)?\n")
height_rider_one = float(input("What is the height of the first rider?\n"))

that_is_a_second_rider = input("Is there a second river (yes/no)?\n").lower()

age_rider_two = 0
height_rider_two = 36
golden_passport_two = ""

if that_is_a_second_rider == "yes":
  age_rider_two = int(input("What is the age of the second rider?\n"))
  if age_rider_two >= 12 and age_rider_two <= 17:
    golden_passport_two = input("Do you have a golden passport (yes/no)?\n")
  height_rider_two = float(input("What is the height of the second rider?\n")) 


if golden_passport_one == "yes":
  age_rider_one = 18

if golden_passport_two == "yes":
  age_rider_two = 18


if  height_rider_one < 36 or height_rider_two < 36:
  print("Sorry, you may not ride.")
elif that_is_a_second_rider == "no":
  if age_rider_one >= 18:
    print("Welcome to the ride. Please be safe and have fun!")
  else:
    print("Sorry, you may not ride.")
elif age_rider_one >= 18 or age_rider_two >= 18:
  print("Welcome to the ride. Please be safe and have fun!")

elif age_rider_one >= 12 and age_rider_two >= 12 and height_rider_one >= 52 and height_rider_two >= 52:
  print("Welcome to the ride. Please be safe and have fun!")
elif age_rider_one >= 16 and age_rider_two >= 14 or age_rider_two >= 16 and age_rider_one >= 14:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")
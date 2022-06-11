import random

list_number = []

user_number = int(input("Enter number: "))

while user_number != 0:
  list_number.append(user_number)
  user_number = int(input("Enter number: "))
  
sum_numbers = 0
maximum_number = 0
smallest_number = 9999999999999

for i in list_number:
  sum_numbers += i
  if i > maximum_number:
    maximum_number = i
  if i > 0:
    if i < smallest_number:
      smallest_number = i

print(f"The sum is: {sum_numbers}")


average_number = sum_numbers / len(list_number)

print(f"The average is: {average_number}")
  
print(f"The largest number is: {maximum_number}")

print(f"The smallest positive number is : {smallest_number}")

random.shuffle(list_number)

print(f"The sorted list id: {list_number}")
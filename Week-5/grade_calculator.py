letter_grade = ''

percentage = float(input("What is your grade percentage? (whitout the percentage simbol) "))

if (percentage >= 90):
    letter_grade = 'A'
elif (percentage >= 80):
    letter_grade = 'B'
elif (percentage >= 70):
    letter_grade = 'C'
elif (percentage >= 60):
    letter_grade = 'D'
else:
    letter_grade = 'F'

plus_and_minus = ''

if percentage > 60 and percentage < 94:
    if (percentage%10 >= 7):
        plus_and_minus = '+'
    elif (percentage%10 <= 3):
        plus_and_minus = '-'



if (percentage >= 70):
    print(f"Congratulations, your grade is {letter_grade+plus_and_minus} and you passed the course!")
else:
    print(f"Your grade is {letter_grade+plus_and_minus}, better lucky next time.")


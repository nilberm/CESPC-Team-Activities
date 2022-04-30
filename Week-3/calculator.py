import math

# sideSquare = float(input('What is the length of a side of the square? '))
# print(f'The area of the square is: {sideSquare * sideSquare}')

# lengthRectangle = float(input('What is the length of the rectangle? '))
# widthRectangle = float(input('What is the width of the rectangle? '))
# print(f'The area of the rectangle is {lengthRectangle * widthRectangle}')

# radiusCircle = float(input('What is the radius of the circle? '))
# print(f'The area of the circle is {3.14 * (radiusCircle**2)}')

#------------------------------- STRETCH CHALLENGE --------------------------#

sideSquare = float(input('What is the length of a side of the square in centimeters? '))
print(f'\nThe area of the square is: {sideSquare ** 2}cm² / {(sideSquare ** 2)/1000}m³')
print(f'The volume of the square is: {sideSquare ** 3}cm² / {(sideSquare ** 3)/1000}m³\n')

lengthRectangle = float(input('What is the length of the rectangle in centimeters?? '))
widthRectangle = float(input('What is the width of the rectangle in centimeters?? '))
print(f'\nThe area of the rectangle is: {lengthRectangle * widthRectangle}cm² / {(lengthRectangle * widthRectangle)/1000}m³\n')

radiusCircle = float(input('What is the radius of the circle in centimeters? '))
print(f'\nThe area of the circle is: {math.pi * (radiusCircle**2):.2f}cm² / {(math.pi * (radiusCircle**2))/1000:.2f}m³')
print(f'The volume of the sphere is: {(4 * math.pi * (radiusCircle ** 3))/3:.2f}cm² / {((4 * math.pi * (radiusCircle ** 3))/3)/1000:.2f}m³')

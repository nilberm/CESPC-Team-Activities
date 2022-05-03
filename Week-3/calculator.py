import math

# sideSquare = float(input("What is the length of a side of the square? "))
# areaSquare = sideSquare ** 2
# volumeSquare = sideSquare ** 3

# print(f"The area of the square is: {areaSquare}")
# print(f"The volume of the square is: {volumeSquare}")

# lengthRectangle = float(input("What is the length of the rectangle? "))
# widthRectangle = float(input("What is the width of the rectangle? "))
# areaRectangle = lengthRectangle * widthRectangle

# print(f"The area of the rectangle is: {areaRectangle}")

# radiusCircle = float(input("What is the radius of the circle? "))
# areaCircle = math.pi * (radiusCircle**2)
# volumeSphere = (4 * math.pi * (radiusCircle**3)) / 3

# print(f"The area of the circle is: {areaCircle}")
# print(f"The volume of the sphere is: {volumeSphere}")


sideSquare = float(input("What is the length of a side of the square in centimeters? "))
areaSquare = sideSquare ** 2
volumeSquare = sideSquare ** 3

print(f"The area of the square is: {areaSquare}cm / {areaSquare / 10000}m")
print(f"The volume of the square is: {volumeSquare}cm")

lengthRectangle = float(input("What is the length of the rectangle in centimeters? "))
widthRectangle = float(input("What is the width of the rectangle in centimeters? "))
areaRectangle = lengthRectangle * widthRectangle

print(f"The area of the rectangle is: {areaRectangle}cm / {areaRectangle / 10000}m")

radiusCircle = float(input("What is the radius of the circle in centimeters? "))
areaCircle = math.pi * (radiusCircle**2)
volumeSphere = (4 * math.pi * (radiusCircle**3)) / 3

print(f"The area of the circle is: {areaCircle}cm / {areaCircle / 10000}m")
print(f"The volume of the sphere is: {volumeSphere}cm")

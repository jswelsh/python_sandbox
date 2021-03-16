def addition(a, b):
	return a + b
print(8, ':', addition(3, 5))

def nextNumber(num):
	return num + 1
print(8, ':',nextNumber(7))

def MinutesToSeconds(minutes):
	return minutes * 60 
print(180, ':',MinutesToSeconds(3))

def areaOfTriangle(base, height):
	return base * height / 2
print(50.0, ':', areaOfTriangle(10,10))

def ConvertAgetoDays(age):
	return age * 365
print(7300, ':', ConvertAgetoDays(20))

def PerimeterRectangle(length, width):
	return (length + width) * 2
print(26, ':', PerimeterRectangle(6, 7))

def MaximumEdgeTriangle(side1, side2):
	return side1 + side2 - 1
print(17, ':', MaximumEdgeTriangle(8,10))

def HoursToSeconds(hours):
	return hours * 60 * 60
print(7200, ':', HoursToSeconds(2))

def string_to_int(string):
	return int(string)
print(7200, ':', string_to_int('7200'))

def cube_it(a):
	return a ** 3
print(27, ':', cube_it(3))

def sum_polygon_angles(numberOfSides):
	return (numberOfSides - 2) * 180
print(360, ':', sum_polygon_angles(4))

def get_first_value(list):
	return list[0]
print(3, ':', [3, 4, 5, 9, 8])


# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between a range inclusively.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def are_divisible_by_seven_not_five(min, max):
	arr = []
	for i in range(min, max):
		if i % 7 == 0 and i % 5 != 0:
			arr.append(str(i))

	return ','.join(arr)

print(are_divisible_by_seven_not_five(100,400))
print(are_divisible_by_seven_not_five(8,150))

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:

def fact(num):
	if num == 0:
		return 1
	return num * fact(num - 1)

print(fact(5))
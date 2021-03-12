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


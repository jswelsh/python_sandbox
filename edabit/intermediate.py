def stuttering_function(word):
	stutter_word = word[0:2]
	return stutter_word + '... ' + word[0:2] + '... ' + word + '?'
print('in...in...increasing?', ':', stuttering_function('increasing'))

def factorial(num):
    new_num = num
    for i in range(num-1):
        new_num *= i+1
    return new_num
print(6227020800, ',', factorial(13))

def basic_calculator(x, operand, y):
	if operand == '+':
            return x + y
	elif operand == '-':
            return x - y
	elif operand == '*':
            return x * y 
	elif operand == '/':
            if y == 0:
                    return "Can't divide by 0!"
            else:
                    return int(x / y)
print(7, ':', basic_calculator(21, '/', 3))
print(21, ':', basic_calculator(7, '*', 3))

def curzon_numbers(num):
    elevated_x = 1 + 2 ** num 
    elevated_y = 1 + 2 * num
    if  elevated_x % elevated_y:
        return False

    else: 
        return True
print(True, curzon_numbers(14))
print(False, curzon_numbers(10))

def multiplying_numbers_in_string(str):
    arr = str.split(',')
    total = 1
    for num in arr:
            total *= int(num)

    return total
print(24, ':', multiplying_numbers_in_string('1,2,3,4'))
print(0, ':', multiplying_numbers_in_string('54, 75, 453, 0'))
print(-20, ':', multiplying_numbers_in_string('10, -2'))

def relation_to_luke(name):
    if name == "Darth Vader":
            return"Luke, I am your father."
    if name == "Leia":
            return"Luke, I am your sister."
    if name == "Han":
            return"Luke, I am your 	brother in law."
    if name == "R2D2":
            return"Luke, I am your droid."
print("Luke, I am your father.", ":", relation_to_luke("Darth Vader"))
print("Luke, I am your sister.", ":", relation_to_luke("Leia"))

def is_leap(year):
    return  year % 4 == 0
print(False, ':', is_leap(1990))
print(True, ':', is_leap(1992))

def fizz(max):
    for i in range(max):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizz(90)

def get_integer()
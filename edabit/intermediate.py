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
# fizz(90)

def caught_speeding(speed, is_birthday):
    speeding_threshold = (65,85) if is_birthday else (60,80)
    if speed > speeding_threshold[1]:
        return 2
    elif speed > speeding_threshold[0]:
        return 1
    else:
        return 0
print(0, ':', caught_speeding(60, False))
print(1, ':', caught_speeding(66, True))
print(1, ':', caught_speeding(84, True))
print(2, ':', caught_speeding(81, False))

def make_bricks(small, big, goal):
    return (goal % 5) <= small and (goal - (big * 5)) <= small
    # if big * 5 + small < goal:
    #     return 'fail 1'
    # elif goal % 5 > small:
    #     return 'fail 2'
    # return False
print(True, ':', make_bricks(2, 2, 15))
print(False, ':', make_bricks(2, 2, 8))
print(True, ':', make_bricks(2, 2, 7))
print(True, ':', make_bricks(2, 4, 7))

def double_char(str):
    str_arr = []
    for i in str:
        str_arr.append(i+i)
    return ''.join(str_arr)
print(double_char('hello'))

def remove_duplicate( li ):
    new_arr=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            new_arr.append(item)
    return new_arr
li=[12,24,35,24,88,120,155,88,120,155]
print(remove_duplicate(li))

def capitalize(str):
    arr = []
    for i in str:
        arr.append(i.upper())
    return ''.join(arr)
print(capitalize('hello world'))

def enough_wood(short, long, length):
    if short + long * 5 < length:
        return 'not enough wood'
    if length % 5 - short > 0:
        return 'not enough small pieces'
    return "you're good"
print(enough_wood(3,5,15))

def make_triangle(size):
    for i in range(1, size):
        print(str(i+1)*(i+1))
print(make_triangle(5))
print(make_triangle(9))

# We count 35 heads and 94 legs among the 
# chickens and rabbits in a farm. How many 
# rabbits and how many chickens do we have?
def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads + 1):
        j = numheads - i
        if 2 * i + 4 * j == numlegs:
            return i,j
    return ns,ns

numheads = 35
numlegs = 94
solutions = solve(numheads,numlegs)
print(solutions)

def number_of_char_in_str(str):
    dic = {}
    
    for s in str:
        dic[s] = dic.get(s,0)+1
    return '\n'.join(['%s,%s' % (k, v) for k, v in dic.items()])

print(number_of_char_in_str('abcdefgabc'))
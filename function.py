def to_celsius(x):
   '''Convert Fahrenheit to Celsius'''
   return (x-32) * 5/9

temp = to_celsius(100)
print(temp)

# Function: A body of resuable code for performing specific processes or tasks

def greeting(name):
   print(f'Welcome, {name}!')
   print(f'You are part of the team!')

greeting("Avinash Kumar")

# return: A reserved keyword in Python that makes a function produce new results, which are saved for later use

def area_triangle(base, height):
   return base * height / 2

area = area_triangle(4,4)

print(f'The area of the triangle is {area}')

# Resuability: Defining code once and using it many times without having to rewrite it.

def get_seconds(hours, minutes, seconds):
   total_seconds = hours * 3600 + minutes * 60 + seconds
   return total_seconds


total_seconds = get_seconds(1,1,60)
print(f'Total number of seconds is {total_seconds}')

def lucky_number(name):
   number = len(name)*9
   print(f"Hello {name}. Your lucky number is {number}")

lucky_number("Avinash")
lucky_number("Kumar")


# Modularity: The ability to write code in separate components that work together and that can be reused for other programs
# Refactoring: The process of restructuring code while maintaining its original functionality
# Self-documenting code: Code written in a way that is readable and makes its purpose clear

def factorial(number):
    fact = 1
    for i in range(number):
        fact = fact * (i+1)

    return fact

number = input("Enter any number: ")
number = int(number)
print(f"The factorial of {number} is {factorial(number)}")

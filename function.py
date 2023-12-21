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
print("Hello Word!")
print(22)

print((5 + 4)/4) 

country = "Brazil"
age = 30

print(country)
print(age)

print(10**3 == 1000)

print (10 * 3 == 40)

print(10 * 3 == age)

if age > 18:
    print("You are an adult")
else:
    print("You are a child")


for number in [1, 2, 3, 4, 5]:
    print(number)

print("different list")
my_list = [3, 6, 9]
for number in my_list:
    print(number/3)


def is_adult(age):
    if age >= 18:
        return True
    else:
        return False
    
print(is_adult(20))

new_list = [20, 25, 10, 5]
print(sorted(new_list))

magic = "Hello"
print(type(magic))

magic = magic.swapcase()
print(magic)

magic = magic.replace("E", "a")
print(magic)   

magic = magic.split("a")
print(magic)

# core python classes
# int, floats, string, boolean, list, lists, dictionaries, tuples, sets, frozensets, functions, ranges, none

# attribute: A value associated with an object or class which is referenced by name using dot notation. For example, if an object o has an attribute a it would be referenced as o.a.
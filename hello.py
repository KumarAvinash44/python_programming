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
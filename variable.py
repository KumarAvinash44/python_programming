#dynamic typing: type of variable is determined at runtime or Variable can point to objects of any data type

age_list = [34, 25, 23, 19, 29]
max_age = max(age_list)
print(f'maximum age value: {max_age}')

# change the type of max_age variable from integer to string
max_age = str(max_age)
print(f'converted type of the variable: {type(max_age)}')


# reassign the total new value to the variable, reassign
max_age = "ninety-nine"
print(max_age)


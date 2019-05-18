# multiline comments
'''
name = input('Your name? ')
color = input('Color you like? ')

print(name + " likes " + color)
'''

birth_year = input('Enter your birth year: ')

print('type of birth_year is: ') # input taken from user is always a string
print(type(birth_year))

age = 2019 - int(birth_year) # int() - converts str to int

print('type of age is: ')
print(type(age))

print('you are: '+ str(age) + ' years old')
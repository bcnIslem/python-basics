
# type converion

# ##################################

# user inputs considered as string
# event if you enter a number

# ##################################

# user input
age = input('inter your age: ')
# convert into int
int_age = int(age)

print(f'type of user input: {age}: {type(age)}') # <class 'str'>
print(f'type of age: {int_age}: {type(int_age)}') # <class 'int'>

# ##################################
# from int to float
i = 60
f = float(i)

print(f'from int {i} to float: {f}')

#  from float to int
ff = 6.6
ii = int(ff)

print(f'from float {ff} to int: {ii}')




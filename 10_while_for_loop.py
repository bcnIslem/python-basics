# while loop syntax

# ##########################

# 
# 
# while boolean conditon:
#     block of code
# 
# 

# so the block of code is executed as long
# as the boolean condition is true

# ##########################

number = 3
sum = 0

i = 1
while i <= number:
    sum += i
    # incrementing the counter
    i += 1

print(f'sum: {sum}') # 6

# ##########################
# for loop in python is used to iterate
# over a sequence or other iterable objects
# such as Strings, lists, range()

# string
test = 'new string'

# array / list
arr = [12, 6, 62, 1]

# range()
# sequence of numbers from 1 to 10
number = range(1, 11)

# 
# 
# for value in sequence:
#     block of code
# 
# 

languages = ['python', 'c#', 'javascript', 'c++', 'java', 'c']

for item in languages:
    print(f'item: {item}')

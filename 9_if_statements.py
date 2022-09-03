# syntax and space are IMPORTANT

# if
note = 12

if note > 10:
    print('good') #
    print('still inside the if statement') #

if note >= 16:
    print('great')
print('outside the if statement') #

# #################################

# if else
if note < 10:
    comment = 'bad'
else:
    comment = 'good'

print(f'comment: {comment}') # good

# #################################
# if we have another condition
# we use the 'elif' as else if witch means:
# it do the else and check for the condition

note = 16

if note < 10:
    comment = 'bad'
elif note > 15:
    comment = 'great'
else:
    comment = 'good' 

print(f'comment: {comment}') # great

#  using another if else statement inside the else

title = 'software engineer'
age = 24

if age > 21:
    print('old enaugh')
else:
    if title == 'software engineer':
        print('alright')
    else:
        print('sorry!')
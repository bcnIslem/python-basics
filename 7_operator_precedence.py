# augmented
x = 10
print(x)

x = x + 3
print(x) # 13

# best practice
y = 10
y += 3
print(y) # 13

# ###########################
#operator precedence
# () , Parentheses
# ** , Exponent
# +x, -x, ~x , Unary plus, Unary minus, Bitwise NOT
# *, /, //, % , Multiplication, Division, Floor division, Modulus
# +, - , Addition, Subtraction
# <<, >> , Bitwise shift operators
# & , Bitwise AND
# ^ , Bitwise XOR
# | , Bitwise OR
# | , Bitwise OR
# ==, !=, >, >=, <, <=, is, is not, in, not in , Comparisons, Identity, Membership operators
# NOT , Logical NOT
# AND , Logical AND
# OR , Logical OR

# ###########################
# some examples

# Precedence of or & and
name = 'islem'
age = 18

if name == 'islem' or name == 'jhon' and age >= 21:
    print('you can enter.')
else:
    print("you can't enter")

# returns true only if name is islem or jhon and true only if age is more than or equal to 21

# ######################
# Precedence of or & and
name = 'islem'
age = 18

if (name == 'islem' or name == 'jhon') and age >= 21:
    print('you can enter.')
else:
    print("you can't enter")

# This program runs if block even when age is 18. It does not give us the desired output since the precedence of and is higher than or.

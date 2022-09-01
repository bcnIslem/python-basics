import math

# we are going to see 3 methods 
# round()
# floor()
# ceil()
# and whats the main difference

# #############################

x1 = 6.0
x2 = 6.4
x3 = 6.5
x4 = 6.6

print(f'x1 = 6.0: round => {round(x1)}') # 6
print(f'x2 = 6.4: round => {round(x2)}') # 6
print(f'x3 = 6.5: round => {round(x3)}') # 6
print(f'x4 = 6.6: round => {round(x4)}') # 7

# round() function float point number from the
# decimal value to the closest multiple of 10.

# notice
# the int value to the closest multiple of 10
# to the power minus ndigits, where ndigits is
# the precision after the decimal point.
# if two multiples are equally close,
# rounding is done toward the even choice

x5 = 9.81317
print(f'x5 = 9.8131: round => {round(x5, 2)}') # 9.81
print(f'x5 = 9.8131: round => {round(x5, 4)}') # 9.8132


# #############################

# floor(y) method returns the floor of y
# the largest integer not greater then y.

y1 = 13.13
y2 = -13.13
y3 = 90.50
y4 = 90.99

print(f'y1 = 13.13: floor => {math.floor(y1)}') # 13
print(f'y2 = -13.13: floor => {math.floor(y2)}') # -14
print(f'y3 = 90.50: floor => {math.floor(y3)}') # 90
print(f'y4 = 90.99: floor => {math.floor(y4)}') # 90


# #############################

# the method ceil(y) returns a ceiling value of y 
# the smallest integer greater than or equal to y.

print(f'y1 = 13.13: ceil => {math.ceil(y1)}') # 14
print(f'y2 = -13.13: ceil => {math.ceil(y2)}') # -13
print(f'y3 = 90.50: ceil => {math.ceil(y3)}') # 91
print(f'y4 = 90.99: ceil => {math.ceil(y4)}') # 91
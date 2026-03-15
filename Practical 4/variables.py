# 4.1 Some simple math
# the estimated population in 2004
a = 5.08 
# the estimated population in 2014
b = 5.33
# the estimated population in 2024
c = 5.55
# the change between 2004 and 2014
d = b - a
# the change between 2014 and 2025
e = c - b
# compare d to e
if d > e:
    # The growth in the first ten years was larger, showing the population growth is decelerating
    print("d is larger than e. Population growth is decelerating in Scotland.")
else:
    # The growth in the next ten years is larger, showing the population growth is accelerating
    print("d is smaller than e. Population growth is accelerating in Scotland.")
# 4.2 Booleans
X = True
Y = False
W = X or Y
# Truth table for W
# | X     | Y     | W = X or Y |
# | True  | True  | True       |
# | True  | False | True       |
# | False | True  | True       |
# | False | False | False      |
print(W)

"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I lik"e turtles!"
print('x is %d, y is %4.2f, z is "%s"\n' % (x,y,z))

# Use the 'format' string method to print the same thing
# print(f"x is {0:d} y is {1:4.2f}, z is {2:s}\n'.format(x,y,z)"
# txt = "x is {x}, y is {y: .2f}, z is {z}\n"
# print(txt.format(x = x, y = y, z = z))
print('x is {}, y is {}, z is \"{}\"\n'.format(x,y.__round__(2),z))

# Finally, print the same thing using an f-string
# print(f"x is {x}, y is {y}, z is {z}\n")
print(f"x is {x}, y is {'%0.2f' % y}, z is \"{z}\"\n") 
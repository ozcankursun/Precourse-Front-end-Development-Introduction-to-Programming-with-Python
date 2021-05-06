# Convert one type to another:

x = 8    # int
y = 1.3  # float

# 1. Convert from int to float:
x = float(x)
# 2. Convert from float to int:
y = int(y)
# 3. Write a Python program to convert an integer to binary. 
# Tip: search for the function 'format'
txt = "The binary version of {0} is {0:b}"
x = 11
print(txt.format(x))
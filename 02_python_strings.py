# Set a different value for 'str' to get the right answer.

str = 'The lenght should be'

# 1. Length
# The length should be 20
print("Length of str = ", len(str))

# 2. Positions
# This will display the second letter:
print(str[1])
# Now, show the third letter
print(str[2])

# 3. Index
# Display the position of the first match with the letter a
# It should print 1
str = 'car'
print("First position of the letter a = ", str.index("a"))

# 4. Count
# Count at least 5 letters a
s = 'I am thinking of the main idea of topic but i cannot remember that'
print("It has ", s.count("a"))

# 5. Print in rows
# Print every letter of the string
str = 'banana'
for x in str:
  print(x)

# 6. For the next exercise, leave the value of `str` as it is
# and use methods to change the given string to lower case, 
# print it, then change it to upper case and print it

str = "HeLLo, hOW aRe YoU?"
print(str.lower())
print(str.upper())

# Tip: search for the different Python String Methods
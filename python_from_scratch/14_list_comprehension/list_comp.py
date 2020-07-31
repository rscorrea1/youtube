###################################################
# Let's learn about List Comprehension in Python! #
###################################################

# list data type => check the previous videos on Lists
numbers = [1,-4,9,25,36]

# Populate lists using for loops
# result = []
# for value in numbers:
#     if value >= 0:
#         result.append(value**0.5)
# print(result)

# list comprehension
def sqRoot(x):
    return x**0.5

result = [sqRoot(value) for value in numbers if value >= 0]
print(result)

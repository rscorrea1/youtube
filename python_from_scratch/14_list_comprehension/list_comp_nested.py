###################################################
# Let's learn about List Comprehension in Python! #
###################################################

# Goal: building a cartesian grid

# for loop strategy
# cartesian = []
# for x in range(1,7):
#     for y in range(1,6):
#         cartesian.append((x,y))
# print(cartesian)

# list comprehension
X = range(1,7)
Y = range(1,6)
cartesian = [(x,y) for x in X for y in Y if x<5 and y<5]
print(cartesian)

#Goal: building a polar grid

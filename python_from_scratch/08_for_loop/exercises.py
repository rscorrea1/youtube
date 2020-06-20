####################################
# Let's learn for loops in Python! #
####################################

# exercises: nested loop + break|continue
numbers = [1,2,3]
letters = ["a","b","c"]

for number in numbers:
    for letter in letters:
        if letter == "b":
            continue
        print(number, letter)

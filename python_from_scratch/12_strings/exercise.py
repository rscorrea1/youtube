########################################
# Let's learn about Strings in Python! #
########################################

from pprint import pprint

# parsing the exercise file
numbers_list = []
with open("exercise.txt","r") as file:
    for line in file:
        line = line.strip("\n")
        if line.startswith("numbers:"):
            line = line.strip("numbers:")
            line = line.replace(",","")
            line = line.split()
            numbers_list.append(line)
            # print(line)

pprint(numbers_list)

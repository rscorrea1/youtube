##############################################
# Let's learn how to parse a file in Python! #
##############################################

# parsing a text file
names, ages, heights = [], [], []
with open("exercise.txt","r") as file:
    for line in file:
        line = line.strip("\n")
        line = line.split("#")
        names.append(line[0])
        ages.append(int(line[1]))
        heights.append(float(line[2]))
        # print(line)

print(names)
print(ages)
print(heights)

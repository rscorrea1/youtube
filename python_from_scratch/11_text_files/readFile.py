#############################################
# Let's learn how to open a file in Python! #
#############################################

# open a file
# file = open("southAmerica.txt","r")
# content = file.read()
# print(content)
# file.close()

# with open("southAmerica.txt","r") as file:
#     content = file.readlines()
#     print(content)
#
# for line in content:
#     line = line.strip("\n")
#     print(line)

countries = []
with open("southAmerica.txt","r") as file:
    for line in file:
        # line = line.strip("\n")
        countries.append(line)
        # print(line)
print(countries)

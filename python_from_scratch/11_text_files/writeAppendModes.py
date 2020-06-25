#############################################
# Let's learn how to open a file in Python! #
#############################################

# write a text file
numerical = [1,2,3,4.5,4.2]
string_list = ["Jesse","Walt","Oli"]
with open("writeToFile.txt", "a") as file:
    for names in string_list:
        file.write(names+"\n")

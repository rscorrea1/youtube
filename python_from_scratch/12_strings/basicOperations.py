########################################
# Let's learn about Strings in Python! #
########################################

## string length
# text = "Python "
# print(len(text))

## indexing: how to access a single character
# channelName = "Fall in Python"
# char = channelName[-2]
# print(char)

## slicing strings => string[start:end]
# channelName = "Fall in Python"
# slice = channelName[8:]
# print(slice)

## string concatenation
# name = "Rodrigo"
# surname = "Correa"
# fullName = name + " " + surname
# print(type(fullName), fullName)

## string repetition
# text = "1"
# print(text*3)

## iterating over a string
channelName = "Fall in Python"
for idx, letter in enumerate(channelName):
    print(idx, letter)

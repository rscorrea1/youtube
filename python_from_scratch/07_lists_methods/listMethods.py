#############################
# Let's learn Python Lists! #
#############################

## how to find all the list methods and attrib.
# colors = ["white","blue","pink"]
# print(type(colors))
# print(dir(colors))


#####################################
# List methods and bonus operations #
#####################################

## index => listName.index(item)
# names = ["Rodrigo", "Bob", "Oli"]
# idx = names.index("Oli")
# print(idx)
#
# if "Jesse" in names:
#     print(names.index("Rodrigo"))


## append => listName.append(item)
# names = ["Rodrigo", "Bob", "Oli"]
# names.append("Jack")
# print(names)
#
# names.append(["Jhon","Marry"])
# print(names)


## insert => listName.insert(index,item)
# names = ["Rodrigo", "Bob", "Oli"]
# names.insert(0,"Walt")
# names.insert(1,"Jesse")
# print(names)


## remove => listName.remove(item)
# names = ["Rodrigo", "Bob", "Oli"]
# if "Oli" in names:
#     names.remove("Oli")
# print(names)


## pop => listName.pop(index)
# names = ["Rodrigo", "Bob", "Oli"]
# names.pop(2)
# print(names)


## clear => listName.clear()
# names = ["Rodrigo", "Bob", "Oli"]
# names.clear()
# print(names)


## bonus: delete an item by its index
# names = ["Rodrigo", "Bob", "Oli"]
# del names[0]
# print(names)


## extend => listName.extend(list)
# names = ["Rodrigo", "Bob", "Oli"]
# names.append(["Walt", "Jack"])
# print(names)


## count => listName.count(element)
# letters = ["a","b","c","b","a","b",]
# print(letters.count("a"))
# print(letters.count("b"))
# print(letters.count("c"))


## reverse => listName.reverse()
# numbers = [3, 4, 5, 1, 2]
# print(numbers)
# numbers.reverse()
# print(numbers)


## sort => listName.sort(reverse=True|False)
# numbers = [3, 4, 5, 1, 2]
# print(numbers)
# numbers.sort(reverse=True)☻
# print(numbers)

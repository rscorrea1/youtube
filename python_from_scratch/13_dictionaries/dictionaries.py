#############################################
# Let's learn about Dictionaries in Python! #
#############################################

## how to initialize a dictionary
menu = {}

## how to add element to a dictionary
menu["Cappuccino"] = 2.5
menu["Tea"] = 1.5
menu["Water"] = 1.0
menu["Juice"] = 2.0
# print(menu)
## dictionary length
# print(len(menu))

## how to retrieve data from a dictionary element
# tea_price = menu["Tea"]
# water_price = menu["Water"]
# # print(tea_price,water_price)
# if "Orange" in menu:
#     print(menu["Orange"])
# else:
#     print("key not valid")

## how to reassign data
menu["Tea"] = 1.8
print(menu)


## how to remove a dictionary element
del menu["Water"]
print(menu)

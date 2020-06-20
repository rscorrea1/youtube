####################################
# Let's learn for loops in Python! #
####################################

## generic example
# guests = ["Walt", "Jesse", "Marry",
#           "Jack", "Paul", "Loren"]
#
# for person in guests:
# 	print("Welcome", person, "!")


## numerical example
# odd_numbers = [1,3,5,7,9]
# even_numbers = []
# for odd in odd_numbers:
#     even = odd-1
#     even_numbers.append(even)
#     print(even,even_numbers)
# print("out of the for block")
# print(odd_numbers)
# print(even_numbers)


## break example
# nationalities = ["British", "Scottish", "Irish",
# 				 "English", "Danish", "Finnish",
# 				 "Norwegian", "Swedish", "French",
# 				 "Italian", "Estonian", "Latvian",
# 				 "Lithuanian", "Austrian", "Belgian",
# 				 "French", "German", "Dutch",
# 				 "American", "Canadian", "Mexican",
# 				 "Ukrainian", "Russian", "Belarusian",
# 				 "Polish", "Greek", "Spanish"]
#
# match_nationality = "Greek"
# for nationality in nationalities:
# 	print(nationality)
# 	if nationality == match_nationality:
# 		print("there you are!")
# 		break


## continue example
# days =["Monday", "Tuesday", "Wednesday", "Thursday",
#        "Friday", "Saturday", "Sunday"]
#
# for day in days:
# 	if day == "Wednesday":
# 		continue
# 	print(day)


## nested loop
# numbers = [1,2,3]
# letters = ["a","b","c"]
#
# for number in numbers:
#     for letter in letters:
#         print(number, letter)

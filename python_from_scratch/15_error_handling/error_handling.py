######################################################
# Let's learn how to deal with Exceptions in Python! #
######################################################

# calculator: dividing by zero
firstValue = 2.0
secondValue = (1,2)

# mix exception handling
try:
    print(secondValue[2])
except ZeroDivisionError:
    print("Cannot divide by zero")
except TypeError:
    print("Cannot mix data types")
except Exception as msg:
    print(msg)

# specific exception handling
# try:
#     print(firstValue/secondValue)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except TypeError:
#     print("Cannot mix data types")

# general exception handling
# try:
#     print(firstValue/secondValue)
# except Exception as msg:
#     print(msg)

print("end of script")

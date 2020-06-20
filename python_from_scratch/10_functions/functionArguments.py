####################################
# Let's learn Functions in Python! #
####################################

# example: concatenator function
def concatenator(arg1, arg2):
    """ Concatenates two given arguments """
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("Concatenation:", arg1+arg2)


# required argument(s)
concatenator("h","i")
print()

# keyword argument(s)
concatenator(arg2="i", arg1="h")

####################################
# Let's learn Functions in Python! #
####################################

# default argument example
def concatenator(arg1, arg2, toSort=False):
    concat_list = arg1 + arg2
    if toSort == True:
        concat_list.sort()
    return concat_list

# call function
result = concatenator([2,9], [7,4])
print(result)

result = concatenator([2,9], [7,4], toSort=True)
print(result)

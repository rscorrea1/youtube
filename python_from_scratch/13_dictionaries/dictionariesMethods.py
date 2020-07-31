#############################################
# Let's learn about Dictionaries in Python! #
#############################################
from pprint import pprint

## define dictionary
# channel = {"Name": "Fall in Python",
#            "Videos": 12,
#            "Content": ["Python Tutorial",
#                        "Engineering",
#                        "Data Science"]
# 		  }

# print(dir(channel))
# print(help(channel.get))


## method: dictionary.get()
##         => returns the value mapped to the key
# channel = {"Name": "Fall in Python",
#            "Videos": 12,
#            "Content": ["Python Tutorial",
#                        "Engineering",
#                        "Data Science"]
# 		  }
# channelName = channel["Name"]   # channel.get("Name")
# subs = channel.get("subscribers","not a valid key")
# print(channelName)
# print(subs)


## method: dictionary.update()
##         => updates the dictionary
# channel = {"Name": "Fall in Python",
#            "Videos": 12,
#            "Content": ["Python Tutorial",
#                        "Engineering",
#                        "Data Science"]
# 		  }
# channel.update({"Subscribers": 82})
# channel.update({"Subscribers": 80, "Videos": 13})
# pprint(channel)


## method: dictionary.pop()
##         => removes a dictionary element
# channel = {"Name": "Fall in Python",
#            "Videos": 12,
#            "Content": ["Python Tutorial",
#                        "Engineering",
#                        "Data Science"]
# 		  }
# channel.pop("Videos")
# pprint(channel)


## method: dictionary.keys()
##         => returns a list of all dictionary keys
# channel = {"Name": "Fall in Python",
#            "Videos": 12,
#            "Content": ["Python Tutorial",
#                        "Engineering",
#                        "Data Science"]
# 		  }
# keys = channel.keys()
# print(keys)


## method: dictionary.values()
##         => returns a list of all dictionary values
# channel = {"Name": "Fall in Python",
#            "Videos": 12,
#            "Content": ["Python Tutorial",
#                        "Engineering",
#                        "Data Science"]
# 		  }
# values = channel.values()
# print(values)


## method: dictionary.items()
#         => returns all key-value pairs
# channel = {"Name": "Fall in Python",
#            "Videos": 12,
#            "Content": ["Python Tutorial",
#                        "Engineering",
#                        "Data Science"]
# 		  }
# items = channel.items()
# print(items)

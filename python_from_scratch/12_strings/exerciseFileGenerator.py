import random

# generate exercise file
years = 2
with open("exercise.txt","w") as file:
    file.write("#"*20+"\n")
    file.write("# Fictitious Lotto #"+"\n")
    file.write("#"*20+"\n")
    for i in range(1,52*years+1):
        file.write("# week " + str(i) + "\n")
        file.write("numbers: {}, {}, {}, {}, {}, {}\n".format(random.randint(0, 40),
                                                         random.randint(0, 40),
                                                         random.randint(0, 40),
                                                         random.randint(0, 40),
                                                         random.randint(0, 40),
                                                         random.randint(0, 40)))

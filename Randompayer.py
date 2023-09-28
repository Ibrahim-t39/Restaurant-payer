# Split string method
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

import random

no = len(names)
buyer = random.randint(1,no)

print(names[buyer - 1] + ' is going to buy the meal today!')
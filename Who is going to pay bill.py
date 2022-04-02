import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
list_size = len(names)
random_number = random.randint(0,list_size-1)
print(f"{names[random_number]} is going to pay the bill")

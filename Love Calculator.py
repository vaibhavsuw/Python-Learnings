print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower_case = name1.lower()
name2_lower_case = name2.lower()

true_count = name1_lower_case.count('t')+name1_lower_case.count('r')+name1_lower_case.count('u')+name1_lower_case.count('e') + name2_lower_case.count('t')+name2_lower_case.count('r')+name2_lower_case.count('u')+name2_lower_case.count('e')
love_count = name1_lower_case.count('l')+name1_lower_case.count('o')+name1_lower_case.count('v')+name1_lower_case.count('e') + name2_lower_case.count('l')+name2_lower_case.count('o')+name2_lower_case.count('v')+name2_lower_case.count('e') 
count_int = int(str(true_count) + str(love_count))


if(count_int<10 or count_int>90):
    print(f"Your score is {count_int}, you go together like coke and mentos.")
elif(count_int>40 and count_int<50):
    print(f"Your score is {count_int}, you are alright together.")
else:
    print(f"Your score is {count_int}.")


print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
bill_in_float = float(bill)
tip_percentage = input("How much tip would you like to give? 10, 12, or 15? ")
tip_percentage_in_float = float(tip_percentage)
people = input("How many people to split the bill? ")
people_in_int = int(people)
per_person_split = (bill_in_float + (bill_in_float * tip_percentage_in_float/100))/people_in_int
per_person_split_round = round(per_person_split,2)
print(f"Each person shoud pay: ${per_person_split_round}")

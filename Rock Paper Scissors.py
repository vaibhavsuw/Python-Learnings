rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

arr = [rock,paper,scissors]
size = len(arr)
import random
computer_input = random.randint(0,size-1)
computer_choice = arr[computer_input]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
user_choice = arr[user_input]
print(computer_choice)
print(user_choice)
if(computer_input == user_input):
  print("Draw")
elif(user_input ==0 and computer_input == 2):
  print("You Won")
elif(user_input ==1 and computer_input == 0):
  print("You Won")
elif(user_input ==2 and computer_input == 1):
  print("You Won")
else:
  print("You Lose")
  

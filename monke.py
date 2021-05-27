import random
rps_choice = input("fight me rock paper scissors r for rock p for paper s for scissors")
if rps_choice.lower() == "r":
  print("you picked rock")
elif rps_choice.lower() == "p":
  print("you picked paper")
elif rps_choice.lower() == "s":
  print("you picked scissors")
else:
  print("wrong")
computer_choice = ["rock", "paper", "scissors"]
computer_pick = random.choice(computer_choice)
print("computer chose",computer_pick)

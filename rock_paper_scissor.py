import random

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

rps_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randrange(0, 3)

# print(computer_choice)

if computer_choice == 0:
    print(f"Computer chose {computer_choice}(rock) {rock}")
    
    if rps_choice == 0:
        print(f"The computer chose Rock and you chose {rps_choice} (rock){rock}. It's a tie.")
    elif rps_choice == 1:
        print(f"The computer chose rock but you chose {rps_choice} (paper){paper}. You win!")
    elif rps_choice == 2:
        print(f"The computer chose rock but you chose {rps_choice} (scissors){scissors}. You lose :(")
    else:
        print("Please choose from the options listed above.")
elif computer_choice == 1:
    print(f"Computer chose {computer_choice} (paper){paper}")
    
    if rps_choice == 0:
        print(f"The computer chose {computer_choice} and you chose {rps_choice} (rock){rock}. You lose :(")
    elif rps_choice == 1:
        print(f"The computer chose {computer_choice} but you chose {rps_choice} (paper){paper}. It's a tie.")
    elif rps_choice == 2:
        print(f"The computer chose {computer_choice} but you chose {rps_choice} (scissors){scissors}. You win!")
    else:
        print("Please choose from the options listed above.")
elif computer_choice == 2:
    print(f"Computer chose {computer_choice} (scissors){scissors}")

    if rps_choice == 0:
        print(f"The computer chose {computer_choice} and you chose {rps_choice} (rock){rock}. You win!")
    elif rps_choice == 1:
        print(f"The computer chose {computer_choice} but you chose {rps_choice} (paper){paper}. You lose :(")
    elif rps_choice == 2:
        print(f"The computer chose {computer_choice} but you chose {rps_choice} (scissors){scissors}. It's a tie.")
    else:
        print("Please choose from the options listed above.")

else:
    print("Game over.")
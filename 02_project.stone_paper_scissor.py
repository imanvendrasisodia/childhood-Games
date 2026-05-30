# using python to create a game of stone paper scissor
import random
computer = random.choice([1,2,3])
user = input ("enter your choice : ")
youdict = {"stone":1,"paper":2,"scissor":3}
if(user in youdict):
    you = youdict[user]
else:    print("invalid choice !") 
reversed_dict = {1:"stone",2:"paper",3:"scissor"}
print(f"you  choose: {reversed_dict[you]} \n computer choose: {reversed_dict[computer]}")
if(you == computer):
    print("ohho! It's a draw! ")
else:
    if(you == 1 and computer == 3):
        print("hurray! you win! ")
    elif(you == 2 and computer == 1):
        print("hurray! you win! ")
    elif(you == 3 and computer == 2):
        print("hurray! you win! ")
    else:
        print("ohho! Computer wins! ")
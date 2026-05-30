# to generate a game using python snake water gun 
'''
for 
1 = snake
0 = water  
-1 = gun
'''
import random
computer = random.choice([1,-1,0])
user = input ("enter your choice : ")

youdict = {"snake":1,"water":0,"gun":-1}
if(user in youdict):
    you = youdict[user]
else:    print("invalid choice !")

reversed_dict = {1:"snake",0:"water",-1:"gun"}
print(f"you  choose: {reversed_dict[you]} \n computer choose: {reversed_dict[computer]}")

if(you == computer):
    print("ohho! It's a draw! ")
else:
    if(you == 1 and computer == 0):
        print("hurray! you win! ")
    elif(you == 0 and computer == -1):
        print("hurray! you win! ")
    elif(you == -1 and computer == 1):
        print("hurray! you win! ")
    else:
        print("ohho! Computer wins! ")
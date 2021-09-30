import random

number = int(input("Please Enter Your guess Number :"))
randomNumber = random.randint(1,6)

if(number==randomNumber):
    print("you are won")
else:
    print("you are lose", f"the number is {randomNumber}")

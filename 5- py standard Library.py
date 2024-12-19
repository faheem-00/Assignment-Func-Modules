import math
import random

#Hypotenuse

def pythogoras(a,b):
    length_tri= math.sqrt(a**2 + b**2)
    return length_tri
result= pythogoras(10,12)
print(result)


#Guess the Number game
num= random.randrange(1,50)

user_guess= int(input("Enter ur Guess:"))
if user_guess==num:
    print("Your guess is Right")
else:
    print("Your guess is Wrong")
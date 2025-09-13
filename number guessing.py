import random
Cnumber=random.randrange(1,102)
userInput=int(input("Enter your number:"))
if userInput>Cnumber:
    print("Computer number",Cnumber)
    print("Your guess number is high")
elif Cnumber>userInput:
    print("Computer number",Cnumber)
    print("Your guess number is low")
else:
    print("Computer number",Cnumber)
    print("Your guess number is equal")
    
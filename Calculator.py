num1=int(input("Enter the value1:10"))

num2=int(input("Enter the value2:"))

opr=input("Enter the operation:")

if opr=="+":
    print(num1+num2)
    
elif opr=="-":
    print(num1-num2)
    
elif opr=="*":
    print(num1*num2)
    
elif opr=="/":
    print(num1/num2)
    
else:
    print("Invalid operation")
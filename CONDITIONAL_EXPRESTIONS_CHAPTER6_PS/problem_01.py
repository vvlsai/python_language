# write a program to find the greatest of four numbers entered by the user

a1=int(input("enter number1: "))
a2=int(input("enter number2: "))
a3=int(input("enter number3: "))
a4=int(input("enter number4: "))
if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is greatest number is a1",a1)
elif(a2>a3 and a2>a4 and a4>a1):
    print("a2 is greatest number ",a2)
elif(a3>a4 and a3>a2 and a3>a1):
    print("a3 is greatest number :",a3)
elif(a4>a3 and a4>a2 and a4>a1):
    print("a4 is a greatest number : ",a4)


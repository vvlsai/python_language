# write a program to caliculate the the grade of a students from this marks from the follow ing scheme :
# 90-100=>ex
# 80-90=>a
# 70-80=>b
# 60-70=>c
# 50-60=>de
# <50=>f
marks=int(input("Enter your  marks: "))
if(marks<=100 and marks>90):
    print ("exelant")
elif(marks<=90 and marks>80):
    print(" you get gread A")
elif(marks<=80 and marks>70):
    print("you get gread B")
elif(marks<=70 and marks>60):
    print("you get gread c")
elif(marks<=60 and marks>50):
    print("you get gread D")
elif(marks<50):
    print("you get gread F")

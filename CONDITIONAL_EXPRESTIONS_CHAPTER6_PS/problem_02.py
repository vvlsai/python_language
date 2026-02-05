# write a program to find out whether A STUDENT HAS  passed or faild requires a total of 40% and at leastn 33% in each subject to pass assume 3 subjects and take marks as an input from the ?
marks1=int(input("enter marks 1: "))
marks2=int(input("enter marks 2: "))
marks3=int(input("enter marks 3: "))
# check for total persentage
total_persentage=((marks1+marks2+marks3)*100)/300
print("your persentage",total_persentage)
if(total_persentage>40 and marks1>33 and marks2>33 and marks3>33 ):
    print("your pass")
else:
    print("your fail")
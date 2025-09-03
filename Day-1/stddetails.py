stdnum=eval(input("enter number: "))
stdname=input("enter name: ")
print("enter 3 subject marks")
stdma1=eval(input("enter 1st marks: "))
stdma2=eval(input("enter 2nd marks: "))
stdma3=eval(input("enter 3rd marks: "))
total=stdma1+stdma2+stdma3
avg=total/3
ans=round(avg,2)
print(f"student_name:{stdname} ,  student_number:{stdnum}, total_marks:{total}, average_marks:{ans}")
def check(a):
    x=""
    if(a>=40):
        if(a<=50):
            x="c grade"
        elif(a>50 and a<=70):
            x="b grade"
        elif(a>71 and a<=80):
            x="a grade"
        else:
            x="distinction"
    else:
        x="fail"
    return x
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
print("1st result",check(stdma1))
print("2nd result",check(stdma2))
print("3rd result",check(stdma3))


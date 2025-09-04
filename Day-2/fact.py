a=int(input("enter num: "))
fact=1
if(a<0):
    print("fact not exist")
elif(a==0):
    print("fact=1")
else:
    temp=a
    while temp>0:
        fact*=temp
        temp-=1
    print(fact)
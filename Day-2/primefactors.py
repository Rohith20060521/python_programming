def prime(x):
    count=0
    if(x<=1):
        return False
    for i in range(2,x+1):
        if(x%i==0):
            count+=1
    if(count>1):
        return False
    else:
        return True
a=int(input("enter num: "))
for i in range(1,a):
    if(a%i==0 and prime(i)==True):
        print(i)
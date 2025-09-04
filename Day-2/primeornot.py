a=int(input("enter num: "))
count=1
if(a<=1):
    print("neither prime nor composite")
for i in range(2,a):
    if(a%i==0):
        count+=1
    else:
        count+=0
if(count>1):
    print("comp")
else:
    print("prime")

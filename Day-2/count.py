a=int(input("enter num: "))
count=0
num=a
while(num>0):
    a=num%10
    count+=1
    num=num//10
print(count)

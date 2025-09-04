a=int(input("enter num: "))
sum=0
num=a
while(num>0):
    a=num%10
    sum+=a
    num=num//10
print(sum)

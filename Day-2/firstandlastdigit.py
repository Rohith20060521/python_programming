a=int(input("enter num: "))
fd=0
temp=a
num=a
while(num>0):
    a=num%10
    fd=a
    num=num//10
print("first digit:",fd)
ld=temp%10
print("last digit:",ld)

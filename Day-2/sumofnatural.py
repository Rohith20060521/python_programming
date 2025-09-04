n=int(input("enter num: "))
def nat():
    i=1
    sum=0
    while(i<=n):
        sum+=i
        i+=1
    return sum
a=nat()
print(a)
n=int(input("enter num: "))
for i in range(1,n+1):
    print(i)
print("using while: ")
def nat():
    i=1
    while(i<=n):
        print(i)
        i+=1
nat()
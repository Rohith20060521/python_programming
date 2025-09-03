def calcnum(n):
    x=""
    if n%2==0:
        x="even"
    else:
        x="odd"
    return x
a=int(input("enter number: "))
z=calcnum(a)
print(z)
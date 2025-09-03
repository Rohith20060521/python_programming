def check(x):
    d=""
    if x>=0:
        d="positive"
    else:
        d="negative"
    return d
a=int(input("enter number: "))
z=check(a)
print(f"{a} is a {z} number")
def week(a):
    x=""
    if a==1:
        x="Sunday"
    elif a==2:
        x="Monday"
    elif a==3:
        x="Tuesday"
    elif a==4:
        x="Wednesday"
    elif a==5:
        x="Thursday"
    elif a==6:
        x="Friday"
    elif a==7:
        x="Saturday"
    else:
        x="Invalid number"
    return x
x=int(input("enter number: "))
y=week(x)
print(f"{x}={y}")
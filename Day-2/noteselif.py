def count(x):
    if x>=2000:
        n=x//2000
        return f"{n} 2000 notes"+" "+count(x-2000*n)
    elif x>=500:
        n=x//500
        return f"{n} 500 notes"+" "+count(x-500*n)
    elif x>=200:
        n=x//200
        return f"{n} 200 notes"+" "+count(x-200*n)
    elif x>=100:
        n=x//100
        return f"{n} 100 notes"+" "+count(x-100*n)
    elif x>=50:
        n=x//50
        return f"{n} 50 notes"+" "+count(x-50*n)
    elif x>=20:
        n=x//20
        return f"{n} 20 notes"+" "+count(x-20*n)
    elif x>=10:
        n=x//10
        return f"{n} 10 notes"+" "+count(x-10*n)
    elif x>=5:
        n=x//5
        return f"{n} 5 notes"+" "+count(x-5*n)
    elif x>=2:
        n=x//2
        return f"{n} 2 notes"+" "+count(x-2*n)
    elif x>=1:
        n=x//1
        return f"{n} 1 notes"+" "+count(x-1*n)
    elif x==0:
        return ""
    else:
        return "invalid"
a=int(input("enter num: "))
x=count(a)
print(x)



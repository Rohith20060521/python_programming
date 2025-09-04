def factors(x):
    for i in range(1,x):
        if(x%i==0):
            print(i,end=" ")
a=int(input("enter num: "))
factors(a)
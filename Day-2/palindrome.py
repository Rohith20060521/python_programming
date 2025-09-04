def palin(n): 
    for i in range(1, n):
        num = i
        rev = 0
        while num > 0:
            r = num % 10
            rev = rev * 10 + r
            num = num // 10
        if rev == i:
            print(i)
a = int(input("Enter a number: "))
palin(a)

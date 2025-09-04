a = int(input("Enter a number: "))
for k in range(2, a + 1):  
    is_prime = True
    for i in range(2, int(k ** 0.5) + 1): 
        if k % i == 0:
            is_prime = False
            break
    if is_prime:
        print(k, end=" ")

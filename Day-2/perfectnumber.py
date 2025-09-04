def is_perfect(num):
    divisors_sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print("Perfect numbers in the range:")
for n in range(start, end + 1):
    if is_perfect(n):
        print(n, end=" ")
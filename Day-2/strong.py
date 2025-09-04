import math
def is_strong(num):
    digits = str(num)
    total = sum(math.factorial(int(d)) for d in digits)
    return total == num
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print("Strong numbers in the range:")
for n in range(start, end + 1):
    if is_strong(n):
        print(n, end=" ")
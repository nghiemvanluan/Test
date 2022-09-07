n = int(input())

def sumOf(n):
    sum = 3
    for i in range (1, n + 1):
        if (n % i == 0) and i < n:
            sum += i 
    return sum 

print(sumOf(n))

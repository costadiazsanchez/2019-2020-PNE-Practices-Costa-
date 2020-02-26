def fibosum(n):

    x = 0
    y = 1
    sum = 0
    count = 0

    while count < n:
        aux = x + y
        x = y
        y = aux
        count = count + 1
        sum = sum + x
    return sum

print("Sum of the First 5 terms of the Fibonacci series: ", fibosum(5))
print("Sum of the First 10 terms of the Fibonacci series: ", fibosum(10))
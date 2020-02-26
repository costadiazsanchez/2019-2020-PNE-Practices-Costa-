def fib (n):
    x = 0
    y = 1
    sum = 0
    count = 0

    while count < n:
        aux = x + y
        x = y
        y = aux
        count = count + 1
    return (x)

print ("5th Fibonacci term: ", fib (5))
print ("10th Fibonacci term: ", fib (10))
print ("15th Fibonacci term: ", fib (15))
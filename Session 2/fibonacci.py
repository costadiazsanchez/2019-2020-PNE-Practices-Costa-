x = 0
y = 1
number = 11
count = 0

while  count < number:
    print (x, end = ' ')
    aux = x + y
    x = y
    y = aux
    count  = count + 1
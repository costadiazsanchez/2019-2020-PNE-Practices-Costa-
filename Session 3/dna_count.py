input_user = input("Introduce the sequence: ")

count_A = 0
count_C = 0
count_T = 0
count_G = 0

print("Total length: ", len(input_user))

for i in input_user:
    if i == 'A':
        count_A = count_A + 1
    elif i == 'C':
        count_C = count_C + 1
    elif i == 'G':
        count_G = count_G + 1
    elif i == 'T':
        count_T = count_T + 1

print("A: ", count_A)
print("C: ", count_C)
print("G: ", count_G)
print("T: ", count_T)
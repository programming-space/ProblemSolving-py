def sum_of_digits(num):
    binary_val = str(bin(num)[2:])
    sum = 0
    for i in binary_val:
        sum += int(i)
    return sum

num = int(input())
print(sum_of_digits(num))
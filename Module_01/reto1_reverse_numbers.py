def reverse (num):
    val = str(num)
    val = val[::-1]

    if (isinstance(num,int)):
        num = int(val)
    else:
        num = float(val)
    return num

numero = 12345.24
print(reverse(numero))

def unique_char (pal):
    palabra = []
    palabra[:0] = pal

    print(palabra)


    for index in range(len(palabra)):
        if palabra.count(palabra[index]) == 1:
            return index
        elif index == len(palabra)-1:
            return -1

palabra = "selenium"
print(unique_char(palabra))
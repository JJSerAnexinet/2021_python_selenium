list = [5, 10, 15, 20, 25, 50, 20]

for i in range(len(list)):
    if list[i] == 20:
        list[i] = 200

print(list)
print(list[2:6])
list1 = ['Hello', 'take']
list2 = ['Dear', 'Sir']
solution = []


for i in list1:
    for j in list2:
        solution.append(f'{i}-{j}')

print(f'Solution: {solution}')
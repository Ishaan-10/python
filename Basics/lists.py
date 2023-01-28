names = ["John","Ishaan","Aditya"]
print(names)
print(names[1])
print(names[0:-2])
print(names[1:])
print(names[:])
names[1]='Ansh'

# largest in list
names=[12,13,15,16]
print("max is "+str(((max(names)))))
print("index of max is "+str(names.index((max(names)))))

# 2d
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    for col in row:
        print(col)

# list methods
list = [1,2,3,4,5]
list.append(6)
list.insert(0,5)
list.pop()
list.remove(5)
list.sort()
# list.clear()
list.reverse()
list2 = list.copy()
print(list)
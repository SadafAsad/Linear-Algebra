import itertools
num = [[10, 20], [40], [30, 56, 25], [20, 10], [33], [40]]
print("Original List", num)
for i in num:
    i.sort()
num.sort()
new_num = list(num for num,_ in itertools.groupby(num))
print("New List", new_num)
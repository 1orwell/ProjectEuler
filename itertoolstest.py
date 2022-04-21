import itertools

total = 0

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
for element in itertools.product(lst, repeat=len(lst)):
    if element[0] == 0:
        print(element)
        total += 1
    else:
        break
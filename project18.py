#work in progress
import itertools

triangle = [[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20, 4,82,47,65],
[19,1, 23, 75, 3, 34],
[88,2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]
"""

triangle = [[75],
[95,64],
[17,47,82]]

permutations_of_tuples = []
permutations_of_lists = []

#Attempting to list all permutations of the indexes
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#lst = [0, 1, 2]
for element in list(itertools.product(lst, repeat=len(lst))):
    permutations_of_tuples.append(element)
    if element[0] != 0:
        break

for tup in permutations_of_tuples:
    # Only want the paths that start with index 0
    if tup[0] == 0:
        permutations_of_lists.append(list(tup))

for path in permutations_of_lists:
    print(f'Path is {path}')

lst_to_remove = []

for perm_list in permutations_of_lists:
    previous_val = perm_list[0]
    for current_val in perm_list:
        remove = True
        if previous_val == current_val:
            remove = False 
        if previous_val + 1 == current_val:
            remove = False
        if remove == True:
            lst_to_remove.append(perm_list)
            break
        previous_val = current_val

for wrong_perm in lst_to_remove:
    permutations_of_lists.remove(wrong_perm)

for perm_list in permutations_of_lists:
    print(perm_list)

We have now worked out every possible path along the triangle, we now just have to add each one and
keep track of the largest.

total = 0
max = 0

for path in permutations_of_lists:
    for index, row in enumerate(triangle):
        print(f'looking at row {row} and taking {path}')
        index_in_row = path[index]
        val = row[index_in_row]
        total += val
    if total > max:
        max = total
    total = 0

print(max)

"""

#Other method: start at the bottom of the traingle and work up, pass the the value above
# the largest of the two possible values it could be added to - recursion

triangle = [[75],
[95,64],
[17,47,82]]

def recurs_tri(triangle, row, index):
    current_val = triangle[row][index]
    val_from_below = max((triangle[row+1][index], triangle[row+1][index+1]))
    
    if row == len(triangle)-2:
        return current_val + val_from_below 
    
    for row in triangle:
        for val in row:
            val_from_below = max((triangle[row+1][index], triangle[row+1][index+1]))
            return current_val + recurs_tri(val_from_below, index+1, row+1)

print(recurs_tri(triangle, 0, 0))




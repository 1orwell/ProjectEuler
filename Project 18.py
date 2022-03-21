#work in progress

import itertools

triangle = [[75],
[95,64],
[17,47,826],
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


previous_index = 0
first_val = triangle[0][0]
total = first_val
totals_list = []
num_of_rows = len(triangle)
list_of_rows = [*range(0,num_of_rows,1)]
print(list_of_rows)
permutations_of_tuples = []
permutations_of_lists = []

#Attempting to list all permutations of indexes of list and remove lists who's consecutive items wouldn't be agecent in the triangle
#problem is that the solution takes up too much memory for the size of the triangle given
for element in list(itertools.permutations(list_of_rows)):
    permutations_of_tuples.append(element)

for tup in permutations_of_tuples:
    permutations_of_lists.append(list(tup))

for perm_list in permutations_of_lists:
    print(type(perm_list))
    previous_val = perm_list[0]
    current_val = perm_list[0]
    for val in perm_list:
        current_val = val
        if current_val != previous_val or previous_val + 1 != current_val:
            permutations_of_lists.remove(perm_list)
        previous_val = val

for perm_list in permutations_of_lists:
    print(perm_list)

"""
for row in triangle[1:]:
    val_a = row[previous_index]
    val_b = row[previous_index+1]
    if val_a > val_b:
        previous_index = previous_index
    else:
        previous_index = previous_index+1
    total = total + max(val_a,val_b)

print(total)
"""
    
        
    

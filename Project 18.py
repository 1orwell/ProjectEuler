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
permutations = []

#Attempting to list all permutations of 1 and 0 of height of the triangle
for element in list(itertools.permutations([1,2,3])):
    permutations.append(element)

for perm_list in permutations:
    for i in range(1,4):
        for val in perm_list:
            if val == i:
                x = 0
            else:
                x=1
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
    
        
    

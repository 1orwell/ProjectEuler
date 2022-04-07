import itertools

for i, pattern in enumerate(itertools.permutations(range(10))):
    # add 1 as it starts counting from 0
    if i+1 == 1000000:
        print(pattern)
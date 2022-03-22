#work in progress
#Need to redo entire approach - currently reseraching dynamic programming


import itertools

# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict

# This class represents a directed graph using
# adjacency list representation


class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# A function used by DFS
	def DFSUtil(self, v, visited):

		# Mark the current node as visited
		# and print it
		visited.add(v)
		print(v, end=' ')

		# Recur for all the vertices
		# adjacent to this vertex
		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)

	# The function to do DFS traversal. It uses
	# recursive DFSUtil()
	def DFS(self, v):

		# Create a set to store visited vertices
		visited = set()

		# Call the recursive helper function
		# to print DFS traversal
		self.DFSUtil(v, visited)

# Driver code


# Create a graph given
# in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 6)
g.addEdge(3, 7)
g.addEdge(4, 7)
g.addEdge(4, 8)
g.addEdge(5, 8)
g.addEdge(5, 9)

print("Following is DFS from (starting from vertex 0)")
g.DFS(0)

# This code is contributed by Neelam Yadav



"""

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
#list_of_rows = [*range(0,num_of_rows,1)]
permutations_of_tuples = []
permutations_of_lists = []

#Attempting to list all permutations of the indexes
for element in list(itertools.permutations([0,1,2])):
    permutations_of_tuples.append(element)

for tup in permutations_of_tuples:
    permutations_of_lists.append(list(tup))

for perm_list in permutations_of_lists:
    print(perm_list)

#Removing any permutations that mean the value taken from the triangle wouldn't be agacent to the item above
# I can hear my computer whir when it gets to this point
# For some reason, this is skipping out the third possible permutation? Possible indexing error?
for perm_list in permutations_of_lists:
    index=0
    previous_val = perm_list[0]
    current_val = perm_list[0]
    indexing_check = 0
    print("in list " + str(perm_list) + " of the list of permutations")
    for val in perm_list:
        print("val is "+str(val))
        print("this should not be more than "+str(indexing_check))
        if val>indexing_check:
            print("removing this list")
            indexing_check = 0
            del permutations_of_lists[index]
            #index += 1
            break
        indexing_check += 1
    index += 1

for perm_list in permutations_of_lists:
    print(perm_list)

    index=0
    for val in perm_list:
        current_val = val
        if current_val != previous_val or previous_val + 1 != current_val:
            del permutations_of_lists[index]
        previous_val = val
        index += 1
for perm_list in permutations_of_lists:
    print(perm_list)

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
        
    


LP part:

Tell me about the most significant technical challenge. How did you resolve it?
Tell me about the case, when you simplified a complicated solution? How did you simplify? Why was the first version over-complicated?


1. BSTs
2. Hashmaps
3. Strings
4. Arrays - Binary Search.
5  Graphs - bfs, dfs topoloogical sort


# topological sort
# assuming that we have an adjacency list

E - [H F]
H - [D]
F - [G]
D = []
G = []

#      E
#    /   \  
#   H     F
#   /     \
#  D       G


[E,H,D]



def find_order(ajacency_list, start vertex):
    stack = [] # extract elements after all childrens visited
    visited_set = set() # maintaing list of visited vertices
    stack.append(start_vertex)
    while stack:
        has_children = False
        for vertex in adjaceny_list[stack[-1]]:
            if vertex not in visited_set:
                stack.append(vertex)
                has_children = True
        if not has_children:
            visited_set.add(stack.pop())

def extract_children(start_vertex):



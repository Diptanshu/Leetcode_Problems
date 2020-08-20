import collections
out_edge_map = collections.defaultdict(set)
in_edge_map = collections.defaultdict(set)
outdegree = collections.Counter()
seqs = [[5,2,6,3],[4,1,5,3,2]] 
# 4 -> 1 -> 5 -> 2 -> 6 -> 3
unique_vertices = set()
for idx, vertex_list in enumerate(seqs):
	n = len(vertex_list)
	for v_index, vertex_num in enumerate(vertex_list):
		unique_vertices.add(vertex_num)
		if v_index < n-1:
			if vertex_list[v_index+1] not in out_edge_map[vertex_num]:
				outdegree[vertex_num] += 1
				if outdegree[vertex_num] > 1:
					return False
			out_edge_map[vertex_num].add(vertex_list[v_index+1])
			in_edge_map[vertex_list[v_index+1]].add(vertex_num)




result, output = [], []
for vertex_num in unique_vertices:
	if vertex_num not in out_edge_map:
		result.append(vertex)

while result:
	v_num = result.pop()
	output.append(v_num)
	for neighbours in in_edge_map[v_num]:
		out_edge_map[neighbours].remove(v_num)
		if not out_edge_map[neighbours]:
			result.append(neighbours)
	out_edge_map.pop(v_num)



'''
def findOrder(self, numCourses, prerequisites):
    dic = collections.defaultdict(set)
    neigh = collections.defaultdict(set)
    for i, j in prerequisites:
        dic[i].add(j)
        neigh[j].add(i)
    stack = [i for i in xrange(numCourses) if not dic[i]]
    res = []
    while stack:
        node = stack.pop()
        res.append(node)
        for i in neigh[node]:
            dic[i].remove(node)
            if not dic[i]:
                stack.append(i)
        dic.pop(node)
    return res if not dic else []

'''


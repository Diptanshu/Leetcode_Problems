def findOrder(self, n, prerequisites):
    G = [set() for _ in range(n)]
    for d, s in prerequisites:
        G[s].add(d)
    vis, orders = [0] * n, []

    def dfs_circle(x):
        vis[x] = -1
        for y in G[x]:
            if vis[y] < 0 or (not vis[y] and dfs_circle(y)):
                return True
        vis[x] = 1
        orders.append(x)
        return False

	for x in range(numCourses):
	    if not vis[x] and dfs_circle(x):
	        return []
    return orders[::-1]

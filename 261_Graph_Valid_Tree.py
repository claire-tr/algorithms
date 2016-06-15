class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # tree is a graph without cycles
        # Has n-1 edges and is acyclic.
        # Has n-1 edges and is connected.

        # 1. Exact number of edges
        if len(edges) != n - 1:
            return False

        # 2. Each node can be visited
        neighbors = {i:[] for i in range(n)}
        for v, w in edges:
            neighbors[v].append(w)
            neighbors[w].append(v)
        queue = [0]
        while queue:
            i = queue.pop()
            if i in neighbors:
                queue.extend(neighbors.pop(i))

        return not neighbors

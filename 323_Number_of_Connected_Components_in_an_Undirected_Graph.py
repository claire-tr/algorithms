class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        #BFS
        if n <= 0:
            return 0
        neighbors = {i:[] for i in range(n)}

        for v, w in edges:
            neighbors[v].append(w)
            neighbors[w].append(v)
        queue = []
        i = 0

        while neighbors:
            i += 1
            queue.append(neighbors.keys()[0]) # stores connected node
            while queue:
                node = queue.pop(0)
                if node in neighbors:
                    queue.extend(neighbors.pop(node))
            # if neighbors is not None, means that there's still nodes that are not anyone's neighbors
        return i

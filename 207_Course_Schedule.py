class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Equivalent to finding if a cycle exists in a directed graph
        # Topological Sort (Motivation: sequence tasks while respecting all precedence constraints)
        # Has a directed cycle => No topological ordering
        status = [0] * numCourses # 0: not visited, 1: visiting, 2: visited
        graph = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(i):
            if status[i] == 1:
                return False
            if status[i] == 2:
                return True
            status[i] = 1
            for j in graph[i]:
                if not dfs(j):
                    return False
            status[i] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

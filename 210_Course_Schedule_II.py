class Solution(object):
    def findOrder_BFS(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        from collections import deque
        # This question asks for an order in which prerequisite courses must be taken first.
        # This prerequisite relationship reminds one of directed graphs.
        # Then, the problem reduces to find a topological sort order of the courses,
        # which would be a DAG if it has a valid order.
        inLinkCounts = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        # initialize graph
        # The first step is to transform it into a directed graph. Since it is likely to be sparse,
        # we use adjacency list graph data structure. 1 -> 2 means 1 must be taken before 2.
        for x, y in prerequisites:
            inLinkCounts[x] += 1
            graph[y].append(x)
        # How can we obtain a topological sort order of a DAG?

        # We observe that if a node has incoming edges, it has prerequisites.
        # Therefore, the first few in the order must be those with no prerequisites, i.e. no incoming edges.
        # Any non-empty DAG must have at least one node without incoming links.
        # If we visit these few and remove all edges attached to them, we are left with a smaller DAG,
        # which is the same problem. This will then give our BFS solution.
        toVisit = deque()
        order = []
        for i in range(numCourses):
            if inLinkCounts[i] == 0:
                toVisit.append(i)
        while toVisit:
            i = toVisit.popleft()
            order.append(i)
            for j in graph[i]:
                inLinkCounts[j] -= 1
                if inLinkCounts[j] == 0:
                    toVisit.append(j)

        return order if len(order) == numCourses else []

    def findOrder(self, numCourses, prerequisites):
        """
        This question asks for an order in which prerequisite courses must be taken first.
        This prerequisite relationship reminds one of directed graphs.
        Then, the problem reduces to find a topological sort order of the courses,
        which would be a DAG(Directed Acyclic Graph) if it has a valid order.
        """
        stack = []
        status = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            # prerequisites, so the order of x:y should be y pointing to x.
            graph[y].append(x)
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
            stack.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return stack[::-1]
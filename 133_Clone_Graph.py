# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return node
        # Undirected, need a dict to store visit status
        # Deep copy
        dic = {}
        queue = [node, ]
        dic[node] = UndirectedGraphNode(node.label)
        while queue:
            cur = queue.pop(0)
            for n in cur.neighbors:
                if n not in dic:
                    dic[n] = UndirectedGraphNode(n.label)
                    queue.append(n)
                dic[cur].neighbors.append(dic[n])
        return dic[node]
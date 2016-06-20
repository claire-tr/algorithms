class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return

        inf = 2147483647
        queue = []

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append([i, j , 0])
        while queue:
            i, j, n = queue.pop(0)

            if i-1 >= 0 and rooms[i-1][j] == inf:
                rooms[i-1][j] = n + 1
                queue.append([i-1, j, n+1])

            if i+1 < len(rooms) and rooms[i+1][j] == inf:
                rooms[i+1][j] = n + 1
                queue.append([i+1, j, n+1])

            if j-1 >= 0 and rooms[i][j-1] == inf:
                rooms[i][j-1] = n + 1
                queue.append([i, j-1, n+1])

            if j+1 < len(rooms[0]) and rooms[i][j+1] == inf:
                rooms[i][j+1] = n + 1
                queue.append([i, j+1, n+1])

        # Is this the nearest?
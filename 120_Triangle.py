# https://discuss.leetcode.com/topic/1669/dp-solution-for-triangle
'''

    This problem is quite well-formed in my opinion. The triangle has a tree-like structure,
    which would lead people to think about traversal algorithms such as DFS.
    However, if you look closely, you would notice that the adjacent nodes always share a 'branch'.
    In other word, there are overlapping subproblems.   
    Also, suppose x and y are 'children' of k. Once minimum paths from x and y to the bottom are known,
    the minimum path starting from k can be decided in O(1), that is optimal substructure.
    Therefore, dynamic programming would be the best solution to this problem in terms of time complexity.
'''


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        dp = [n for n in triangle[-1]]

        for i in xrange(len(triangle) - 2, -1, -1):
            for j in xrange(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]
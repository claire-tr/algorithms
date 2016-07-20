#coding=utf-8

'''
    F(n) = F(1, n) + F(2, n) + ... + F(n, n).

    Optimal Substructure:
    Given a sequence 1…n, we pick a number i out of the sequence as the root,
    then the number of unique BST with the specified root F(i),
    is the cartesian product of the number of BST for its left and right subtrees.

    Overlapping Subproblems:
    the result only related to the number of the nodes, no need to care about the
    specific value of each node (1, 2 and 3, 4 share the same number)
'''

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in xrange(2, n + 1):
            for j in xrange(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]
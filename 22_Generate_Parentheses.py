class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        self.backtracking(n, n, [], results)
        return results

    def backtracking(self, left, right, res, results):
        # At each step, we have three states: number of '(' left, number of ')' left, and the current temporary result
        # print res, results
        if left == 0 and right == 0:
            results.append(''.join(res))
        if left > 0:
            # can add '('
            res.append('(')
            self.backtracking(left-1, right, res, results)
            res.pop()
        if right > left:
            # can add ')'
            res.append(')')
            self.backtracking(left, right-1, res, results)
            res.pop()

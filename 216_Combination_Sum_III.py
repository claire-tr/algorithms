class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []
        self.backtracking(1, k, n, [], results)
        return results

    def backtracking(self, start, k, n, temp, results):
        if k == 0 and n == 0:
            results.append(temp[::])
            return
        if k < 0 or n < 0:
            return
        while start < 10:
            temp.append(start)
            self.backtracking(start + 1, k - 1, n - start, temp, results)
            temp.pop()
            start += 1
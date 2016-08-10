class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        self.backtracking(candidates, 0, target, [], results)
        return results

    def backtracking(self, candidates, start, target, temp, results):
        if target < 0: return
        if target == 0:
            results.append(temp[::])
            return
        for i in range(start, len(candidates)):
            temp.append(candidates[i])
            self.backtracking(candidates, i, target - candidates[i], temp, results)
            temp.pop()
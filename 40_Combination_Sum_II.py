class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        self.backtracking(sorted(candidates), 0, target, [], results)
        return results

    def backtracking(self, candidates, start, target, temp, results):
        # print start, target, temp
        if target == 0:
            # print 'append'
            results.append(temp[::])
            return
        if target < 0 or start >= len(candidates):
            return
        while start < len(candidates):
            # print start
            temp.append(candidates[start])
            self.backtracking(candidates, start + 1, target - candidates[start], temp, results)
            temp.pop()
            while start < len(candidates) - 1 and candidates[start + 1] == candidates[start]:
                start += 1
            start += 1

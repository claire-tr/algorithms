class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        '''
            For each digits, enumerate all the possible character,
            add this possible character into the current solution,
            then go to the next index
        '''

        dic = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        self.helper(digits, 0, dic, [], res)
        return res

    def helper(self, digits, index, dic, cur, res):
        if index == len(digits):
            res.append(''.join(cur)) if cur else None
            return
        for c in dic[int(digits[index])]:
            cur.append(str(c))
            self.helper(digits, index + 1, dic, cur, res)
            cur.pop()
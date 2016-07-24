class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        '''
            For every character, we can keep it or abbreviate it.
            To keep it, we add it to the current solution and carry on backtracking.
            To abbreviate it, we omit it in the current solution, but increment the count,
            which indicates how many characters have we abbreviated.
            When we reach the end or need to put a character in the current solution,
            and the count is bigger than zero, we add the number into the solution
        '''
        res = []
        self.helper(word, '', 0, 0, res)
        return res

    def helper(self, word, cur, index, count, res):
        if index == len(word):
            if count > 0:
                cur += str(count)
            res.append(cur)
            return
        # omit this character
        self.helper(word, cur, index + 1, count + 1, res)

        # keep this character
        if count > 0:
            cur += str(count)
        self.helper(word, cur + word[index], index +1, 0, res)

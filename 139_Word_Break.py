class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        res = [False] * (len(s)+1)
        # End at this position
        res[0] = True

        for i in range(1, len(s)+1):
            if s[0:i] in wordDict:
                res[i] = True
                continue
            for j in range(i+1):
                if res[j] and s[j:i] in wordDict:
                    res[i] = True
                    continue
        return res[len(s)]
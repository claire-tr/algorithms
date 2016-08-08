# coding=utf-8
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        We use a boolean vector dp[]. dp[i] is set to true if a valid word (word sequence) ends there.
        The optimization is to look from current position i back and
        only substring and do dictionary look up in case the preceding position j with dp[j] == true is found.

        subproblems: substrings match in the wordDict
        they are overlapping

        break down into substrings, looking for the valid break down points

        既然动态规划需求存储历史信息，那我们首先应该确认我们要存储的历史信息。
        这里我用boolean location[i]表示到字符串s的第i个字符时，是否可以用dict中的词来表示。

        """
        dp = [True] + [False] * len(s)

        for i in xrange(1, len(s) + 1):
            for j in xrange(0, i+1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    continue
        return dp[len(s)]
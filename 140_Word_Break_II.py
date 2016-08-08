# coding=utf-8
class Solution(object):
    def wordBreak_II_one(self, s, wordDict):
        dp = [True] + [False] * len(s)
        for i in xrange(1, len(s) + 1):
            for j in xrange(0, i+1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    continue

        end, res = len(s), []
        for i in xrange(len(dp) - 2, -1, -1):
            if dp[i] and s[i:end] in wordDict:
                res.insert(0, s[i:end])
                end = i

        return ' '.join(res)

    def wordBreak_backtracking(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        results = []
        self.backtracking(s, wordDict, 0, [], results)
        return results

    def backtracking(self, s, wordDict, start, temp, results):
        if start == len(s):
            results.append(' '.join(temp))
            return
        for i in xrange(start + 1, len(s) + 1):
            if s[start:i] in wordDict:
                temp.append(s[start:i])
                self.backtracking(s, wordDict, i, temp, results)
                temp.pop()


if __name__ == '__main__':
    s = Solution()
    str = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print s.wordBreak_II_one(str, wordDict)

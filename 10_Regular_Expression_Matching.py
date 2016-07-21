class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        '''
            http://xiaohuiliucuriosity.blogspot.com/2014/12/regular-expression-matching.html
            dp[i][j]: if s[0..i-1] matches p[0..j-1]
            if p[j - 1] != '*'
                dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
            if p[j - 1] == '*', say if p[j - 2] == x
                dp[i][j] is true if any of the following is true:
                    1) "x*" repeats 0 time and matches empty: f[i][j - 2]
                    2) "x*" repeats >= 1 times, then it should match "x*x": s[i - 1] == x && f[i - 1][j]
            '.' matches any single character
        '''
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for i in xrange(m + 1)]
        dp[0][0] = True

        for j in xrange(2, n + 1):
            dp[0][j] = p[j - 1] == '*' and dp[0][j - 2]

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if p[j - 1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                else:
                    # p[0] cannot be '*'
                    dp[i][j] = dp[i][j-2] or ((s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j])

        return dp[m][n]
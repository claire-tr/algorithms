class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s == "0":
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * (len(s) + 1)
        dp[0] = dp[1] = 1 if s[0] != "0" else 0
        for i in range(2, len(s)+1):
            if int(s[i-1:i]) > 0:
            #01, 02, ..., 09
                dp[i] += dp[i-1]
            if int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]


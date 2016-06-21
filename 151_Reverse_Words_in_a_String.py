class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        words = s.split()
        res = ""
        for i in range(len(words)-1, -1, -1):
            if words[i] != " ":
                res += words[i] + " "
        res = res[:-1]

        return str(res)
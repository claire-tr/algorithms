class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return " ".join(s.strip().split()[::-1])
        if not s:
            return ""
        words = s.strip().split()
        res = ""
        for i in range(len(words)-1, -1, -1):
            if words[i] != " ":
                res += words[i] + " "
        res = res[:-1]

        return str(res)
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or numRows == 1:
            return s
        i = 0
        res = [''] * numRows
        while i < len(s):
            for j in range(numRows):
                if i >= len(s):
                    break
                else:
                    res[j] += s[i]
                    i += 1
            for j in range(numRows-2, 0, -1):
                if i >= len(s):
                    break
                else:
                    res[j] += s[i]
                    i += 1

        for i in range(1, numRows):
            res[0] += res[i]
        return str(res[0])
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack and not needle:
            return 0
        if not haystack:
            return -1
        if not needle:
            return 0
        start, j = -1, 0
        for i in xrange(len(haystack)):
            if haystack[i] == needle[0]:
                start = i
                while j < len(needle) and i+j < len(haystack):
                    if haystack[i + j] != needle[j]:
                        j = 0
                        start = -1
                        break
                    j += 1
                if start != -1 and j == len(needle):
                    return start
                if start != -1 and j < len(needle):
                    return -1
        return start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        '''
            1.
            Two pointers, i scans for haystack and j scans for needle
            Scan haystack from 0 to len(haystack), once meet the leading character of needle,
            two pointers move together to compare if there's a match, if there is, return the start
            index, else, back to the start point and continue looking for the next fit.

            2.
            KMP O(n)
            http://blog.csdn.net/kenden23/article/details/17029625
        '''

        '''
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
        '''

        # Clean Version
        if not haystack and not needle:
            return 0
        if not haystack:
            return -1
        for i in range(len(haystack)):
            for j in range(len(needle)+1):
                if j == len(needle):
                    return i
                if i + j == len(haystack):
                    return -1
                if haystack[i+j] != needle[j]:
                    break
        return -1
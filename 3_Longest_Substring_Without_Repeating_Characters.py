class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Flexible Window Size
        '''
        Use two pointers to define the maximum substring:
            start, the left pointer marks the start of the current substring,
            i, the right pointer, scans through the string.
        Keep a hash map, which stores the characters in the string as keys, and their index as values.

        As the right pointer scan the string, Keep updating the map and max length.
        If the current character is already in the hash map,
        Move the left pointer to max(start, the right of the same character last found).

        '''
        if not s:
            return 0
        start, max_l = 0, 0
        dic = {}
        for i in xrange(len(s)):
            if s[i] in dic:
                start = max(start, dic[s[i]]+1)
            dic[s[i]] = i
            max_l = max(i - start + 1, max_l)
        return max_l

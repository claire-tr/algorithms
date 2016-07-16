class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
            Two pointers, flexible window size
            left pointer, the head, mark the start of the subarray
            right pointer, the i, scan through the array, mark the end of the sub-array
            Keep a hash map, which stores the characters in the string as keys,
                             and how many times they have appear as values.
            while length of the map is greater than 2, it means that there's more than
            two distinct characters in this substring, so from start, move forward the left
            pointer and updating the map, until meet the criteria. Then update the maximum length.

        '''
        if not s:
            return 0
        res, start = 0, 0
        dic = collections.defaultdict(int)

        for i in xrange(len(s)):
            dic[s[i]] += 1
            while len(dic) > 2:
                dic[s[start]] -= 1
                if dic[s[start]] == 0:
                    dic.pop(s[start])
                start += 1
            res = max(res, i - start + 1)
        return res
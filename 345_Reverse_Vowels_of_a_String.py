class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Two pointers
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        start, end = 0, len(s)-1
        res = list(s)
        while start < end:
            while start < end and s[start] not in vowels:
                start += 1
            while start < end and s[end] not in vowels:
                end -= 1
            res[start], res[end] = res[end], res[start]
            start += 1
            end -= 1
        return ''.join(res)
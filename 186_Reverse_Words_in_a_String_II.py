class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        if " " not in s:
            return
        # Reverse the whole sentence
        self.reverse(s, 0, len(s)-1)
        # Reverse each word
        start = 0
        for i in range(len(s)):
            if s[i] == " ":
                self.reverse(s, start, i-1)
                start = i+1
        self.reverse(s, start, len(s)-1)

    def reverse(self, s, l, r):
        while l >= 0 and len(s) > r > l:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

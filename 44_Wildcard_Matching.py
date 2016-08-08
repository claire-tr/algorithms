class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Greedy: http://www.cnblogs.com/yuzhangcmu/p/4116153.html
        # j: the next pattern should be satisfied
        # if j meets an '*', record the current position and move forward, if next i == j+1, then go step 1
        # if next i != j +1, means the previous '*' needs to cover this i, update and go forward
        # if one of the step not match, and not *, then go back to the previous '*', match one more char, go forward
        i, j, star, match = 0, 0, -1, 0
        while i < len(s):
            if j < len(p) and (p[j] == '?' or s[i] == p[j]):
                i, j = i + 1, j + 1
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1
            elif star != -1:
                j = star + 1
                match += 1
                i = match
            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)
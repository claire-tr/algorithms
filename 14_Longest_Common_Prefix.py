class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        sh = strs[0]
        for s in strs:
            sh = s if len(s)<len(sh) else sh
        res = ""
        for i in range(len(sh)):
            for s in strs:
                if s[i] != sh[i]:
                    return res
            res += sh[i]
        return res
    
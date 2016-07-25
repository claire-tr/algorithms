class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = ['69', '96', '88', '00', '11']
        i, j = 0, len(num)-1
        while i <= j:
            if str(num[i] + num[j]) not in dic:
                return False
            i += 1
            j -= 1
        return True
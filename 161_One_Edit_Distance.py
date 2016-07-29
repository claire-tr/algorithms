class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''
          There're 3 possibilities to satisfy one edit distance apart:

          1) Replace 1 char:
         	  s: a B c
         	  t: a D c
          2) Delete 1 char from s:
        	  s: a D  b c
        	  t: a    b c
          3) Delete 1 char from t
        	  s: a   b c
        	  t: a D b c
        '''
        # Scan both two strings, once meet a difference, it means that this should be the only one
        # difference between the two strings, which means rest of the two strings are completely
        # the same.
        for i in xrange(min(len(s), len(t))):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                elif len(s) < len(t):
                    return s[i:] == t[i+1:]
                else:
                    return s[i+1:] == t[i:]
        return abs(len(s) - len(t)) == 1

import collections
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        # To identify each group, compute the modulo 26 difference
        # between each letter in a word with the first letter in it.
        # map() tutorial: http://my.oschina.net/zyzzy/blog/115096
        groups = collections.defaultdict(list)
        for s in strings:
            key = tuple((ord(c) - ord(s[0])) % 26 for c in s)
            groups[key].append(s)

        return map(sorted, groups.values())
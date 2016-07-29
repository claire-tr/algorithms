class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # Similar with minimum window substring
        import collections
        dic_words = collections.Counter(words)
        res = []
        x = len(words[0])

        for step in range(x):
            # Three possible starting point
            dic_s = collections.defaultdict(int)
            count = 0
            head = step

            for i in xrange(step, len(s) - x + 1, x):
                # jump x steps at each round
                cur = s[i:i+x]
                if cur in dic_words:
                    count += 1
                    dic_s[cur] += 1
                    while dic_s[cur] > dic_words[cur]:
                        dic_s[s[head:head + x]] -= 1
                        count -= 1
                        head += x
                    if len(words) == count:
                        res.append(head)
                else:
                    dic_s = collections.defaultdict(int)
                    count = 0
                    head = i + x
        return res



class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p1 = [i for i in range(len(words)) if words[i] == word1]
        print p1
        if word1 == word2:
            dist = len(words)
            for i in p1:
                for j in p1:
                    if i != j:
                        dist = min(dist, abs(i-j))
            return dist
        p2 = [i for i in range(len(words)) if words[i] == word2]
        return min([abs(i - j) for i in p1 for j in p2])
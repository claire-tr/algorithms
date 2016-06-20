class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p1 = [i for i in range(len(words)) if words[i] == word1]
        p2 = [i for i in range(len(words)) if words[i] == word2]

        return min([abs(i - j) for i in p1 for j in p2])
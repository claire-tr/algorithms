class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.adict = collections.defaultdict(set)
        for s in dictionary:
            val = s
            if len(s) > 2:
                s = s[0] + str(len(s)-2) + s[-1]
            self.adict[s].add(val)


    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        val = word
        if len(word) > 2:
            word = word[0]+str(len(word)-2)+word[-1]
        # https://leetcode.com/discuss/61561/python-short-solution-using-defaultdict-with-comments
        # if word abbreviation not in the dictionary, or word itself in the dictionary (word itself may
        # appear multiple times in the dictionary, so it's better using set instead of list)
        return len(self.adict[word]) == 0 or (len(self.adict[word]) == 1 and val == list(self.adict[word])[0])


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
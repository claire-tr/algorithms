class TrieNode(object):
    def __init__(self):
        self.isWord = False
        self.children = {}


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find(word, self.root)

    def find(self, word, node):
        if not word:
            return node.isWord
        if word[0] == '.':
            for key, child in node.children.iteritems():
                if self.find(word[1:], child):
                    return True
        else:
            node = node.children.get(word[0])
            if node:
                return self.find(word[1:], node)

        return False




# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
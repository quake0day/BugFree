class TrieNode(object):
    def __init__(self):
        self.childs = {}
        self.isWord = False
        
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
            if not node.childs.get(c):
                node.childs[c] = TrieNode()
            node = node.childs[c]
        node.isWord = True
                

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        q = [[self.root, word]]
        while q:
            node, w = q.pop()
            if len(w) == 0:
                if node.isWord == True:
                    return True
            elif w[0] == ".":
                for key, val in node.childs.iteritems():
                    q.append([val, w[1:]])
            elif w[0] != ".":
                if w[0] in node.childs:
                    q.append([node.childs.get(w[0]), w[1:]])
        return False
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
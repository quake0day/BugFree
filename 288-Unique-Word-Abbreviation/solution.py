import collections
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.h = collections.defaultdict(set)
        for d in dictionary:
            self.h[self.getAbbr(d)].add(d)
    
    def getAbbr(self, word):
        if len(word) <= 2:
            return word
        else:
            return word[0]+str(len(word[1:-1]))+word[-1]

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        w = self.getAbbr(word)
        if w in self.h and (len(self.h[w]) > 1 or (len(self.h[w]) == 1 and word not in self.h[w])):
            return False
        return True


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
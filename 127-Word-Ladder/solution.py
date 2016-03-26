import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        n = len(beginWord)
        worddic = [chr(ord('a')+i) for i in xrange(26)]
        q = collections.deque()
        q.append([beginWord,1])
        while q:
            w, t = q.popleft()
            if w in wordList:
                wordList.remove(w)
            for i in xrange(n):
                for c in worddic:
                    nw = w[:i] + c + w[i+1:]
                    if nw == endWord:
                        return t + 1
                    if nw in wordList:     
                        q.append([nw,t+1])
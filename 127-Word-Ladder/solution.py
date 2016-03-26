import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        t = 0
        n = len(beginWord)
        worddic = [chr(ord('a')+i) for i in xrange(26)]
        q = collections.deque()
        q.append([beginWord,0])
        while q:
            w, t = q.popleft()
            for i in xrange(n):
                for c in worddic:
                    if w == endWord:
                        return t
                    nw = w[:i] + c + w[i+1:]
                    if nw in wordList:
                        wordList.remove(nw)
                        q.append([nw,t+1])
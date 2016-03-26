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
        visited = set()
        while q:
            w, t = q.popleft()
            if w == endWord:
                return t
            for c in worddic:
                for i in xrange(n):
                    nw = w[:i] + c + w[i+1:]
                    if nw not in visited and nw in wordList:     
                        q.append([nw,t+1])
                        visited.add(nw)
        return 0
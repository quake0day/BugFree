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
        worddic = (chr(ord('a')+i) for i in xrange(26))
        def dfs(beginWord, endWord, wordList, t, res):
            for i in xrange(n):
                for c in worddic:
                    beginWord = beginWord[:i] + c + beginWord[i+1:]
                    if beginWord == endWord:
                        res.append(t)
                        return
                    elif beginWord in wordList:
                        t += 1
                        dfs(beginWord, endWord, wordList, t, res)
        res = []
        dfs(beginWord, endWord, wordList, t, res)
        return min(res)
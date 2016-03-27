class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        cl = [chr(ord('a') + i) for i in xrange(26)]
        wordlist.add(endWord)
        l = {beginWord}
        p = collections.defaultdict(set)
        n = len(beginWord)
        while l and endWord not in p:
            nxt = collections.defaultdict(set)
            for w in l:
                for c in cl:
                    for i in xrange(n):
                        tmp = w[:i] + c + w[i+1:]
                        if tmp in wordlist and tmp not in p:
                            nxt[tmp].add(w)
            l = nxt
            p.update(nxt)
        
        # backtracking
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[pp] + r for r in res for pp in p[r[0]]]
        return res
                    
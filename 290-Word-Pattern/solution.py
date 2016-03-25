class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        pattern = list(pattern)
        s = str.split(" ")
        if len(pattern) != len(s):
            return False
        res = zip(pattern, s)
        h = {}
        for a,b in res:
            if a in h and b != h[a]:
                return False
            h[a] = b
        return len(set(h.values())) == len(h.values())
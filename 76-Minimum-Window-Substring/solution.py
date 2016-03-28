import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s == None:
            return ""
        map_t = collections.Counter(t)
        #map_q = {key:0 for key in map_t.keys()}
        cnt = 0
        minL = len(s) + 1
        start = len(s) + 1
        l, r = 0, 0
        for r in xrange(len(s)):
            if s[r] in map_t:
                map_t[s[r]] -= 1
                if map_t[s[r]] >= 0:
                    cnt += 1
            while cnt == len(t):
                if r-l+1 < minL:
                    start =  l
                    minL = r-l+1
                
                if s[l] in map_t:
                    map_t[s[l]] += 1
                    if map_t[s[l]] > 0:
                        cnt -= 1
                l += 1
            

        return s[start:start+minL] 
                
                
                
            
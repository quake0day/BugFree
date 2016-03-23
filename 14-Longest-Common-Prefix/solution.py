class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        mL = min(map(len, strs)) if strs else 0
        for j in xrange(mL):
            for i in xrange(1, len(strs)):
                if strs[i][j] != strs[0][j]:
                    return strs[0][:j]
        return strs[0][:mL] if mL else "" 
        
            
        
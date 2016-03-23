class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        mL = min(map(len, strs)) if strs else 0
        for i in range(mL):
            for j in xrange(1, len(strs)):
                if strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0][:mL] if mL else ""

        
            
        
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        s = list(s)
        vo = set(list("aeiouAEIOU"))
        i, j = 0, n - 1
        while i < j:
            if s[i] in vo and s[j] in vo:
                s[i], s[j] = s[j], s[i]
                i, j = i+1, j-1
            elif s[i] in vo:
                j -= 1
            elif s[j] in vo:
                i += 1
            else:
                i, j = i + 1, j - 1
        return "".join(s)
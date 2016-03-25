class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        h = {}
        for s in strings:
            d = ord(s[0]) - ord('a')
            key = tuple((ord(ch) - d) % 26 for ch in s)
            h[key] = h[key] + [s] if key in h else [s]

        return map(sorted, h.values())
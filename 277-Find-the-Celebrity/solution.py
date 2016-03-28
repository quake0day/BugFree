# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        for i in xrange(n):
            if not knows(i, c):
                c = i
        for k in xrange(n):
            if k != c and find(c,k):
                return -1
        return c
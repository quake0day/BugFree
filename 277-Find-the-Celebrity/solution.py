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
            if knows(c, i):
                c = i
        if any(knows(c, i) for i in xrange(c)):
            return -1
        if any(not knows(i,c) for i in xrange(n)):
            return -1
        return c
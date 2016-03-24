class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        for i in xrange(2, n):
            if isPrime[i] == True:
                for j in xrange(2, (n-1)//i+1):
                    isPrime[i*j] = False
        return sum(isPrime)
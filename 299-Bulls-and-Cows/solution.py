class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        e_secret = list(enumerate(list(secret)))
        h = {k:0 for k in e_secret}
        e_guess = list(enumerate(list(guess)))
        processed = []
        A = 0
        for t in e_guess:
            if t in h:
                A += 1
                del h[t]
                processed.append(t)
        for item in processed:
            e_guess.remove(item)
        m = {}
        for pos, val in h.keys():
            m[val] = m[val] + 1 if val in m else 1
        B = 0
        for t in e_guess:
             if t[1] in m:
                B += 1
                m[t[1]] -= 1
                if m[t[1]] == 0:
                    del m[t[1]]
        return str(A)+"A"+str(B)+"B"
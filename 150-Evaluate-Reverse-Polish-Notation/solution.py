import math
class Solution(object):
    def evalRPN(self,tokens):
        stack = []
        for t in tokens:
            if t.isdigit() or (t[0] == "-" and t[1:].isdigit()):
                stack.append(int(t))
            else:
                b, a = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(a+b)
                elif t == "-":
                    stack.append(a-b)
                elif t == "*":
                    stack.append(a*b)
                elif t == "/":
                    # handle the case of 1/-100, in python it returns -1, should return 0
                    if a*b < 0 and a%b != 0:
                        stack.append(a/b+1)
                    else:
                        stack.append(a/b)
        return stack.pop()
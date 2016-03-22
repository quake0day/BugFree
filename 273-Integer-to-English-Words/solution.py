class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
    
        dic1 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        dic4 = ["", "Thousand", "Million", "Billion"]
    
        seg,res = [],[]
        while num > 0:
            seg.append(str(num%1000))
            num = num//1000
        for i in range(len(seg)):
            if i > 0 and seg[i] > "0":
                res = [dic4[i]] + res
            res = self.read3dig(seg[i]) + res
        return " ".join(res)
    
    def read3dig(self, num3):
        dic1 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        dic10 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        dic2 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        res = []
    
        if len(num3) > 2:
            res += [dic1[int(num3[-3])]]
            res += ["Hundred"]
    
        if len(num3) > 1:
            if num3[-2] > "1":
                res += [dic2[int(num3[-2])]]
            elif num3[-2] == "1":
                res += [dic10[int(num3[-1])]]
                return res
        if dic1[int(num3[-1])]:
            res += [dic1[int(num3[-1])]]
        return res
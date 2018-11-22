class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        total = 0
        for i, item in enumerate(s):
            cur = dic[item]
            try:
                nxt = dic[s[i + 1]]
            except:
                total += cur
            else:
                if nxt > dic[item]:
                    total -= cur
                else:
                    total += cur
        return total
        
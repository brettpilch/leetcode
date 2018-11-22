class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = ['' for i in range(numRows)]
        dire = 1
        i = 0
        r = 0
        lens = len(s)
        while i < lens:
            rows[r] += s[i]
            i += 1
            r += dire
            if r in [0, numRows - 1]:
                dire = -dire
        return ''.join(rows)
            
        
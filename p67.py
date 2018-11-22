class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        long = max(len(a), len(b))
        carry = 0
        out = ''
        for i in range(long):
            try:
                achar = int(a[-1 - i])
            except:
                achar = 0
            try:
                bchar = int(b[-1 - i])
            except:
                bchar = 0
            plus = achar + bchar + carry
            if plus < 2:
                out += str(plus)
                carry = 0
            else:
                out += str(plus % 2)
                carry = 1
        if carry:
            out += '1'
        return out[::-1]
                
            
        
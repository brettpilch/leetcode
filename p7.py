class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        strx = str(x)
        if strx[0] == '-':
            output = int(strx[0] + strx[-1:0:-1])
        else:
            output = int(strx[::-1])
        if output < -(2**31) or output > 2**31 - 1:
            return 0
        return output
        
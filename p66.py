class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        def plusit(digits):
            if digits == [9]:
                return [1, 0]
            last = digits[-1] + 1
            if last < 10:
                digits[-1] = last
                return digits
            else:
                return plusit(digits[:-1]) + [0]
        return plusit(digits)
        
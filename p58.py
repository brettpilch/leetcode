class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for char in reversed(s):
            if char == ' ':
                if length > 0:
                    return length
            else:
                length += 1
        return length
        
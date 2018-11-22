class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length = len(needle)
        if length < 1:
            return 0
        for c, char in enumerate(haystack):
            if haystack[c:c + length] == needle:
                return c
        return -1
        
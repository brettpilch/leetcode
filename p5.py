from functools import lru_cache

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        @lru_cache(128)
        def is_palindrome(i, j):
            if j - i < 2:
                return True
            if s[i] == s[j]:
                return is_palindrome(i + 1, j - 1)
            return False
        
        longest = ''
        size = 0
        for i in range(len(s)):
            if len(s) - i <= size:
                break
            for j in range(len(s) - 1, i, -1):
                if j - i > len(longest) and is_palindrome(i, j):
                    longest = s[i:j]
                    size = len(longest)
                else:
                    break
        return longest
        


import random
from string import ascii_lowercase

s = ''.join([random.choice(ascii_lowercase) for i in range(1000)])
# s = 'a' * 1000
print(s)
sol = Solution()
print(sol.longestPalindrome(s))

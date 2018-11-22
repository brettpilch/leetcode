class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        long = 0
        lens = len(s)
        for i in range(lens):
            for j in range(i + 1 + long, lens + 1):
                this_str = s[i:j]
                this_set = set(this_str)
                len_this_str = len(this_str)
                if len_this_str == len(this_set):
                    long = len_this_str
                else:
                    break
        return long
        
a = Solution()
print(a.lengthOfLongestSubstring(" "))

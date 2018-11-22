class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opens = []
        match = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in match:
                try:
                    last = opens.pop()
                except:
                    return False
                else:
                    if match[char] != last:
                        return False
            else:
                opens.append(char)
        return len(opens) == 0
                
                
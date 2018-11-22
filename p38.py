class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ['1', '11']
        while len(result) < n:
            word = result[-1]
            match = word[0]
            count = 1
            new_word = ''
            for char in word[1:]:
                if char == match:
                    count += 1
                else:
                    new_word += str(count) + match
                    match = char
                    count = 1
            new_word += str(count) + match
            result.append(new_word)
        return result[n - 1]
            
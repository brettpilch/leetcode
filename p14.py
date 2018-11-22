class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        i = 0
        while True:
            try:
                letter = [string[i] for string in strs]
            except:
                break
            else:
                if len(set(letter)) == 1:
                    result += letter[0]
                    i += 1
                else:
                    break
        return result
        
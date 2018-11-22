class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums) - 1:
            cur = nums[i]
            try:
                nxt = nums[i + 1]
            except:
                break
            else:
                if cur == nxt:
                    nums.remove(cur)
                else:
                    i += 1
        return len(nums)
        
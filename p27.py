class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cnt = nums.count(val)
        for i in range(cnt):
            nums.remove(val)
        return len(nums)
        
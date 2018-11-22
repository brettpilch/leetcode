class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def searchit(start, nums, target):
            length = len(nums)
            if length == 0:
                return start
            if length == 1:
                if target <= nums[0]:
                    return start
                else:
                    return start + 1
            mid = length // 2
            if nums[mid] == target:
                return start + mid
            elif target < nums[mid]:
                return searchit(start, nums[:mid], target)
            else:
                return searchit(start + mid, nums[mid:], target)
        
        return searchit(0, nums, target)
        
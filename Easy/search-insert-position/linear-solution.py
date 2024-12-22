class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lastPosition = len(nums)
        for i in range(0,lastPosition):
            if nums[i] >= target:
                return i
        return lastPosition

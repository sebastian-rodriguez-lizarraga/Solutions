class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap_nums = {}
        for i in range(0,len(nums)):
            hashmap_nums[nums[i]] = i
        for j in range(len(nums)-1,-1,-1):
            complement = target-nums[j] 
            if complement in hashmap_nums and hashmap_nums[complement] != j:
                return [j, hashmap_nums[complement]]

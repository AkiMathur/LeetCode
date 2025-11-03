class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sol = dict()

        for i in range(len(nums)):
            if target - nums[i] in sol:
                return [sol[target - nums[i]],i]
            sol[nums[i]] = i
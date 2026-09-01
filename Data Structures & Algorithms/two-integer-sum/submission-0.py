class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}

        for i , num in enumerate(nums):
            complement = target - num
            if complement in previous:
                return [previous[complement] , i]
            previous[num] = i
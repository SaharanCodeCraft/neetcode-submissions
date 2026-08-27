class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        def quickselect(left,right):
            pivot = nums[right]
            p = left
            for i in range(left,right):
                if  nums[i] <= nums[right]:
                    nums[p], nums[i] = nums[i], nums[p]
                    p+= 1
            nums[p], nums[right] = nums[right], nums[p]
            if p ==target:
                return nums[p]
            elif target < p:
                return quickselect(left, p-1)
            else:
                return quickselect(p+1, right)
        return quickselect(0, len(nums)-1)
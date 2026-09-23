class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        total = 0
        min_count = len(nums) + 1
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_count = min(right - left + 1, min_count)
                total -= nums[left]
                left += 1
        if min_count == len(nums) + 1:
            return 0
        return min_count
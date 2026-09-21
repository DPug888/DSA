class Solution:
    def twoSum(self, nums, target):
        freq = {}
        for i in range(len(nums)):
            com = target - nums[i]
            if com in freq:
                return [freq[com], i]
            freq[nums[i]] = i
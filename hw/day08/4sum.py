class Solution:
    def fourSum(self, nums, target):
        result = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            arr = sorted([nums[i], nums[j], nums[k], nums[l]])
                            if arr not in result:
                                result.append(arr)
        return result
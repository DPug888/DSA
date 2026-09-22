class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)
        sums = [0]
        for i in range(n):
            sums.append(sums[i] + arr[i])
        max_sum = sums[k]
        for i in range(1, n-k+1):
            curr_sum = sums[i+k] - sums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum
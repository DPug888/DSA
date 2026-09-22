class Solution:
    def prefixAvg(self, arr):
        ans = []
        total = 0
        for i in range(len(arr)):
            total += arr[i]
            avg = total//(i+1)
            ans.append(avg)
        return ans
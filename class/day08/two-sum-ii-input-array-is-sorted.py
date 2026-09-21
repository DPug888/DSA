class Solution(object):
    def twoSum(self, numbers, target):
        l = numbers[0]
        r = numbers[-1]
        for i in range(len(numbers)):
            for j in range(len(numbers)-1):
                if l+r == target:
                    return (i,j)
                elif l+r > target:
                    r-=1
                elif l+r < target:
                    l+=1
class Solution(object):
    def diagonalSum(self, mat):
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i]
            total += mat[i][n - 1 - i]
        if n % 2 == 1:
            total -= mat[n // 2][n // 2]
        return total

#         # cook your dish here
# arr = list(map(int, input().split()))
# target = int(input())
# num1= arr[0]
# num2=arr[-1]
# new = []arr = list(map(int, input().split()))
# target = int(input())
# num1= arr[0]
# num2=arr[-1]
# new = []
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if num1 + num2 == target:
#             new.append(num1)
#             new.append(num2)
#             print(new)
#         num1 = arr[i+1]
#         num2 = arr[j-1]
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if num1 + num2 == target:
#             new.append(num1)
#             new.append(num2)
#             print(new)
#         num1 = arr[i+1]
#         num2 = arr[j-1]
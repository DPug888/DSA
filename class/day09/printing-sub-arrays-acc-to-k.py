arr = list(map(int, input().split()))
k = int(input())
n=len(arr)
for i in range(n-k+1):
  for j in range(i,i+k):
    print(arr[j], end=' ')
  print()
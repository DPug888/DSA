# cook your dish here
n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        print(f"{arr[i]}, {arr[j]}")
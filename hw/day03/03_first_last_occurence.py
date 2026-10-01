# cook your dish here
n, target = map(int, input().split())
arr = list(map(int, input().split()))
first_pos = -1
last_pos = -1

for i in range(n):
    if arr[i] == target:
        if first_pos == -1:
            first_pos = i
        last_pos = i

print(first_pos, last_pos)
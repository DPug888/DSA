# cook your dish here
n , c = map(int, input().split())
scores = list(map(int, input().split()))
count = 0
for i in range(n):
    if scores[i] >= c:
        count += 1
print(count)
# cook your dish here
n = int(input())
arr = list(map(int, input().split()))
print("Scores")
for i in range(n):
    print(arr[i], end=" ")
    if (i + 1) % 4 == 0:
        print()

print()
total = 0
for i in range(n):
    total = total + arr[i]

average = total / n
print(f"Average: {average:.2f}")

lowest = min(arr)
highest = max(arr)

print()
print("Score Deviation")
for i in range(n):
    deviation = arr[i] - average
    print(f"{arr[i]} {deviation:.2f}")

total = 0
for i in range(n):
    total = total + (arr[i] - average) ** 2

sd = (total / n) ** 0.5
print()
print(f"Standard Deviation: {sd:.2f}")

count = 0
for i in range(n):
    if average - sd <= arr[i] <= average + sd:
        count += 1

print("Scores within one standard deviation: ", count)
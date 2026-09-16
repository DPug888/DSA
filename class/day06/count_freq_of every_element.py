arr = [10, 20, 10, 30, 20, 10]
frequency = {}
for x in arr:
    frequency[x] = frequency.get(x, 0) + 1
print(frequency)
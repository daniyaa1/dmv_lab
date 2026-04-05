n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    val = int(input("Enter element (-1 for missing): "))
    arr.append(val)

# Calculate mean of available values
sum_val = 0
count = 0

for i in arr:
    if i != -1:
        sum_val += i
        count += 1

mean = sum_val / count

# Replace missing values
for i in range(len(arr)):
    if arr[i] == -1:
        arr[i] = mean

print("Array after handling missing values:")
print(arr)

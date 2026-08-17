# Day 10 - Find Second Largest Number

numbers = [10, 25, 8, 40, 15, 30]

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Largest number:", largest)
print("Second largest number:", second_largest)

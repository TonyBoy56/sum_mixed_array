# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.

mixed_array = ['5', '0', 9, 3, 2, 1, '9', 6, 7]

def sum_mix(arr):
    for i in range(len(arr)):
        print(arr[i])
sum_mix(mixed_array)
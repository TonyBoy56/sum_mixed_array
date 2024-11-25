# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.

mixed_array = ['5', '0', 9, 3, 2, 1, '9', 6, 7]
# mixed_array = ['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']
# mixed_array = ['1', '5', '8', 8, 9, 9, 2, '3']

def sum_mix(arr):
    int_array = [int(item) for item in arr]
    result = 0
    i = 0
    while result <= len(int_array):
        for i in range(len(int_array)):
            result += int_array[i]
            print(f"Current index of [i]: {int_array[i]}")
        print(result)
        
sum_mix(mixed_array)
def count_frequency(arr):

    frequency = {}  # Initialize an empty dictionary
    for element in arr:
        if element in frequency:
            frequency[element] += 1  # Increment count if element exists
        else:
            frequency[element] = 1   # Add element with count 1 if it's new
    return frequency

# Example usage:
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
result = count_frequency(my_list)
print(result)  # Output: {1: 1, 2: 2, 3: 3, 4: 4}


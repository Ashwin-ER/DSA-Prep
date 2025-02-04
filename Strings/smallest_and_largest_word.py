def find_smallest_and_largest_word(s):
    words = s.split()
    smallest_word = largest_word = words[0]
    for word in words:
        if len(word) < len(smallest_word):
            smallest_word = word
        if len(word) > len(largest_word):
            largest_word = word

    return smallest_word, largest_word

input_string = "This is a simple test string to find smallest and largest word"

smallest, largest = find_smallest_and_largest_word(input_string)


print("Smallest Word:", smallest)
print("Largest Word:", largest)

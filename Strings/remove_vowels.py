def remove_vowels(string):
    result = ''
    vowels = 'aeiouAEIOU'
    for char in string:
        if char not in vowels:
            result += char
    return result


print(remove_vowels("Hello World"))

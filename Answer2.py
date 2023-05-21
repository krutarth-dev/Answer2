def is_valid_string(s):
    # Counting the frequency of each character
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    # Counting the frequencies of the frequencies
    freq_count = {}
    for freq in frequency.values():
        freq_count[freq] = freq_count.get(freq, 0) + 1

    # If all characters have the same frequency, it's valid
    if len(freq_count) == 1:
        return "YES"

    # If there are exactly two frequencies and one occurs only once,
    # removing one character with that frequency makes it valid
    if len(freq_count) == 2:
        if freq_count.get(1) == 1 or (1 in freq_count and freq_count[1] == 1):
            return "YES"

    return "NO"

# Testing
s = "abc"
print(is_valid_string(s))
#Explanation
# Output: YES (All characters appear the same number of times: {'a': 1, 'b': 1, 'c': 1})

# Additional Test Case 1
s = "abcc"
print(is_valid_string(s))
#Explanation
# Output: NO (Removing one occurrence of 'c' would leave different frequencies: {'a': 1, 'b': 1, 'c': 2})

# Additional Test Case 2
s = "aabbccdd"
print(is_valid_string(s))
#Explanation
# Output: YES (All characters appear the same number of times: {'a': 2, 'b': 2, 'c': 2, 'd': 2})

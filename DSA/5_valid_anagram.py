def is_valid_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    char_count = {}

    # Count the frequency of characters in s1
    for char in s1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Decrement the count of characters in s2
    for char in s2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False

    # All counts should be zero if s1 and s2 are anagrams
    for count in char_count.values():
        if count != 0:
            return False

    return True


# Test the function
print(is_valid_anagram("listen", "silent"))  # Output: True
print(is_valid_anagram("hello", "ollhe"))  # Output: True
print(is_valid_anagram("python", "java"))  # Output: False

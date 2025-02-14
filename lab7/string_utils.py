def reverse_string(s):
    """returns the reverse"""
    return s[::-1]
def count_vowels(s):
    vowels="aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
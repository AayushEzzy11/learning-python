# Function to get unique words from a sentence
def unique_words(sentence):
    words = sentence.split()  # Split the sentence into words
    return set(words)         # Return a set of unique words

# Input from the user
user_sentence = input("Enter a sentence: ")

# Create a set of unique words from the user's sentence
user_words_set = unique_words(user_sentence)

# Define another set of words for demonstration
other_words_set = {'apple', 'banana', 'cherry', 'banana'}

# Print the sets
print("Unique words from your sentence:", user_words_set)
print("Another set of words:", other_words_set)

# Union operation
union_set = user_words_set.union(other_words_set)
print("Union of both sets:", union_set)

# Intersection operation
intersection_set = user_words_set.intersection(other_words_set)
print("Intersection of both sets:", intersection_set)

# Difference operation
difference_set = user_words_set.difference(other_words_set)
print("Difference (user words - other words):", difference_set)
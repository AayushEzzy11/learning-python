# Given string
input_string = "hello world hello everyone this is a test hello world"

# Initialize an empty dictionary to store word counts
word_count = {}

# Split the string into words
words = input_string.split()

# Count the occurrences of each word
for word in words:
    # Normalize the word to lowercase (optional, if you want case insensitivity)
    word = word.lower()
    # Update the count in the dictionary
    if word in word_count:
        word_count[word] += 1  # Increment the count if the word is already in the dictionary
    else:
        word_count[word] = 1  # Initialize the count for new words

# Display the word counts
print("Word occurrences:")
for word, count in word_count.items():
    print(f"'{word}': {count}")
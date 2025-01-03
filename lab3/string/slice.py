#string input from user
text = input("Enter a string: ")

#Get string length
length = len(text)

#Find first, middle and last characters
first_char = text[0]
middle_char = text[length//2]
last_char = text[-1]

#Print characters
print("\nCharacters:")
print(f"First character: {first_char}")
print(f"Middle character: {middle_char}")
print(f"Last character: {last_char}")

#Display every second character
print("\nEvery second character:", text[::2])

word_to_replace ="sample"
replacement_word="example"

with open("sample.txt","r") as file:
    text=file.read()

text=text.replace(word_to_replace,replacement_word)

with open("sample.txt","w") as file:
    file.write(text)

print(f"Replaced '{word_to_replace}' with '{replacement_word}' successfully")
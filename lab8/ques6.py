word_to_find="sample"
with open("sample.txt","r") as file:
    text=file.read()
    count=text.lower().split().count(word_to_find.lower())
    print(f"The word '{word_to_find}' appears {count} times in file")

with open("sample.txt","r") as file:
    words=file.read().split()
    print("Number of words :",len(words))
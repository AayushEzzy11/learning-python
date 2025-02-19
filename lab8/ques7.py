with open("sample.txt","r") as file:
    lines=file.readlines()

with open("sample.txt","w") as file:
    for line in lines:
        if line.strip():
            file.write(line)
print("Blank lines removed successfully")
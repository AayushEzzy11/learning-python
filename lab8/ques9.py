filename = "youtube_data.txt"

def display_videos():
    with open(filename,"r") as file:
        content=file.read()
        print("Youtube Videos :")
        print(content if content else "No Videos available")

def add_video(title):
    with open(filename,"a") as file:
        file.write(title + "\n")
    print(f"Video '{title}' added")

def update_videos(old_title,new_title):
    with open(filename,"r") as file:
        lines=file.readlines()
    with open(filename,"w") as file:
        for line in lines:
            file.write(new_title + "\n" if line.strip()==old_title else line)
        print(f"Updated '{old_title}' to '{new_title}'")

def delete_videos(title):
    with open(filename,"r") as file:
        lines=file.readlines()
    with open(filename,"w") as file:
        for line in lines:
            if line.strip() != title:
                file.write(line)
    print(f"Delected video: '{title}'")            

add_video("Python Tutorial")
add_video("Django Tutorial")
display_videos()
update_videos("Django Basics","Django Advanced")
delete_videos("Python Tutorial")
display_videos()
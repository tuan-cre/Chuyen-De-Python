
link = r"d:\\music\muabui.mp3"

def get_filename(link):
    return link.split("\\")[-1]

def get_filename2(link):
    return link.split("\\")[-1].split(".")[0]

print(get_filename(link))
print(get_filename2(link))
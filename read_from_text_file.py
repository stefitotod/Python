# Намерете и принтирайте най-дългата дума в текстов файл.

with open("about.txt", "r") as fp:      # about.txt- текстов файл с думи 
    words = fp.read().split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
print(longest)

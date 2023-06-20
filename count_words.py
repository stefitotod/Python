# Да се намерят броят на срещане на всяка една дума от текстов файл.

with open("words.txt", "r") as f:
    words = f.read().split()
    for word in set(words):
        print(f"{word}-{words.count(word)}")

enter=input("enter sentence: ")
print(enter)
words = enter.split()
print(words)
reverse_words=[word[::-1] for word in words]
print(reverse_words)
reverse_enter=" ".join(reverse_words).capitalize()
print(reverse_enter)
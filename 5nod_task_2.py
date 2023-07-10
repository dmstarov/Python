text_1 = input("Enter your text!")
buffer ="*"*len(text_1)
print(buffer)

text_2 = input("Enter your guess!")
print(text_2)

for character in text_1:
    if character == text_2:
        print(character)

       # text_3 = text_2
       # buffer += text_1
    else:
        print("try again")
       # buffer += text_1
#print(buffer) 
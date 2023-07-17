secret = input("Enter word: ")
print(secret)
secret_show=""

for n in secret:
    if n== " ":
        secret_show += " "
    else:
        secret_show += "*"
print(secret_show)
print(secret)

imput_letter = input("Enter gues: ")
print(imput_letter)
result = ""

for n in secret:
    if n == imput_letter:
        result += n
        print(result)
    elif n== " ":
        result += " "
    else:
        result += "*"
    
print(result)

# print(hidden_text)
 
# hidden_text2 = ""
 
# print("Enter a letter")
 
# input_letter = input()

# for letter in some_text:
#     if letter == input_letter:
#         hidden_text2 += letter # same as hidden_text2 = hidden_text2 + letter
#     elif letter == " ":
#         hidden_text2 += space # same as hidden_text2 = hidden_text2 + space
#     else:
#         hidden_text2 += star # same as hidden_text2 = hidden_text2 + star
 
# print(hidden_text2)
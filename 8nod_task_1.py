
def get_char_count(text):
    
    result = {}
    for letters in text:
        if letters in result:
            result[letters] +=1
        else:
            result[letters]=1
    return result

text = input("type here: ")
print(get_char_count(text))
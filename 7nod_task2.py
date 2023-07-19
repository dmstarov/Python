def is_palindrom(text):
    text = text.replace(" ", "").lower()
    new_text= text[::-1]
    print(text)
    print(new_text)
    if text == new_text:
        print("TRUE")
    else:
        print("FALSE")

is_palindrom("Hello not")

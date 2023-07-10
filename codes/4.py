import datetime
name=input("What i syour name?")
age=int(input(f"How old are you, {name}?"))
current_year = datetime.datetime.now().year
age1 = 100 - age
add_age = current_year+age1
print(f"{name} will be 100 years old in {add_age} !")
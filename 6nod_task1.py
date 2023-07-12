start= input("Do you want to play? Y/N  ")
all_entry=[]

while start == "Y":
    new_entry = float(input("Enter integer or float!"))
    all_entry.append(new_entry)
    print(all_entry)
    start= input("Do you want to play? Y/N  ")
    if start == "N":
       print("Buy!")

avg = sum(all_entry) / len(all_entry)
print(avg)




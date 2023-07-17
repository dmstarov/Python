number = int(input("Enter numbers: "))



for n in range(2, int(number **0.5)+1):
    if number%n==0:
        print(f"not {number} delitsja {n} bez ostatsk")
        break
else:
    print(f"{number} simple")




first_n = int(input("Enter 1st number: "))

second_n = int(input("Enter 2st number: "))


numbers = []

numbers += [first_n]
numbers += [second_n]

print(numbers)
numbers = [n**3 for n in range(first_n,second_n+1)]

print(numbers)
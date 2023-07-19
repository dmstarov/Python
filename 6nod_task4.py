number = int(input("Enter number: "))
print(number)
number_l=[]
till = 20
number_last = number + till
print(number_last)
#number_l =[number*2 for n in range(number,number_last)]
while len(number_l) < till:
     number_l.append(number)
     number +=1


#number_l=[number.append(float(1) for n in range(number, number_last)]
print(number_l)
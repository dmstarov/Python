#3nod_1
#
# temp = int(input("your temp?"))
# if temp < 35:
#     print("nav par aukstu?")
# elif temp <= 37:
#     print("viss kartiba!")
# else:
#     print("iespejams draudzis")
    
## 3nod_2

# age= int(input("cik gadu staradajiet?"))
# 
# if age>2:
#     alga = int(input("cik liela alga?"))
#     bonuss_1 = alga * 0.15
#     bonuss_f = age * bonuss_1
#     print(f"jusu bonus = {bonuss_f}")
# else:
#     print("No bonuss")



 # 4nod_1
#for n in range(101):
#     if n%7==0 and n%5 ==0:
#         print("Fizz")
#     elif n%5==0:
#         print("Bizz")
#     elif n%7==0:
#        print("FizzBizz")
#    else:
#        print(n)
        
# 4nod_2
    
height = int(input("Enter height of this stuff x > 0:"))
i = 1
 
while height:
    spaces = height - 1
    print(" " * spaces + "*" * i)
    height -= 1
    i += 2
     










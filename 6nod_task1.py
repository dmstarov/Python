listik=[]
exit = "q"

while True:
    enter= input("Enter float -q to quit: ")
    if enter == exit:
        break
    else:
        listik.append(float(enter))
        #my_list.append(float(num))
        listik.sort()
        print(f"Pirmie 3 ir {listik[-1:-4:-1]} un pedejie ir{listik[0:3]}")
        print(f"videja vērtība: {round(sum(listik) / len(listik),2)} Visi skaitļi:{listik}")


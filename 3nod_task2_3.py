total = 0
i = 0
while i < 10:
    print("oh i is now", i)
    if i % 2 == 0:    
        i += 1    
        total += 1
        continue
     
    else:
        print("ten")
        i += 1 


print(total)
print(i)

# for c in "kartupelis":

#    if c < "i":

 #       print(c, end="")
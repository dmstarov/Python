def add_mult(a,b,c):
    order = sorted([a,b,c])
    return ((order[0]+order[1])*order[2])

print(add_mult(2,4,3))
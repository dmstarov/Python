def get_min_avg_max(sequence):
    min_val, max_val, avg_val = min(sequence), sum(sequence)/len(sequence), max(sequence)
    return min_val, max_val, avg_val
    
    #print(min(sequence), max(sequence), sum(sequence)/ len(sequence))

my_list = [10,-200,30,4, 1000]
print(get_min_avg_max(my_list))
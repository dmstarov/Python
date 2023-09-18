# def clean_dict_value(d, bad_val):
#     d_copy = d.copy()
#     for key,value in d_copy.items():
#         if value == bad_val:
#            if key in d.keys():
#                del d[key]
#     return d

# print(clean_dict_value({'a':5,'b':6,'c':5}, 5)) #-> {'b':6}

def clean_dict_values(d, v_list):
    d_copy = d.copy()
    for k,v in d_copy.items():
        if v in v_list:
            if k in d.keys():
                del d[k]
    return d 

print(clean_dict_values({'a':3,'b':6,'c':5}, [3,4,5]))



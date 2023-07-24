def clean_dict_value(d, bad_val):
    d_copy = d.copy()
    for k,v in d_copy.items():
        if v == bad_val:
            if k in d.keys():
                del d[k]
    return d


print(clean_dict_value({'a':5,'b':6,'c':5}, 5))
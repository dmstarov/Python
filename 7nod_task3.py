def get_city_year(p0,perc,delta,p):
     year_start = 1
     while p0 < p:
        result = (p0 + (p0 * perc*0.01)+ delta) * year_start
        print(result)        
        if result -p0 <= 0:
            return -1
        elif p - result > 0:
            p0 = result
            year_start += 1
        else:
            return year_start
        
            print(f" we need {year_start} years")
print(get_city_year(1000,2,50,1200))


# def get_city_year(p0, percentage, delta, target_pop, debug=False):
#     year_to_target = 1
#     while p0 < target_pop :
#         citizens_next_year = p0 + p0 * percentage * 0.01 + delta 
#         if round(citizens_next_year - p0, 2) <= 0:   
#             return -1
#         elif target_pop - citizens_next_year > 0: 
#             p0 = citizens_next_year
#             year_to_target += 1
#         else:
#             return year_to_target
#         if debug:
#             print(f"Year: {year_to_target}, citizens: {p0}")

# print( get_city_year(1000, 2, 50, 1200))
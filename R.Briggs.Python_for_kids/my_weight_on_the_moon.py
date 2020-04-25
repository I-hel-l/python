my_weight_on_Earth = 70
percent_to_get_moon_weight = 0.165

for year in range(1, 16):
    my_weight_on_Earth += 1
    my_moon_weight = my_weight_on_Earth * percent_to_get_moon_weight
    print("В %s год мой вес будет %.3f кг" % (year, my_moon_weight))

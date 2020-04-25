def get_weight_on_moon(my_weight_on_Earth, weight_gain_step):
    for year in range(1, 16):
        percent_to_get_moon_weight = 0.165
        my_weight_on_Earth = my_weight_on_Earth + weight_gain_step
        my_moon_weight = my_weight_on_Earth * percent_to_get_moon_weight
        print("В %s год мой вес будет %.3f кг" % (year, my_moon_weight))

get_weight_on_moon(70, 0.2)
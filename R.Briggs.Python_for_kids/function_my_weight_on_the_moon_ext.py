import sys

def get_weight_on_moon():
    print('Enter your current earth weight:')
    my_weight_on_Earth = int(sys.stdin.readline())

    print('Enter your annual weight gain:')
    weight_gain_step = float(sys.stdin.readline())

    print('Enter the number of years:')
    years = int(sys.stdin.readline())

    for i in range(0, years):
        percent_to_get_moon_weight = 0.165
        my_weight_on_Earth = my_weight_on_Earth + weight_gain_step
        my_moon_weight = my_weight_on_Earth * percent_to_get_moon_weight
        print("В %s год мой вес будет %.3f кг" % (i, my_moon_weight))

get_weight_on_moon()
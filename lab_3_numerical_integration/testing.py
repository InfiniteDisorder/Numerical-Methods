import math
from numerical_integration import *


def test_numerical_integration(method, a, b, f, expected_value, e, k=2, richardson_extrapolation=False):
    n = 2
    iter_error = abs(method(a, b, f, n) - expected_value)
    print(iter_error, 2)
    last_iter_value = 0
    while iter_error > e:
        n *= 2
        value = method(a, b, f, n)
        if richardson_extrapolation:
            iter_error = abs(value + (value - last_iter_value) / (math.pow(2, k)) - expected_value)
        else:
            iter_error = abs(value - expected_value)

        last_iter_value = value
        print(iter_error, n)


left = 1
right = 15
func = math.log
expected_value_loc = 15 * math.log(15) - 15 - math.log(1) + 1
error_list = [0.1, 0.01, 0.001]

for error in error_list:
    print('error:=', error)
    print('mid_rec')
    test_numerical_integration(mid_rectangle_method, left, right, func, expected_value_loc, error)
    print('trapezium')
    test_numerical_integration(trapezium_method, left, right, func, expected_value_loc, error)
    print('simpson')
    test_numerical_integration(simpson_method, left, right, func, expected_value_loc, error, k=4)
    print('mid_rec + richardson')
    test_numerical_integration(mid_rectangle_method, left, right, func, expected_value_loc, error,
                               richardson_extrapolation=True)
    print('trapezium + richardson')
    test_numerical_integration(trapezium_method, left, right, func, expected_value_loc, error,
                               richardson_extrapolation=True)
    print('simpson + richardson')
    test_numerical_integration(simpson_method, left, right, func, expected_value_loc, error, k=4,
                               richardson_extrapolation=True)



from fuel_consumption import *
from temperature import *

unified_conversion_func_map = {}
unified_conversion_func_map.update(temp_func_map)
unified_conversion_func_map.update(fuel_economy_func_map)

# runs tests
def run_tests():
    print("TESTS:\n")

    temp_test()
    print()

    fc_tests()

# help message
help_message = "-h displays this message\n"
help_message +="t_,c|f|k,c|f|k <value> temperature conversion\n"
help_message +="fc_,us_mpg|l100km,us_mpg|l100km <value> fuel consumption conversion\n"
help_message +="example: python unit_converter.py t_cc -40\n"

# 
unknown_option_error = "ERR: incorrect input -> see help\n"

# need this and the dummy arg to get it to work properly with dicttionary get
def unknown_option_error_string(arg1):
    return unknown_option_error + help_message

if __name__ == "__main__":
    run_tests()
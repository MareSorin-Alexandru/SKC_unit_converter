from sys import argv
from fuel_consumption import *
from temperature import *

# runs tests
def run_tests():
    print("TESTS:\n")

    temp_test()
    print()

    fc_tests()

# help message
help_message = "-h displays this message\n"
help_message +="-t c|f|k,c|f|k <value> temperature conversion\n"
help_message +="-fc us_mpg|l100km,us_mpg|l100km <value> fuel consumption conversion\n"
help_message +="example: python unit_converter.py -t cc -40\n"

# 
unknown_option_error = "ERR: incorrect input -> see help\n"

# need this and the dummy arg to get it to work properly with dicttionary get
def unknown_option_error_string(arg1):
    return unknown_option_error + help_message

def main():

    #run_tests()

    if len(argv)==1:
        print(help_message)
        return
    elif argv[1]=="-h":
        print(help_message)
        return
    elif (len(argv)>=2 and len(argv)<=3) or len(argv)>=5:
        print("ERR: incorect number of arguments -> see help")
        print(help_message)
        
    if argv[1]=="-t":
        print(temp_func_map.get(argv[2],unknown_option_error_string)(float(argv[3])))
        return
    elif argv[1]=="-fc":
        print(fuel_economy_func_map.get(argv[2],unknown_option_error_string)(float(argv[3])))
        return
    else:
        print(unknown_option_error)
        return
    
if __name__ == "__main__":
    main()
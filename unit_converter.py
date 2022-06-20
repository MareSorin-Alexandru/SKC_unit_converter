from sys import argv
from fuel_consumption import *
from temperature import *

# runs tests
def run_tests():
    print("TESTS:\n")

    temp_test()
    print()

    fc_tests()

# prints help message
def print_help():
    print("-h displays this message\n")
    print("-t c|f|k,c|f|k <value> temperature conversion\n")
    print("-fc us_mpg|l100km,us_mpg|l100km <value> fuel consumption conversion\n")
    print("example: python unit_converter.py -t cc -40\n")

def main():

    run_tests()

    if len(argv)==1:
        print_help()
        return
    elif argv[1]=="-h":
        print_help()
        return
    elif (len(argv)>=2 and len(argv)<=3) or len(argv)>=5:
        print("ERR: incorect number of arguments -> see help")
        print_help()
        
    if argv[1]=="-t":
        if argv[2]=="fc":
            print(t_FtoC(float(argv[3])))
            return
        elif argv[2]=="fk":
            print(t_FtoK(float(argv[3])))
            return
        elif argv[2]=="ff":
            print(t_FtoF(float(argv[3])))
            return
        elif argv[2]=="cf":
            print(t_CtoF(float(argv[3])))
            return
        elif argv[2]=="ck":
            print(t_CtoK(float(argv[3])))
            return
        elif argv[2]=="cc":
            print(t_CtoC(float(argv[3])))
            return
        elif argv[2]=="kc":
            print(t_FtoC(float(argv[3])))
            return
        elif argv[2]=="kf":
            print(t_KtoF(float(argv[3])))
            return
        elif argv[2]=="kk":
            print(t_KtoK(float(argv[3])))
            return
        else:
            print("ERR: incorrect input -> see help")
            print_help()
            return
    elif argv[1]=="-fc":
        if argv[2]=="us_mpgus_mpg":
            print(fc_us_mpgtous_mpg(float(argv[3])))
            return
        elif argv[2]=="us_mpguk_mpg":
            print(fc_us_mpgtouk_mpg(float(argv[3])))
            return
        elif argv[2]=="us_mpgl100km":
            print(fc_us_mpgtol100KM(float(argv[3])))
            return
        elif argv[2]=="l100kmus_mpg":
            print(fc_l100KMtous_mpg(float(argv[3])))
            return
        elif argv[2]=="l100kmuk_mpg":
            print(fc_l100kmtouk_mpg(float(argv[3])))
            return
        elif argv[2]=="l100kml100km":
            print(fc_l100KMtol100KM(float(argv[3])))
            return
        elif argv[2]=="uk_mpgus_mpg":
            print(fc_uk_mpgtous_mpg(float(argv[3])))
            return
        elif argv[2]=="uk_mpgl100km":
            print(fc_uk_mpgtol100km(float(argv[3])))
            return
        elif argv[2]=="uk_mpguk_mpg":
            print(fc_uk_mpgtouk_mpg(float(argv[3])))
            return
        else:
            print("ERR: incorrect input -> see help")
            print_help()
            return
    else:
        print("ERR: incorrect input -> see help")
        print_help()
        return
    
if __name__ == "__main__":
    main()
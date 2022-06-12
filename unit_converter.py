from sys import argv

# Required for Testing (comparing floats)
def assert_almost_equal_float(fl1, fl2, delta=0.01):
    assert abs( fl1 - fl2 ) < delta 

# Temp
"""
should temps under 0K be treated as erronous input ?
should they just be converted to 0K 
loud errors or silent "correction"?
Its not addressed here
"""

# F to C
def t_FtoC(f_temp):
    return float(format((f_temp-32)*(5/9),".2f"))

# F to K
def t_FtoK(f_temp):
    return float(format((f_temp-32)*(5/9) + 273.15 ,  ".2f"))

# F to F
def t_FtoF(f_temp):
    return float(format(f_temp,".2f"))

# C to F
def t_CtoF(c_temp):
    return float(format(((9/5)*c_temp)+32 ,  ".2f"))

# C to K
def t_CtoK(c_temp):
    return float(format(c_temp + 273.15,".2f"))

# C to C
def t_CtoC(c_temp):
    return float(format(c_temp,".2f"))

# K to C
def t_KtoC(k_temp):
    return float(format(k_temp - 273.15, ".2f"))

# K to F
def t_KtoF(k_temp):
    return float(format(((9/5)*(k_temp-273.15))+32 ,  ".2f"))

# K to K
def t_KtoK(k_temp):
    return float(format(k_temp,".2f"))

# temperature conversion tests
def temp_test():
    print("Temps")
    print("from to input_v true_v test_v")

    print("f c -40 -40",t_FtoC(-40))
    assert_almost_equal_float( t_FtoC(-40), -40 )

    print("f k -40 233.15",t_FtoK(-40))
    assert_almost_equal_float( t_FtoK(-40), 233.15 )
    
    print("f f 0 0",t_FtoF(0))
    assert_almost_equal_float(t_FtoF(0),0)

    print("k c 0 -273.15",t_KtoC(0))
    assert_almost_equal_float( t_KtoC(0), -273.15 )

    print("k f 0 -459.67",t_KtoF(0))
    assert_almost_equal_float( t_KtoF(0), -459.67 )

    print("k k 0 0", t_KtoK(0))
    assert_almost_equal_float(t_KtoK(0),0)

    print("c f -40 -40", t_CtoF(-40))
    assert_almost_equal_float( t_CtoF(-40), -40 )

    print("c k 0 273.15",t_CtoK(0))
    assert_almost_equal_float( t_CtoK(0), 273.15 )

    print("c c 0 0", t_CtoC(0))
    assert_almost_equal_float(t_CtoC(0),0)

# Fuel Consumption

# us_mpg to l/00Km
def fc_us_mpgtol100KM(fc_us_mpg):
    return float(format(235.237/fc_us_mpg, ".2f"))

# us_mpg to uk_mpg
def fc_us_mpgtouk_mpg(fc_us_mpg):
    return float(format(fc_us_mpg*1.201,".2f"))

# us_mpg to us_mpg
def fc_us_mpgtous_mpg(fc_us_mpg):
    return float(format(fc_us_mpg,".2f"))

# uk_mpg to us_mpg
def fc_uk_mpgtous_mpg(fc_uk_mpg):
    return float(format(fc_uk_mpg*0.832,".2f"))

# uk_mpg to l/100km
def fc_uk_mpgtol100km(fc_uk_mpg):
    return float(format(282.533/fc_uk_mpg,".2f"))

# uk_mpg to uk_mpg
def fc_uk_mpgtouk_mpg(fc_uk_mpg):
    return float(format(fc_uk_mpg,".2f"))

# l/100Km to us_mpg
def fc_l100KMtous_mpg(fc_l100km):
    return float(format(235.237/fc_l100km, ".2f"))

# l/100km to uk_mpg
def fc_l100kmtouk_mpg(fc_l100km):
    return float(format(282.533/fc_l100km,".2f"))

# l/100km to l/100km
def fc_l100KMtol100KM(fc_l100km):
    return float(format(fc_l100km,".2f"))

# fuel consumption tests
def fc_tests():
    print("Fuel Consumption")
    print("from to input_v true_v test_v")

    print("lp100km us_mpg 16 14.7",fc_l100KMtous_mpg(16))
    assert_almost_equal_float(fc_l100KMtous_mpg(16),14.7)

    print("lp100km uk_mpg 16 17.66",fc_l100kmtouk_mpg(16))
    assert_almost_equal_float(fc_l100kmtouk_mpg(16),17.66)

    print("lp100km lp100km 5 5",fc_l100KMtol100KM(5))
    assert_almost_equal_float(fc_l100KMtol100KM(5),5)

    print("us_mpg lp100km 14 16.8",fc_us_mpgtol100KM(14))
    assert_almost_equal_float(fc_us_mpgtol100KM(14), 16.8)

    print("us_mpg uk_mpg 5 6",fc_us_mpgtouk_mpg(5))
    assert_almost_equal_float(fc_us_mpgtouk_mpg(5),6)

    print("us_mpg us_mpg 5 5",fc_us_mpgtous_mpg(5))
    assert_almost_equal_float(fc_us_mpgtous_mpg(5),5)

    print("uk_mpg lp100km 14 20.18",fc_uk_mpgtol100km(14))
    assert_almost_equal_float(fc_uk_mpgtol100km(14), 20.18)

    print("uk_mpg us_mpg 14 11.65",fc_uk_mpgtous_mpg(14))
    assert_almost_equal_float(fc_uk_mpgtous_mpg(14),11.65)

    print("uk_mpg uk_mpg 22 22",fc_uk_mpgtouk_mpg(22))
    assert_almost_equal_float(fc_uk_mpgtouk_mpg(22),22)

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

    #run_tests()

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
from sys import argv

# Required for Testing (comparing floats)
def assert_almost_equal_float(fl1, fl2, delta=0.01):
    assert fl1 - fl2 < delta 

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

# mpg to l/00Km
def fc_MPGtoL100KM(fc_mpg):
    return float(format(235.23/fc_mpg, ".2f"))

# mpg to mpg
def fc_MPGtoMPG(fc_mpg):
    return float(format(fc_mpg,".2f"))

# l/100Km to mpg
def fc_L100KMtoMPG(fc_l100km):
    return float(format(235.23/fc_l100km, ".2f"))

# l/100km to l/100km
def fc_L100KMtoL100KM(fc_l100km):
    return float(format(fc_l100km,".2f"))

# fuel consumption tests
def fc_tests():
    print("Temps")
    print("from to input_v true_v test_v")

    print("lp100km mpg 16 14.7",fc_L100KMtoMPG(16))
    assert_almost_equal_float(fc_L100KMtoMPG(16),14.7)

    print("lp100km lp100km 5 5",fc_MPGtoMPG(5))
    assert_almost_equal_float(fc_L100KMtoL100KM(5),5)

    print("mpg lp100km 14 16.8",fc_MPGtoL100KM(14))
    assert_almost_equal_float(fc_MPGtoL100KM(14), 16.8)

    print("lp100km lp100km 5 5",fc_MPGtoMPG(5))
    assert_almost_equal_float(fc_L100KMtoL100KM(5),5)

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
    print("-fc mpg|l100km,mpg|l100km <value> fuel consumption conversion\n")
    print("example: python unit_converter.py -t cc -40\n")

def main():

    if len(argv)==1:
        print_help()
        return
    if argv[1]=="-h":
        print_help()
        return
    if (len(argv)>=2 and len(argv)<=3) or len(argv)>=5:
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
        if argv[2]=="mpgmpg":
            print(fc_MPGtoMPG(float(argv[3])))
            return
        if argv[2]=="mpgl100km":
            print(fc_MPGtoL100KM(float(argv[3])))
            return
        if argv[2]=="l100kmmpg":
            print(fc_L100KMtoMPG(float(argv[3])))
            return
        if argv[2]=="l100kml100km":
            print(fc_L100KMtoL100KM(float(argv[3])))
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
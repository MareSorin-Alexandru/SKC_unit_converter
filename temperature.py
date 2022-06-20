from auxilliary_functions import *

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
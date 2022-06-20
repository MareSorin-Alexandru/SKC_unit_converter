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

temp_func_map = {
    "t_fc":t_FtoC,
    "t_fk":t_FtoK,
    "t_ff":t_FtoF,

    "t_kf":t_KtoF,
    "t_kc":t_KtoC,
    "t_kk":t_KtoK,

    "t_cf":t_CtoF,
    "t_ck":t_CtoK,
    "t_cc":t_CtoC
}

# temperature conversion tests
def temp_test():
    print("Temps")
    print("from to input_v true_v test_v")

    print("f c -40 -40",t_FtoC(-40))
    assert_almost_equal_float( temp_func_map.get("t_fc")(-40), -40 )

    print("f k -40 233.15",t_FtoK(-40))
    assert_almost_equal_float( temp_func_map.get("t_fk")(-40), 233.15 )
    
    print("f f 0 0",t_FtoF(0))
    assert_almost_equal_float( temp_func_map.get("t_ff")(0), 0 )


    print("k c 0 -273.15",t_KtoC(0))
    assert_almost_equal_float( temp_func_map.get("t_kc")(0), -273.15 )

    print("k f 0 -459.67",t_KtoF(0))
    assert_almost_equal_float( temp_func_map.get("t_kf")(0), -459.67 )

    print("k k 0 0", t_KtoK(0))
    assert_almost_equal_float( temp_func_map.get("t_kk")(0), 0 )
    

    print("c f -40 -40", t_CtoF(-40))
    assert_almost_equal_float( temp_func_map.get("t_cf")(-40), -40 )

    print("c k 0 273.15",t_CtoK(0))
    assert_almost_equal_float( temp_func_map.get("t_ck")(0), 273.15 )

    print("c c 0 0", t_CtoC(0))
    assert_almost_equal_float( temp_func_map.get("t_cc")(0), 0 )
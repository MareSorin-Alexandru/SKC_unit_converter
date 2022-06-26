from auxilliary_functions import *

# Fuel Consumption

# us_mpg to l/00Km
def fc_us_mpgtol100KM(fc_us_mpg):
    return format(235.237/fc_us_mpg, ".2f")

# us_mpg to uk_mpg
def fc_us_mpgtouk_mpg(fc_us_mpg):
    return format(fc_us_mpg*1.201,".2f")

# us_mpg to us_mpg
def fc_us_mpgtous_mpg(fc_us_mpg):
    return format(fc_us_mpg,".2f")

# uk_mpg to us_mpg
def fc_uk_mpgtous_mpg(fc_uk_mpg):
    return format(fc_uk_mpg*0.832,".2f")

# uk_mpg to l/100km
def fc_uk_mpgtol100km(fc_uk_mpg):
    return format(282.533/fc_uk_mpg,".2f")

# uk_mpg to uk_mpg
def fc_uk_mpgtouk_mpg(fc_uk_mpg):
    return format(fc_uk_mpg,".2f")

# l/100Km to us_mpg
def fc_l100KMtous_mpg(fc_l100km):
    return format(235.237/fc_l100km, ".2f")

# l/100km to uk_mpg
def fc_l100kmtouk_mpg(fc_l100km):
    return format(282.533/fc_l100km,".2f")

# l/100km to l/100km
def fc_l100KMtol100KM(fc_l100km):
    return format(fc_l100km,".2f")

fuel_economy_func_map = {
    "fc_us_mpgl100km" : fc_us_mpgtol100KM,
    "fc_us_mpguk_mpg" : fc_us_mpgtouk_mpg,
    "fc_us_mpgus_mpg" : fc_us_mpgtous_mpg,

    "fc_uk_mpgl100km" : fc_uk_mpgtol100km,
    "fc_uk_mpgus_mpg" : fc_uk_mpgtous_mpg,
    "fc_uk_mpguk_mpg" : fc_uk_mpgtouk_mpg,

    "fc_l100kmus_mpg" : fc_l100KMtous_mpg,
    "fc_l100kmuk_mpg" : fc_l100kmtouk_mpg,
    "fc_l100kml100km" : fc_l100KMtol100KM 
}

# fuel consumption tests
def fc_tests():
    print("Fuel Consumption")
    print("from to input_v true_v test_v")

    print("l100km us_mpg 16 14.7",fc_l100KMtous_mpg(16))
    assert_almost_equal_float( float(fuel_economy_func_map.get("fc_l100kmus_mpg")(16)),14.7)

    print("l100km uk_mpg 16 17.66",fc_l100kmtouk_mpg(16))
    assert_almost_equal_float( float(fuel_economy_func_map.get("fc_l100kmuk_mpg")(16)),17.66)

    print("l100km l100km 5 5",fc_l100KMtol100KM(5))
    assert_almost_equal_float( float(fuel_economy_func_map.get("fc_l100kml100km")(5)),5)


    print("us_mpg l100km 14 16.8",fc_us_mpgtol100KM(14))
    assert_almost_equal_float( float(fuel_economy_func_map.get("fc_us_mpgl100km")(14)), 16.8)

    print("us_mpg uk_mpg 5 6",fc_us_mpgtouk_mpg(5))
    assert_almost_equal_float( float(fuel_economy_func_map.get("fc_us_mpguk_mpg")(5)),6)

    print("us_mpg us_mpg 5 5",fc_us_mpgtous_mpg(5))
    assert_almost_equal_float( float(fuel_economy_func_map.get("fc_us_mpgus_mpg")(5)),5)


    print("uk_mpg l100km 14 20.18",fc_uk_mpgtol100km(14))
    assert_almost_equal_float( float(fuel_economy_func_map.get("fc_uk_mpgl100km")(14)), 20.18)

    print("uk_mpg us_mpg 14 11.65",fc_uk_mpgtous_mpg(14))
    assert_almost_equal_float( float(fuel_economy_func_map.get("fc_uk_mpgus_mpg")(14)),11.65)

    print("uk_mpg uk_mpg 22 22",fc_uk_mpgtouk_mpg(22))
    assert_almost_equal_float( float(fuel_economy_func_map.get("fc_uk_mpguk_mpg")(22)),22)
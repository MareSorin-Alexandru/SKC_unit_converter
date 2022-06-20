# Required for Testing (comparing floats)
def assert_almost_equal_float(fl1, fl2, delta=0.01):
    assert abs( fl1 - fl2 ) < delta 
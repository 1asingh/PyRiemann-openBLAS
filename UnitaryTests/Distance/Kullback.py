import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy
from Utils.Distance import Distance
from Utils.CovMat import CovMat
from oldPyRiemann.distance import distance_kullback, distance_kullback_right, distance_kullback_sym

m1 = CovMat.random(10)
m2 = CovMat.random(10)


def test_distance_kullback():
    old_dist = distance_kullback(m1.numpy_array, m2.numpy_array)
    m1.reset_fields()
    m2.reset_fields()
    new_dist = Distance.kullback(m1, m2)

    return _get_state(old_dist, new_dist, "kullback")


def test_distance_kullback_right():
    old_dist = distance_kullback_right(m1.numpy_array, m2.numpy_array)
    m1.reset_fields()
    m2.reset_fields()
    new_dist = Distance.kullback_right(m1, m2)

    return _get_state(old_dist, new_dist, "kullback right")


def test_distance_kullback_sym():
    old_dist = distance_kullback_sym(m1.numpy_array, m2.numpy_array)
    m1.reset_fields()
    m2.reset_fields()
    new_dist = Distance.kullback_sym(m1, m2)

    return _get_state(old_dist, new_dist, "kullback sym")


def _get_state(old, new, func_name):
    if abs( old - new ) < 1e-10:
        print("%s : PASS" % func_name)
        return True
    else:
        print("%s : FAIL" % func_name)
        return False
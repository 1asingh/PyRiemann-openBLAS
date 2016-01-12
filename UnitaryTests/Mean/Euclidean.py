import os
import sys
import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Utils.CovMats import CovMats

from Utils.Mean import Mean
from oldPyRiemann.mean import mean_euclid

def test_mean_euclidean():
    covmats = CovMats.random(10, 10)
    old_dist = mean_euclid(covmats.numpy_array)
    covmats.reset_fields()
    new_dist = Mean.euclidean(covmats)

    return _get_state(old_dist, new_dist, "mean euclidian")


def _get_state(old, new, func_name):
    if abs( old.sum() - new.sum() ) < 1e-10:
        print("%s : PASS" % func_name)
        return True
    else:
        print("%s : FAIL" % func_name)
        return False

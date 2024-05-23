"""
cc_plugin_og/tests/test_basicchecks.py
"""
import os
import unittest
from urllib.parse import urljoin

import numpy as np
import requests_mock
from compliance_checker.tests.helpers import MockTimeSeries
from netCDF4 import Dataset

#from cc_plugin_og import util
from cc_plugin_og.tests.resources import STATIC_FILES

from ..checker import OGChecker


class TestOGCheck(unittest.TestCase):
    # @see
    # http://www.saltycrane.com/blog/2012/07/how-prevent-nose-unittest-using-docstring-when-verbosity-2/
    def shortDescription(self):
        return None

    # Override __str__ and __repr__ behavior to show a copy-pastable
    # nosetest name for ion tests.
    #  ion.module:TestClassName.test_function_name
    def __repr__(self):
        name = self.id()
        name = name.split(".")
        if name[0] not in ["ion", "pyon"]:
            return f"{name[-1]} ({'.'.join(name[:-1])})"
        else:
            return f"{name[-1]} ({'.'.join(name[:-2])} : {'.'.join(name[-2:])})"

    __str__ = __repr__

    def get_dataset(self, nc_dataset):
        """
        Return a pairwise object for the dataset
        """
        if isinstance(nc_dataset, str):
            nc_dataset = Dataset(nc_dataset, "r")
            self.addCleanup(nc_dataset.close)
        return nc_dataset

    def setUp(self):

        self.check = OGChecker()

    def test_good_dataset(self):
        """
        Checks that a file with the proper lat and lon do work
        """
        dataset = self.get_dataset(STATIC_FILES["good_dataset"])
        result = self.check.check_mandatory_variables(dataset)
        self.assertTrue(result.value)

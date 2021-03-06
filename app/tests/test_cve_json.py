# -*- coding: utf-8 -*-
#
# Author:   Stanley Huang
# Project:  crawler 1.0
# Date:     2021-07-10
#
import unittest
from pkg.cvecrawler.cve_json import is_cve_json_filename

class CveJsonTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_is_cve_json_filename_10(self):
        self.assertTrue(is_cve_json_filename('CVE-2021-28809'))
    
    def test_is_cve_json_filename_20(self):
        self.assertTrue(is_cve_json_filename('CVE-2021-3660'))
    
    def test_is_cve_json_filename_30(self):
        self.assertFalse(is_cve_json_filename('CVE-2021-3660.json'))
    
    def test_is_cve_json_filename_40(self):
        self.assertFalse(is_cve_json_filename('openpgp-encrypted-message'))
        
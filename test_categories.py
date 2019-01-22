#!/usr/bin/env python

"""This python script will perform http request and perform basic API validation testing"""

__author__ = "Rey Suela"
__email__ = "rsuela@gmail.com"

import requests
import unittest
import json
import sys
import re

url_endpoint = "https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false"


class CategoriesTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """ This method will run once and will fetch
            the json output from the http endpoint"""
        try:
            request_data = requests.get(url_endpoint)
            if request_data.status_code != 200:
                raise requests.exceptions.RequestException
            self.json_result = json.loads(request_data.text)
        except requests.exceptions.RequestException as e:
            print("Unable to connect to %s" % (url_endpoint))
            sys.exit(0)

    def test_name(self):
        """ Check the result of the json output
            if name value is Carbon credits"""
        self.assertEqual(self.json_result["Name"], "Carbon credits")

    def test_canrelist(self):
        """ Check the result of the json output
            if CanRelist value is True"""
        self.assertTrue(self.json_result["CanRelist"])

    def test_gallery(self):
        """ Parse through the promotions and check if there is an
            element named 'Gallery' and Description contains
            '2x larger image'"""
        for promotion in self.json_result["Promotions"]:
            if promotion["Name"] == "Gallery":
                keyword = re.findall("^2x larger image",
                                     promotion["Description"], re.MULTILINE)
                search = ""
                if keyword:
                    search = keyword[0]
                self.assertEqual(search, "2x larger image")


if __name__ == "__main__":
    unittest.main()

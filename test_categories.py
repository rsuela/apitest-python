#!/usr/bin/env python

"""This python script will perform http request and perform basic API validation testing"""

__author__ = "Rey Suela"
__email__ = "rsuela@gmail.com"

from pyunitreport import HTMLTestRunner
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
        """ Test `Name` property should contain the value `Carbon credits`"""
        try:
            self.assertEqual(self.json_result["Name"], "Carbon credits")
        except KeyError:
            raise AssertionError("ERROR! CanRelist property not found")

    def test_canrelist(self):
        """ Test CanRelist property should contain boolean True"""
        try:
            self.assertTrue(self.json_result["CanRelist"])
        except KeyError:
            raise AssertionError("ERROR! CanRelist property not found")

    def test_gallery(self):
        """ Test if `Gallery` Name is present in Promotions list and 
            Description should contain the value '2x larger image'"""
        isFound = False
        for promotion in self.json_result["Promotions"]:
            if promotion["Name"] == "Gallery":
                isFound = True
                keyword = re.findall("^2x larger image",
                                     promotion["Description"], re.MULTILINE)
                search = ""
                if keyword:
                    search = keyword[0]
                self.assertEqual(search, "2x larger image")
        
        # if gallery is not found in the list this should catch it
        self.assertTrue(isFound, msg="Gallery Object not found")


if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(output=''))
    #unittest.main()

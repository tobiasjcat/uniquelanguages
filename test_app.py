#!/usr/bin/python3

#Paul Croft
#November 20, 2020

import json
import unittest
import requests

test_cases = json.load(open("all_compiled.json"))
# print(test_cases)

class TestEndpoint(unittest.TestCase):
    def test_positive(self):
        for region in test_cases:
            get_response = requests.get("http://localhost:5000/v1/region/{}".format(region))
            self.assertEqual(get_response.status_code, requests.codes.ok)
            self.assertEqual(get_response.json(), json.loads(test_cases[region]))

    def test_non_region(self):
        get_response = requests.get("http://localhost:5000/v1/region/antartica")
        self.assertEqual(get_response.status_code, requests.codes.not_found)

    def test_no_region(self):
        get_response = requests.get("http://localhost:5000/v1/region/")
        self.assertEqual(get_response.status_code, requests.codes.not_found)

    def test_post_request(self):
        get_response = requests.post("http://localhost:5000/v1/region/europe")
        self.assertEqual(get_response.status_code, requests.codes.method_not_allowed)



if __name__ == '__main__':
    unittest.main()
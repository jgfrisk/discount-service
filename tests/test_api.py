import unittest
import requests

class APITests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://localhost:5000/v1"

        # Initialize the database with some data
        requests.post(cls.base_url + "/create", json={"brand": "testbrand1", "number_to_create": 5})
        requests.post(cls.base_url + "/create", json={"brand": "testbrand2", "number_to_create": 3})


    def test_create1(self):
        response = requests.post(self.base_url + "/create", json={"brand": "testbrand", "number_to_create": 10})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 10)

    def test_fetch1(self):
        response = requests.get(self.base_url + "/fetch/testbrand1/user1")
        self.assertTrue("discount_code" in response.json())


    def test_fetch_brand_missing(self):
        response = requests.get(self.base_url + "/fetch/missingbrand/user1")
        self.assertEqual(response.status_code, 404)


    def test_fetch_all(self):
        for counter in range(1,3+1):
            response = requests.get(self.base_url + f"/fetch/testbrand2/user{counter}")
            self.assertEqual(response.status_code, 200)
        # No more codes should exist
        response = requests.get(self.base_url + "/fetch/testbrand2/user4")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()

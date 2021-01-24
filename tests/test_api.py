import unittest
import requests

class APITests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://localhost:5000/v1"

    def test_create1(self):
        response = requests.post(self.base_url + "/create", json={"brand": "testbrand", "number_to_create": 10})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 10)

if __name__ == "__main__":
    unittest.main()

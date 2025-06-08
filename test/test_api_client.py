import unittest
import datetime

from pylivoltek.api_client import ApiClient
from pylivoltek.rest import ApiException


class TestApiClientDatetime(unittest.TestCase):
    def setUp(self):
        self.client = ApiClient()

    def test_deserialize_datetime_valid(self):
        value = "2024-01-02T03:04:05Z"
        result = self.client._ApiClient__deserialize_datetime(value)
        self.assertIsInstance(result, datetime.datetime)

    def test_deserialize_datetime_invalid(self):
        with self.assertRaises(ApiException):
            self.client._ApiClient__deserialize_datetime("not-a-date")


if __name__ == "__main__":
    unittest.main()

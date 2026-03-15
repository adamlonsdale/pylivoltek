import datetime
import unittest

from pylivoltek.api_client import ApiClient
from pylivoltek.configuration import Configuration
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


class TestAuthBehavior(unittest.TestCase):
    def test_configuration_auth_settings_exposes_token_header(self):
        cfg = Configuration()
        cfg.api_key['token'] = 'abc'
        settings = cfg.auth_settings()['token']
        self.assertEqual(settings['in'], 'header')
        self.assertEqual(settings['key'], 'Authorization')
        self.assertEqual(settings['value'], 'abc')

    def test_update_params_for_auth_injects_header(self):
        cfg = Configuration()
        cfg.api_key['token'] = 'abc'
        client = ApiClient(cfg)
        headers = {}
        query = []
        client.update_params_for_auth(headers, query, ['token'])
        self.assertEqual(headers['Authorization'], 'abc')
        self.assertEqual(query, [])


if __name__ == "__main__":
    unittest.main()

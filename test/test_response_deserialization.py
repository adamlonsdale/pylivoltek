import json
import unittest

from pylivoltek.api_client import ApiClient


class _FakeResponse(object):
    def __init__(self, payload):
        self.data = json.dumps(payload).encode()


class ResponseDeserializationTests(unittest.TestCase):
    def setUp(self):
        self.client = ApiClient()

    def test_login_response_uses_login_models(self):
        payload = {
            "code": "200",
            "message": "SUCCESS",
            "data": {
                "msgCode": "operate.success",
                "message": None,
                "data": "jwt-token",
                "msg_code": "operate.success",
            },
        }

        response = self.client.deserialize(_FakeResponse(payload), "LoginResponse")

        self.assertEqual(response.message, "SUCCESS")
        self.assertEqual(response.data.data, "jwt-token")
        self.assertEqual(response.data.msg_code, "operate.success")
        self.assertEqual(response.data.msg_code_legacy, "operate.success")

    def test_site_list_response_uses_paginated_site_models(self):
        payload = {
            "code": "200",
            "message": "SUCCESS",
            "data": {
                "count": 1,
                "list": [{"powerStationId": "site-1", "powerStationName": "Home"}],
            },
        }

        response = self.client.deserialize(_FakeResponse(payload), "SiteListResponse")

        self.assertEqual(response.data.count, 1)
        self.assertEqual(response.data.list[0]["powerStationId"], "site-1")

    def test_device_list_response_uses_paginated_device_models(self):
        payload = {
            "code": "200",
            "message": "SUCCESS",
            "data": {
                "count": 1,
                "list": [{"id": 8, "inverterSn": "INV-001"}],
            },
        }

        response = self.client.deserialize(_FakeResponse(payload), "DeviceListResponse")

        self.assertEqual(response.data.count, 1)
        self.assertEqual(response.data.list[0]["inverterSn"], "INV-001")

    def test_device_energy_summary_response_deserializes_nested_data(self):
        payload = {
            "code": "200",
            "message": "SUCCESS",
            "data": {
                "loadCustomerElectric": "3.1",
                "pvProduceElectric": "137.5",
                "timestamp": 1655769319674,
            },
        }

        response = self.client.deserialize(_FakeResponse(payload), "DeviceEnergySummaryResponse")

        self.assertEqual(response.data.load_customer_electric, "3.1")
        self.assertEqual(response.data.pv_produce_electric, "137.5")
        self.assertEqual(response.data.timestamp, 1655769319674)


if __name__ == "__main__":
    unittest.main()

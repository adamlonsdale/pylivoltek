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

    def test_charging_station_query_response_deserializes_nested_data(self):
        payload = {
            "code": "200",
            "message": "SUCCESS",
            "data": [
                {
                    "adress": "China NanJin",
                    "agent": 238039445626880,
                    "agentAndParent": [0, 238039445626880],
                    "country": 45,
                    "currencyUnitName": "CNY, ￥",
                    "currentPower": "0",
                    "downPrice": [
                        {
                            "endTime": 86400,
                            "id": 757,
                            "powerStation": 620,
                            "price": 0.0,
                            "startTime": 0,
                        }
                    ],
                    "gridTiedType": 1,
                    "id": 620,
                    "imageUrl": None,
                    "isShown": 1,
                    "latitude": 39.983813,
                    "longitude": 116.345813,
                    "name": "testsite",
                    "pvCapacity": "33",
                    "registrationTime": 1685694644000,
                    "registrationTimeZone": "2023-06-02 16:30:44",
                    "status": 2,
                    "systemTypeName": "Residential solar energy storage (ess)",
                    "timezoneValue": "Asia/Shanghai",
                    "todayPowerGeneration": "0",
                    "totalCapacity": "0",
                    "totalPowerGeneration": "0",
                    "upPrice": [
                        {
                            "endTime": 86400,
                            "id": 751,
                            "powerStation": 620,
                            "price": 0.0,
                            "startTime": 0,
                        }
                    ],
                    "updateTime": 0,
                    "workStatus": None,
                }
            ],
        }

        response = self.client.deserialize(_FakeResponse(payload), "ChargingStationQueryResponse")

        self.assertEqual(response.message, "SUCCESS")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0].name, "testsite")
        self.assertEqual(response.data[0].agent_and_parent, [0, 238039445626880])
        self.assertEqual(response.data[0].down_price[0].price, 0.0)
        self.assertEqual(response.data[0].up_price[0].power_station, 620)
        self.assertEqual(response.data[0].total_capacity, "0")

    def test_bess_device_description_response_deserializes_nested_data(self):
        payload = {
            "code": "200",
            "message": "SUCCESS",
            "data": {
                "productType": "Hyper",
                "protocolVersion": "0.48",
                "supportedCommand": "Invert Restart,BMS Restart,Emergency charging",
                "workMode": "backup,user defined,command mode",
            },
        }

        response = self.client.deserialize(_FakeResponse(payload), "BessDeviceDescriptionResponse")

        self.assertEqual(response.message, "SUCCESS")
        self.assertIsNotNone(response.data)
        self.assertEqual(response.data.product_type, "Hyper")
        self.assertEqual(response.data.protocol_version, "0.48")
        self.assertIn("Emergency charging", response.data.supported_command)

    def test_bess_device_description_response_deserializes_flat_fields(self):
        payload = {
            "code": "200",
            "message": "SUCCESS",
            "productType": "Hyper",
            "protocolVersion": "0.46",
            "supportedCommand": "Invert Restart,BMS Restart",
            "workMode": "backup,user defined",
        }

        response = self.client.deserialize(_FakeResponse(payload), "BessDeviceDescriptionResponse")

        self.assertEqual(response.message, "SUCCESS")
        self.assertIsNone(response.data)
        self.assertEqual(response.product_type, "Hyper")
        self.assertEqual(response.protocol_version, "0.46")
        self.assertIn("Invert Restart", response.supported_command)


if __name__ == "__main__":
    unittest.main()

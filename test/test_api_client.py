import datetime
import unittest

from pylivoltek.api_client import ApiClient
from pylivoltek.models.bess_remote_start_stop_request import BessRemoteStartStopRequest
from pylivoltek.models.bess_work_mode_schedule_entry import BessWorkModeScheduleEntry
from pylivoltek.models.bess_work_mode_set_request import BessWorkModeSetRequest
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

    def test_sanitize_for_serialization_serializes_bess_remote_request_model(self):
        payload = self.client.sanitize_for_serialization(
            BessRemoteStartStopRequest(
                account="user@example.com",
                pwd="md5-hash",
                sn="SN-123",
                control_type=1,
            )
        )

        self.assertEqual(
            payload,
            {
                "account": "user@example.com",
                "pwd": "md5-hash",
                "sn": "SN-123",
                "controlType": 1,
            },
        )

    def test_sanitize_for_serialization_keeps_optional_charging_days_when_present(self):
        payload = self.client.sanitize_for_serialization(
            BessWorkModeSetRequest(
                account="user@example.com",
                pwd="md5-hash",
                sn="SN-123",
                work_mode=2,
                schedule_list=[
                    BessWorkModeScheduleEntry(
                        start_hour=11,
                        start_min=0,
                        end_hour=18,
                        end_min=0,
                        charge_type=1,
                        charging_days=[0, 1, 3, 4],
                    )
                ],
            )
        )

        self.assertEqual(payload["workMode"], 2)
        self.assertEqual(payload["scheduleList"][0]["chargingDays"], [0, 1, 3, 4])

    def test_sanitize_for_serialization_omits_optional_charging_days_when_absent(self):
        payload = self.client.sanitize_for_serialization(
            BessWorkModeSetRequest(
                account="user@example.com",
                pwd="md5-hash",
                sn="SN-123",
                work_mode=2,
                schedule_list=[
                    BessWorkModeScheduleEntry(
                        start_hour=9,
                        start_min=0,
                        end_hour=10,
                        end_min=0,
                        charge_type=2,
                    )
                ],
            )
        )

        self.assertEqual(payload["scheduleList"][0]["chargeType"], 2)
        self.assertNotIn("chargingDays", payload["scheduleList"][0])


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

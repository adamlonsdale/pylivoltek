import datetime
import unittest
from unittest import mock

from pylivoltek.api_client import ApiClient
from pylivoltek.configuration import Configuration
from pylivoltek.models.api_response import ApiResponse
from pylivoltek.rest import ApiException


class TestApiClient(unittest.TestCase):
    def setUp(self):
        self.client = ApiClient()

    def tearDown(self):
        self.client.pool.close()
        self.client.pool.join()

    def test_deserialize_datetime_valid(self):
        value = "2024-01-02T03:04:05Z"
        result = self.client._ApiClient__deserialize_datetime(value)
        self.assertIsInstance(result, datetime.datetime)

    def test_deserialize_datetime_invalid(self):
        with self.assertRaises(ApiException):
            self.client._ApiClient__deserialize_datetime("not-a-date")

    def test_sanitize_for_serialization_handles_models_and_dates(self):
        model = ApiResponse(
            code=200,
            message=datetime.date(2024, 1, 2),
        )

        result = self.client.sanitize_for_serialization(
            {
                "payload": model,
                "at": datetime.datetime(2024, 1, 2, 3, 4, 5),
                "items": (1, datetime.date(2024, 1, 3)),
            }
        )

        self.assertEqual(
            result,
            {
                "payload": {"code": 200, "message": "2024-01-02"},
                "at": "2024-01-02T03:04:05",
                "items": (1, "2024-01-03"),
            },
        )

    def test_parameters_to_tuples_expands_supported_collection_formats(self):
        params = {
            "multi": ["a", "b"],
            "ssv": [1, 2],
            "pipes": ["x", "y"],
            "plain": "value",
        }

        result = self.client.parameters_to_tuples(
            params,
            {
                "multi": "multi",
                "ssv": "ssv",
                "pipes": "pipes",
            },
        )

        self.assertEqual(
            result,
            [
                ("multi", "a"),
                ("multi", "b"),
                ("ssv", "1 2"),
                ("pipes", "x|y"),
                ("plain", "value"),
            ],
        )

    def test_update_params_for_auth_populates_header_and_query(self):
        self.client.configuration.auth_settings = mock.Mock(
            return_value={
                "headerAuth": {"in": "header", "key": "X-Token", "value": "abc"},
                "queryAuth": {"in": "query", "key": "token", "value": "xyz"},
            }
        )
        headers = {}
        querys = []

        self.client.update_params_for_auth(
            headers, querys, ["headerAuth", "queryAuth"]
        )

        self.assertEqual(headers, {"X-Token": "abc"})
        self.assertEqual(querys, [("token", "xyz")])

    def test_update_params_for_auth_rejects_unknown_location(self):
        self.client.configuration.auth_settings = mock.Mock(
            return_value={
                "badAuth": {"in": "cookie", "key": "token", "value": "abc"}
            }
        )

        with self.assertRaises(ValueError):
            self.client.update_params_for_auth({}, [], ["badAuth"])

    def test_prepare_post_parameters_reads_files(self):
        file_handle = mock.MagicMock()
        file_handle.__enter__.return_value = file_handle
        file_handle.__exit__.return_value = False
        file_handle.name = "/tmp/example.txt"
        file_handle.read.return_value = b"data"

        with mock.patch("pylivoltek.api_client.open", return_value=file_handle, create=True) as mocked_open:
            with mock.patch("pylivoltek.api_client.mimetypes.guess_type", return_value=("text/plain", None)):
                result = self.client.prepare_post_parameters(
                    post_params=[("name", "value")],
                    files={"upload": "/tmp/example.txt"},
                )

        mocked_open.assert_called_once_with("/tmp/example.txt", "rb")
        self.assertEqual(result[0], ("name", "value"))
        self.assertEqual(result[1][0], "upload")
        self.assertEqual(result[1][1][0], "example.txt")
        self.assertEqual(result[1][1][1], b"data")
        self.assertEqual(result[1][1][2], "text/plain")

    def test_call_api_uses_thread_pool_for_async_requests(self):
        self.client.pool.close()
        self.client.pool.join()
        self.client.pool = mock.Mock()
        self.client.pool.apply_async.return_value = "thread"

        result = self.client.call_api("/sites", "GET", async_req=True)

        self.assertEqual(result, "thread")
        self.client.pool.apply_async.assert_called_once()


class TestConfiguration(unittest.TestCase):
    def test_get_api_key_with_prefix_refreshes_before_lookup(self):
        config = Configuration()

        def refresh(conf):
            conf.api_key["token"] = "new-token"
            conf.api_key_prefix["token"] = "Bearer"

        config.refresh_api_key_hook = refresh

        self.assertEqual(
            config.get_api_key_with_prefix("token"),
            "Bearer new-token",
        )

    def test_debug_toggles_http_debug_level(self):
        config = Configuration()

        config.debug = True
        self.assertEqual(config.logger["package_logger"].level, 10)
        self.assertEqual(config.logger["urllib3_logger"].level, 10)

        config.debug = False
        self.assertEqual(config.logger["package_logger"].level, 30)
        self.assertEqual(config.logger["urllib3_logger"].level, 30)


if __name__ == "__main__":
    unittest.main()

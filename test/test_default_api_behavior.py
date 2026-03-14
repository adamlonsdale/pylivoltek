import unittest
from unittest import mock

from pylivoltek.api.default_api import DefaultApi


class TestDefaultApiBehavior(unittest.TestCase):
    def setUp(self):
        self.api_client = mock.Mock()
        self.api_client.select_header_accept.return_value = "application/json"
        self.api_client.select_header_content_type.return_value = "application/json"
        self.api = DefaultApi(api_client=self.api_client)

    def test_get_device_details_requires_serial_number(self):
        with self.assertRaises(ValueError):
            self.api.get_device_details_with_http_info("token", "site-1", None)

    def test_get_device_details_rejects_unknown_kwarg(self):
        with self.assertRaises(TypeError):
            self.api.get_device_details_with_http_info(
                "token",
                "site-1",
                "serial-1",
                unexpected=True,
            )

    def test_get_device_details_builds_expected_call(self):
        self.api_client.call_api.return_value = "response"

        result = self.api.get_device_details_with_http_info(
            "token",
            "site-1",
            "serial-1",
            user_type="owner",
            _request_timeout=(1, 3),
        )

        self.assertEqual(result, "response")
        self.api_client.call_api.assert_called_once_with(
            "/hess/api/device/{siteId}/{serialNumber}/details",
            "GET",
            {"siteId": "site-1", "serialNumber": "serial-1"},
            [("userToken", "token"), ("userType", "owner")],
            {"Accept": "application/json"},
            body=None,
            post_params=[],
            files={},
            response_type="InlineResponse2005",
            auth_settings=["token"],
            async_req=None,
            _return_http_data_only=None,
            _preload_content=True,
            _request_timeout=(1, 3),
            collection_formats={},
        )

    def test_login_posts_body_without_auth(self):
        self.api_client.call_api.return_value = "login-response"
        body = {"username": "demo", "password": "secret"}

        result = self.api.hess_api_login_post_with_http_info(body)

        self.assertEqual(result, "login-response")
        self.api_client.call_api.assert_called_once_with(
            "/hess/api/login",
            "POST",
            {},
            [],
            {"Accept": "application/json", "Content-Type": "application/json"},
            body=body,
            post_params=[],
            files={},
            response_type="InlineResponse200",
            auth_settings=["token"],
            async_req=None,
            _return_http_data_only=None,
            _preload_content=True,
            _request_timeout=None,
            collection_formats={},
        )

    def test_site_list_wrapper_returns_data_only(self):
        self.api_client.call_api.return_value = "sites"

        result = self.api.hess_api_user_sites_list_get("token", 1, 20)

        self.assertEqual(result, "sites")
        self.api_client.call_api.assert_called_once()
        self.assertTrue(
            self.api_client.call_api.call_args.kwargs["_return_http_data_only"]
        )


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest import mock

import urllib3

from pylivoltek.configuration import Configuration
from pylivoltek.rest import ApiException
from pylivoltek.rest import RESTClientObject


class TestRESTClientObject(unittest.TestCase):
    def setUp(self):
        self.client = RESTClientObject(Configuration())
        self.client.pool_manager = mock.Mock()

    def test_request_rejects_body_and_post_params_together(self):
        with self.assertRaises(ValueError):
            self.client.request(
                "POST",
                "https://example.com",
                body={"x": 1},
                post_params={"y": 2},
            )

    def test_get_request_passes_query_params_as_fields(self):
        response = mock.Mock(status=200, reason="OK", data=b"{}", getheaders=mock.Mock(return_value={}))
        self.client.pool_manager.request.return_value = response

        result = self.client.request(
            "GET",
            "https://example.com/resource",
            query_params=[("page", 2)],
            headers={"Accept": "application/json"},
        )

        self.client.pool_manager.request.assert_called_once_with(
            "GET",
            "https://example.com/resource",
            fields=[("page", 2)],
            preload_content=True,
            timeout=None,
            headers={"Accept": "application/json", "Content-Type": "application/json"},
        )
        self.assertEqual(result.status, 200)

    def test_json_request_serializes_body_and_appends_query_string(self):
        response = mock.Mock(status=200, reason="OK", data=b"{}", getheaders=mock.Mock(return_value={}))
        self.client.pool_manager.request.return_value = response

        self.client.request(
            "POST",
            "https://example.com/resource",
            query_params=[("site", "abc")],
            headers={"Content-Type": "application/json"},
            body={"ok": True},
        )

        self.client.pool_manager.request.assert_called_once_with(
            "POST",
            "https://example.com/resource?site=abc",
            body='{"ok": true}',
            preload_content=True,
            timeout=None,
            headers={"Content-Type": "application/json"},
        )

    def test_multipart_request_drops_content_type_header(self):
        response = mock.Mock(status=200, reason="OK", data=b"{}", getheaders=mock.Mock(return_value={}))
        self.client.pool_manager.request.return_value = response
        headers = {"Content-Type": "multipart/form-data", "X-Test": "1"}

        self.client.request(
            "POST",
            "https://example.com/upload",
            headers=headers,
            post_params=[("file", "value")],
        )

        self.client.pool_manager.request.assert_called_once_with(
            "POST",
            "https://example.com/upload",
            fields=[("file", "value")],
            encode_multipart=True,
            preload_content=True,
            timeout=None,
            headers={"X-Test": "1"},
        )
        self.assertEqual(headers, {"X-Test": "1"})

    def test_request_converts_timeout_tuple(self):
        response = mock.Mock(status=200, reason="OK", data=b"{}", getheaders=mock.Mock(return_value={}))
        self.client.pool_manager.request.return_value = response

        self.client.request(
            "GET",
            "https://example.com/resource",
            _request_timeout=(2, 5),
        )

        timeout = self.client.pool_manager.request.call_args.kwargs["timeout"]
        self.assertIsInstance(timeout, urllib3.Timeout)
        self.assertEqual(timeout.connect_timeout, 2)
        self.assertEqual(timeout.read_timeout, 5)

    def test_request_raises_api_exception_for_non_success_status(self):
        response = mock.Mock(status=500, reason="Boom", data=b"nope", getheaders=mock.Mock(return_value={"X": "1"}))
        self.client.pool_manager.request.return_value = response

        with self.assertRaises(ApiException) as exc:
            self.client.request("GET", "https://example.com/resource")

        self.assertEqual(exc.exception.status, 500)
        self.assertEqual(exc.exception.reason, "Boom")


if __name__ == "__main__":
    unittest.main()

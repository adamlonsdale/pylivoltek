# coding: utf-8
from __future__ import absolute_import

import unittest
import warnings

from pylivoltek.api.default_api import DefaultApi
from pylivoltek.api_client import ApiClient


class DefaultApiBehaviorTests(unittest.TestCase):
    def setUp(self):
        self.client = ApiClient()
        self.calls = []

        def fake_call_api(*args, **kwargs):
            self.calls.append((args, kwargs))
            return {'ok': True}

        self.client.call_api = fake_call_api
        self.api = DefaultApi(self.client)

    def _last(self):
        return self.calls[-1]

    def test_all_primary_methods_call_expected_path_and_verb(self):
        cases = [
            (self.api.list_sites, ('t', 1, 10), {}, 'GET', '/hess/api/userSites/list'),
            (self.api.list_devices, ('t', 9, 1, 10), {}, 'GET', '/hess/api/device/{siteId}/list'),
            (self.api.get_current_power_flow, ('t', 9), {}, 'GET', '/hess/api/site/{siteId}/curPowerflow'),
            (self.api.get_device_generation_or_consumption, ('t', 8), {}, 'GET', '/hess/api/device/{deviceId}/realElectricity'),
            (self.api.get_site_generation_overview, ('t', 9), {}, 'GET', '/hess/api/site/{siteId}/overview'),
            (self.api.get_site_details, ('t', 9), {}, 'GET', '/hess/api/site/{siteId}/details'),
            (self.api.get_site_installer, ('t', 9), {}, 'GET', '/hess/api/site/{siteId}/siteInstaller'),
            (self.api.get_site_historical_power_flow, ('t', 9), {'dateType': 'day'}, 'GET', '/hess/api/site/{siteId}/HisPowerflow'),
            (self.api.get_site_historical_active_power, ('t', 9), {'dateType': 'day'}, 'GET', '/hess/api/site/{siteId}/power'),
            (self.api.get_device_historical_alarm, ('t', 9, 'sn'), {}, 'GET', '/hess/api/device/{siteId}/{serialNumber}/alarm'),
            (self.api.get_site_social_contribution, ('t', 9), {}, 'GET', '/hess/api/site/{siteId}/socialContr'),
            (self.api.get_energy_storage, ('t', 9), {}, 'GET', '/hess/api/site/{siteId}/ESS'),
            (self.api.get_device_details, ('t', 9, 'sn'), {}, 'GET', '/hess/api/device/{siteId}/{serialNumber}/details'),
            (self.api.get_device_technical_parameters, ('t', 9, 'sn'), {}, 'GET', '/hess/api/device/{siteId}/{serialNumber}/realTime'),
            (self.api.get_site_historical_solar_generation, ('t', 9), {'dateType': 'day'}, 'GET', '/hess/api/site/{siteId}/solarEnergy'),
            (self.api.get_site_historical_grid_import_export, ('t', 9), {'dateType': 'day'}, 'GET', '/hess/api/site/{siteId}/utilityEnergy'),
            (self.api.create_charging_station, ('t', {'a': 1}), {}, 'POST', '/hess/api/chargeSite/create'),
            (self.api.query_charging_stations, ('t', {'a': 1}), {}, 'POST', '/hess/api/chargeSite/querySite'),
            (self.api.update_charging_station, ('t', {'a': 1}), {}, 'POST', '/hess/api/chargeSite/update'),
            (self.api.delete_charging_station, ('t', {'a': 1}), {}, 'POST', '/hess/api/chargeSite/disable'),
            (self.api.create_charging_device, ('t', {'a': 1}), {}, 'POST', '/hess/api/chargeDevice/create'),
            (self.api.query_charging_devices, ('t', {'a': 1}), {}, 'POST', '/hess/api/chargeDevice/queryEv'),
            (self.api.delete_charging_device, ('t', {'a': 1}), {}, 'POST', '/hess/api/chargeDevice/disable'),
            (self.api.query_charging_records, ('t', {'a': 1}), {}, 'POST', '/hess/api/chargeRecord'),
            (self.api.send_charging_command, ('t', {'a': 1}), {}, 'POST', '/hess/api/chargeCommandDown'),
            (self.api.set_charging_schedule, ('t', {'a': 1}), {}, 'POST', '/hess/api/chargeSchedule'),
            (self.api.get_power_station_id_by_device_sn, ('t', 'sn'), {}, 'GET', '/hess/api/site/{serialNumber}'),
            (self.api.get_site_owner, ('t', 9), {}, 'GET', '/hess/api/site/{siteId}/siteOwner'),
            (self.api.get_device_basic_data, ('t', {'a': 1}), {}, 'POST', '/hess/api/device/basicData'),
            (self.api.get_device_one_day_fault_alarm, ('t', 9, 'sn'), {}, 'GET', '/hess/api/device/{siteId}/{serialNumber}/oneDayFaultAlarm'),
            (self.api.generate_user_token, ('t', {'a': 1}), {}, 'POST', '/hess/api/user/userToken'),
            (self.api.list_user_tokens, ('t',), {'page': 1, 'size': 10}, 'GET', '/hess/api/user/userTokenList'),
            (self.api.get_device_power_report, ('t', {'a': 1}), {}, 'POST', '/hess/api/sample/energy'),
            (self.api.get_site_day_energy, ('t', {'a': 1}), {}, 'POST', '/hess/api/sample/energy/site/day'),
            (self.api.login, ({'account': 'a'},), {}, 'POST', '/hess/api/login'),
            (self.api.get_recent_energy_import_export, ('t', 9), {}, 'GET', '/hess/api/site/{siteId}/recentUtilityEnergy'),
            (self.api.get_recent_solar_generated_energy, ('t', 9), {}, 'GET', '/hess/api/site/{siteId}/recentSolarEnergy'),
        ]
        for func, args, kwargs, method, path in cases:
            func(*args, **kwargs)
            cargs, ckwargs = self._last()
            self.assertEqual(cargs[0], path)
            self.assertEqual(cargs[1], method)
            self.assertEqual(ckwargs['_return_http_data_only'], True)

    def test_posts_set_json_headers_and_body(self):
        body = {'x': 1}
        self.api.create_charging_station('token', body, user_type='1')
        cargs, _ = self._last()
        self.assertEqual(cargs[3], [('userToken', 'token'), ('userType', '1')])
        self.assertEqual(cargs[4]['Content-Type'], 'application/json')
        self.assertEqual(self._last()[1]['body'], body)

    def test_get_device_technical_parameters_forwards_filters(self):
        self.api.get_device_technical_parameters('tok', 1, 'sn1', startTime='2024-01-01', endTime='2024-01-02')
        cargs, _ = self._last()
        query_params = cargs[3]
        self.assertIn(('userToken', 'tok'), query_params)
        self.assertIn(('startTime', '2024-01-01'), query_params)
        self.assertIn(('endTime', '2024-01-02'), query_params)

    def test_deprecated_wrappers_forward_and_warn(self):
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always')
            self.api.hess_api_user_sites_list_get('t', 1, 10)
            self.assertTrue(any(issubclass(w.category, DeprecationWarning) for w in caught))
        cargs, _ = self._last()
        self.assertEqual(cargs[0], '/hess/api/userSites/list')


if __name__ == '__main__':
    unittest.main()

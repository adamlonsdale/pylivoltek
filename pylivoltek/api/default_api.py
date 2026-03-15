# coding: utf-8

from __future__ import absolute_import

import warnings

from pylivoltek.api_client import ApiClient


class DefaultApi(object):
    """Hand-maintained API surface for Livoltek endpoints."""

    _CALL_KWARGS = frozenset(['async_req', '_return_http_data_only', '_preload_content', '_request_timeout'])

    def __init__(self, api_client=None):
        self.api_client = api_client or ApiClient()

    @staticmethod
    def _split_call_kwargs(kwargs):
        """Separate transport-control kwargs from query-filter kwargs."""
        call_kwargs = {k: v for k, v in kwargs.items() if k in DefaultApi._CALL_KWARGS}
        filters = {k: v for k, v in kwargs.items() if k not in DefaultApi._CALL_KWARGS}
        return call_kwargs, filters

    def _call(self, method, path, response_type='object', path_params=None,
              query_params=None, body=None, auth=True, **kwargs):
        query_params = query_params or []
        header_params = {'Accept': self.api_client.select_header_accept(['application/json'])}
        if body is not None:
            header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json'])
        return self.api_client.call_api(
            path,
            method,
            path_params or {},
            query_params,
            header_params,
            body=body,
            post_params=[],
            files={},
            response_type=response_type,
            auth_settings=['token'] if auth else [],
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only', True),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats={}
        )

    @staticmethod
    def _token_query(user_token, user_type=None, extra=None):
        params = [('userToken', user_token)]
        if user_type is not None:
            params.append(('userType', user_type))
        if extra:
            for key, value in extra.items():
                if value is not None:
                    params.append((key, value))
        return params

    # ---- Existing clean methods ----
    def get_device_details(self, user_token, site_id, serial_number, user_type=None, **kwargs):
        return self._call('GET', '/hess/api/device/{siteId}/{serialNumber}/details', 'InlineResponse2005',
                          path_params={'siteId': site_id, 'serialNumber': serial_number},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_energy_storage(self, user_token, site_id, user_type=None, **kwargs):
        return self._call('GET', '/hess/api/site/{siteId}/ESS', 'InlineResponse2007',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_recent_energy_import_export(self, user_token, site_id, user_type=None, **kwargs):
        return self._call('GET', '/hess/api/site/{siteId}/recentUtilityEnergy', 'InlineResponse2008',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_recent_solar_generated_energy(self, user_token, site_id, user_type=None, **kwargs):
        return self._call('GET', '/hess/api/site/{siteId}/recentSolarEnergy', 'InlineResponse2009',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    # ---- Primary clean methods (spec-covered endpoints) ----
    def list_sites(self, user_token, page, size, user_type=None, **kwargs):
        call_kwargs, filters = self._split_call_kwargs(kwargs)
        filters.update({'page': page, 'size': size})
        return self._call('GET', '/hess/api/userSites/list', 'InlineResponse200',
                          query_params=self._token_query(user_token, user_type, filters), **call_kwargs)

    def list_devices(self, user_token, site_id, page, size, user_type=None, **kwargs):
        call_kwargs, filters = self._split_call_kwargs(kwargs)
        filters.update({'page': page, 'size': size})
        return self._call('GET', '/hess/api/device/{siteId}/list', 'InlineResponse2001',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type, filters), **call_kwargs)

    def get_current_power_flow(self, user_token, site_id, user_type=None, **kwargs):
        return self._call('GET', '/hess/api/site/{siteId}/curPowerflow', 'InlineResponse2004',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_device_generation_or_consumption(self, user_token, device_id, user_type=None, **kwargs):
        return self._call('GET', '/hess/api/device/{deviceId}/realElectricity', 'InlineResponse2006',
                          path_params={'deviceId': device_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_site_generation_overview(self, user_token, site_id, user_type=None, **kwargs):
        return self._call('GET', '/hess/api/site/{siteId}/overview', 'InlineResponse2003',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def login(self, body, **kwargs):
        return self._call('POST', '/hess/api/login', 'InlineResponse2002', body=body, auth=False, **kwargs)

    def get_site_details(self, user_token, site_id, user_type=None, **kwargs):
        return self._call('GET', '/hess/api/site/{siteId}/details',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_site_installer(self, user_token, site_id, user_type=None, **kwargs):
        return self._call('GET', '/hess/api/site/{siteId}/siteInstaller',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_site_historical_power_flow(self, user_token, site_id, user_type=None, **kwargs):
        call_kwargs, filters = self._split_call_kwargs(kwargs)
        return self._call('GET', '/hess/api/site/{siteId}/HisPowerflow',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type, filters), **call_kwargs)

    def get_site_historical_active_power(self, user_token, site_id, user_type=None, **kwargs):
        call_kwargs, filters = self._split_call_kwargs(kwargs)
        return self._call('GET', '/hess/api/site/{siteId}/power',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type, filters), **call_kwargs)

    def get_device_historical_alarm(self, user_token, site_id, serial_number, user_type=None, **kwargs):
        call_kwargs, filters = self._split_call_kwargs(kwargs)
        return self._call('GET', '/hess/api/device/{siteId}/{serialNumber}/alarm',
                          path_params={'siteId': site_id, 'serialNumber': serial_number},
                          query_params=self._token_query(user_token, user_type, filters), **call_kwargs)

    def get_site_social_contribution(self, user_token, site_id, user_type=None, **kwargs):
        return self._call('GET', '/hess/api/site/{siteId}/socialContr',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_device_technical_parameters(self, user_token, site_id, serial_number, user_type=None, **filters):
        return self._call('GET', '/hess/api/device/{siteId}/{serialNumber}/realTime',
                          path_params={'siteId': site_id, 'serialNumber': serial_number},
                          query_params=self._token_query(user_token, user_type, filters))

    def get_site_historical_solar_generation(self, user_token, site_id, user_type=None, **kwargs):
        call_kwargs, filters = self._split_call_kwargs(kwargs)
        return self._call('GET', '/hess/api/site/{siteId}/solarEnergy',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type, filters), **call_kwargs)

    def get_site_historical_grid_import_export(self, user_token, site_id, user_type=None, **kwargs):
        call_kwargs, filters = self._split_call_kwargs(kwargs)
        return self._call('GET', '/hess/api/site/{siteId}/utilityEnergy',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type, filters), **call_kwargs)

    def create_charging_station(self, user_token, body, user_type=None, **kwargs):
        return self._call('POST', '/hess/api/chargeSite/create', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def query_charging_stations(self, user_token, body, user_type=None, **kwargs):
        return self._call('POST', '/hess/api/chargeSite/querySite', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def update_charging_station(self, user_token, body, user_type=None, **kwargs):
        return self._call('POST', '/hess/api/chargeSite/update', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def delete_charging_station(self, user_token, body, user_type=None, **kwargs):
        return self._call('POST', '/hess/api/chargeSite/disable', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def create_charging_device(self, user_token, body, user_type=None, **kwargs):
        return self._call('POST', '/hess/api/chargeDevice/create', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def query_charging_devices(self, user_token, body, user_type=None, **kwargs):
        return self._call('POST', '/hess/api/chargeDevice/queryEv', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def delete_charging_device(self, user_token, body, user_type=None, **kwargs):
        return self._call('POST', '/hess/api/chargeDevice/disable', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def query_charging_records(self, user_token, body, user_type=None, **kwargs):
        return self._call('POST', '/hess/api/chargeRecord', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def send_charging_command(self, user_token, body, user_type=None, **kwargs):
        return self._call('POST', '/hess/api/chargeCommandDown', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def set_charging_schedule(self, user_token, body, user_type=None, **kwargs):
        return self._call('POST', '/hess/api/chargeSchedule', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def get_power_station_id_by_device_sn(self, user_token, serial_number, user_type=None, **kwargs):
        return self._call('GET', '/hess/api/site/{serialNumber}', path_params={'serialNumber': serial_number},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_site_owner(self, user_token, site_id, user_type=None, **kwargs):
        return self._call('GET', '/hess/api/site/{siteId}/siteOwner', path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_device_basic_data(self, user_token, user_type=None, **filters):
        return self._call('GET', '/hess/api/device/basicData',
                          query_params=self._token_query(user_token, user_type, filters))

    def get_device_one_day_fault_alarm(self, user_token, site_id, serial_number, user_type=None, **kwargs):
        return self._call('GET', '/hess/api/device/{siteId}/{serialNumber}/oneDayFaultAlarm',
                          path_params={'siteId': site_id, 'serialNumber': serial_number},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def generate_user_token(self, body, user_type=None, **kwargs):
        query_params = []
        if user_type is not None:
            query_params.append(('userType', user_type))
        return self._call('POST', '/hess/api/user/userToken', query_params=query_params, body=body, **kwargs)

    def list_user_tokens(self, user_token, user_type=None, **kwargs):
        call_kwargs, filters = self._split_call_kwargs(kwargs)
        return self._call('GET', '/hess/api/user/userTokenList', query_params=self._token_query(user_token, user_type, filters), **call_kwargs)

    def get_device_power_report(self, user_token, body, user_type=None, **kwargs):
        return self._call('POST', '/hess/api/sample/energy', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def get_site_day_energy(self, user_token, body, user_type=None, **kwargs):
        return self._call('POST', '/hess/api/sample/energy/site/day', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    # ---- Deprecated generated wrappers ----
    def _deprecated(self, old_name, new_name):
        warnings.warn('%s is deprecated; use %s instead.' % (old_name, new_name), DeprecationWarning, stacklevel=2)

    def hess_api_user_sites_list_get(self, user_token, page, size, **kwargs):
        self._deprecated('hess_api_user_sites_list_get', 'list_sites')
        return self.list_sites(user_token, page, size, **kwargs)

    def hess_api_device_site_id_list_get(self, user_token, site_id, page, size, **kwargs):
        self._deprecated('hess_api_device_site_id_list_get', 'list_devices')
        return self.list_devices(user_token, site_id, page, size, **kwargs)

    def hess_api_site_site_id_cur_powerflow_get(self, user_token, site_id, **kwargs):
        self._deprecated('hess_api_site_site_id_cur_powerflow_get', 'get_current_power_flow')
        return self.get_current_power_flow(user_token, site_id, **kwargs)

    def hess_api_device_device_id_real_electricity_get(self, user_token, device_id, **kwargs):
        self._deprecated('hess_api_device_device_id_real_electricity_get', 'get_device_generation_or_consumption')
        return self.get_device_generation_or_consumption(user_token, device_id, **kwargs)

    def hess_api_site_site_id_overview_get(self, user_token, site_id, **kwargs):
        self._deprecated('hess_api_site_site_id_overview_get', 'get_site_generation_overview')
        return self.get_site_generation_overview(user_token, site_id, **kwargs)

    def hess_api_login_post(self, body, **kwargs):
        self._deprecated('hess_api_login_post', 'login')
        return self.login(body, **kwargs)

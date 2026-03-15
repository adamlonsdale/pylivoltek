# coding: utf-8

from __future__ import absolute_import

import warnings

from pylivoltek.api_client import ApiClient


class DefaultApi(object):
    """Hand-maintained API surface for Livoltek endpoints."""

    _CALL_KWARGS = frozenset(['async_req', '_return_http_data_only', '_preload_content', '_request_timeout'])

    def __init__(self, api_client=None):
        """
        Initialise the DefaultApi with a configured ApiClient.
        
        Parameters:
            api_client (ApiClient, optional): An ApiClient instance to use for requests. If omitted, a new ApiClient() is created and assigned.
        """
        self.api_client = api_client or ApiClient()

    @staticmethod
    def _split_call_kwargs(kwargs):
        """
        Partition keyword arguments into transport-control options and query filters.
        
        Returns:
            tuple: A pair (call_kwargs, filters) where `call_kwargs` is a dict of transport-control
            keyword names (those in DefaultApi._CALL_KWARGS) mapped to their values, and `filters` is a
            dict of the remaining keyword arguments to be used as query/filter parameters.
        """
        call_kwargs = {k: v for k, v in kwargs.items() if k in DefaultApi._CALL_KWARGS}
        filters = {k: v for k, v in kwargs.items() if k not in DefaultApi._CALL_KWARGS}
        return call_kwargs, filters

    def _call(self, method, path, response_type='object', path_params=None,
              query_params=None, body=None, auth=True, **kwargs):
        """
        Construct and dispatch an HTTP request to the configured ApiClient for a given endpoint.

        Builds Accept/Content-Type headers, ensures query parameters default to a list, and forwards request details
        to self.api_client.call_api.

        Parameters:
        	method (str): HTTP method (e.g. 'GET', 'POST').
        	path (str): Request path template (e.g. '/hess/api/site/{siteId}').
        	response_type (str): Expected response model name used for deserialization.
        	path_params (dict, optional): Mapping of path template keys to values.
        	query_params (list, optional): List of (key, value) tuples to be appended to the URL.
        	body (object, optional): Request body to be sent as JSON when provided.
        	auth (bool, optional): If True, use the client's token-based auth settings; if False, omit auth.
        	**kwargs: Transport-control options propagated to the ApiClient. Recognised keys:
        		- async_req: request executed asynchronously when truthy.
        		- _return_http_data_only: return only deserialised data when True.
        		- _preload_content: whether to preload response content.
        		- _request_timeout: timeout for the request.

        Returns:
        	The deserialised response corresponding to `response_type` (or raw response when client is configured so).
        """
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
        """
        Builds a list of query parameter (name, value) pairs for authentication and optional filters.
        
        Parameters:
            user_token (str): Authentication token to include as the 'userToken' query parameter.
            user_type (str | None): Optional user type to include as the 'userType' query parameter when not None.
            extra (dict | None): Optional mapping of additional query parameter names to values; entries with value None are omitted.
        
        Returns:
            list[tuple]: List of (key, value) tuples suitable for use as query parameters. The list always contains ('userToken', user_token) and includes ('userType', user_type) only if user_type is not None; keys from `extra` are appended for non-None values.
        """
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
        """
        Retrieve detailed information for a device at a specific site.
        
        Parameters:
            user_token (str): Authentication token identifying the user.
            site_id (str|int): Identifier of the site that contains the device.
            serial_number (str): Serial number of the device to fetch details for.
            user_type (str, optional): Optional user type to scope the request.
            **kwargs: Transport and request-control options (e.g. timeout, async_req).
        
        Returns:
            InlineResponse2005: Parsed response object containing the device's detailed information.
        """
        return self._call('GET', '/hess/api/device/{siteId}/{serialNumber}/details', 'InlineResponse2005',
                          path_params={'siteId': site_id, 'serialNumber': serial_number},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_energy_storage(self, user_token, site_id, user_type=None, **kwargs):
        """
        Retrieve energy storage information for a site.
        
        Parameters:
            user_token (str): Authentication token for the user.
            site_id (str|int): Identifier of the site.
            user_type (str, optional): Optional user type to include in the query.
            **kwargs: Additional transport-level options (e.g. async_req, _return_http_data_only, _preload_content, _request_timeout).
        
        Returns:
            InlineResponse2007: Parsed response containing the site's energy storage details.
        """
        return self._call('GET', '/hess/api/site/{siteId}/ESS', 'InlineResponse2007',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_recent_energy_import_export(self, user_token, site_id, user_type=None, **kwargs):
        """
        Retrieve recent grid import and export energy data for a site.
        
        Parameters:
            user_token (str): Authentication token identifying the user.
            site_id (str|int): Identifier of the site to query.
            user_type (str, optional): Optional user type to include in the query parameters.
            **kwargs: Transport and request-control options (for example: async_req, _return_http_data_only, _preload_content, _request_timeout).
        
        Returns:
            InlineResponse2008: Recent utility (grid) import and export energy data for the specified site.
        """
        return self._call('GET', '/hess/api/site/{siteId}/recentUtilityEnergy', 'InlineResponse2008',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_recent_solar_generated_energy(self, user_token, site_id, user_type=None, **kwargs):
        """
        Retrieve recent solar-generated energy data for the specified site.
        
        Parameters:
            user_token (str): User authentication token.
            site_id (str|int): Identifier of the site to query.
            user_type (str, optional): Optional user type to include in the query parameters; when omitted, no userType is sent.
        
        Returns:
            InlineResponse2009: Recent solar energy measurements and associated metadata for the site.
        """
        return self._call('GET', '/hess/api/site/{siteId}/recentSolarEnergy', 'InlineResponse2009',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    # ---- Primary clean methods (spec-covered endpoints) ----
    def list_sites(self, user_token, page, size, user_type=None, **kwargs):
        """
        List user sites for a given token with paging and optional filters.
        
        Parameters:
            user_token (str): Authentication token identifying the user.
            page (int): Page number to retrieve (zero-based or one-based per API semantics).
            size (int): Number of items per page.
            user_type (str | None): Optional user type to include in the query parameters.
            **kwargs: Additional query filters (passed as query parameters) and transport-control options
                (async_req, _return_http_data_only, _preload_content, _request_timeout). Filters are merged
                with `page` and `size` before sending.
        
        Returns:
            InlineResponse200: API response object containing the paginated list of user sites.
        """
        call_kwargs, filters = self._split_call_kwargs(kwargs)
        filters.update({'page': page, 'size': size})
        return self._call('GET', '/hess/api/userSites/list', 'InlineResponse200',
                          query_params=self._token_query(user_token, user_type, filters), **call_kwargs)

    def list_devices(self, user_token, site_id, page, size, user_type=None, **kwargs):
        """
        Retrieve a paginated list of devices for a site.
        
        Parameters:
            user_token (str): Authentication token identifying the user.
            site_id (str|int): Identifier of the site whose devices are requested.
            page (int): Page index for pagination.
            size (int): Number of items per page.
            user_type (str, optional): Optional user type included in the query parameters.
            **kwargs: Additional query filters forwarded as query parameters (e.g. search or filter fields).
        
        Returns:
            InlineResponse2001: Response model containing the paginated list of devices and associated metadata.
        """
        call_kwargs, filters = self._split_call_kwargs(kwargs)
        filters.update({'page': page, 'size': size})
        return self._call('GET', '/hess/api/device/{siteId}/list', 'InlineResponse2001',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type, filters), **call_kwargs)

    def get_current_power_flow(self, user_token, site_id, user_type=None, **kwargs):
        """
        Retrieve the current power flow for a site.
        
        Parameters:
            user_token (str): Authentication token associated with the user.
            site_id (str|int): Identifier of the site to query.
            user_type (str, optional): Optional user type to include in the request.
            **kwargs: Additional query filters or transport-control options (for example `page`, `size`, `async_req`, `_request_timeout`).
        
        Returns:
            InlineResponse2004: Parsed response containing the site's current power flow data.
        """
        return self._call('GET', '/hess/api/site/{siteId}/curPowerflow', 'InlineResponse2004',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_device_generation_or_consumption(self, user_token, device_id, user_type=None, **kwargs):
        """
        Retrieve real-time electricity generation or consumption data for a specific device.
        
        Parameters:
            user_token (str): User authentication token to include in the request.
            device_id (str): Identifier of the device to query.
            user_type (str, optional): Optional user type to include in the request query.
            **kwargs: Additional query filters or transport options passed through to the request (for example timeout or pagination).
        
        Returns:
            InlineResponse2006: Response object containing the device's current generation and consumption metrics.
        """
        return self._call('GET', '/hess/api/device/{deviceId}/realElectricity', 'InlineResponse2006',
                          path_params={'deviceId': device_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_site_generation_overview(self, user_token, site_id, user_type=None, **kwargs):
        """
        Retrieve the generation overview for the specified site.
        
        Parameters:
        	user_token (str): Authentication token sent as the `userToken` query parameter.
        	site_id (str|int): Identifier of the site inserted into the request path.
        	user_type (str, optional): Optional user type included as the `userType` query parameter.
        
        Returns:
        	InlineResponse2003: The site's generation overview data.
        """
        return self._call('GET', '/hess/api/site/{siteId}/overview', 'InlineResponse2003',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def login(self, body, **kwargs):
        """
        Authenticate with the API using the provided login payload.
        
        Parameters:
        	body (dict): Login request payload containing credentials and any required fields for authentication.
        
        Returns:
        	InlineResponse2002: Authentication response object from the server, typically containing an access token and related user information.
        """
        return self._call('POST', '/hess/api/login', 'InlineResponse2002', body=body, auth=False, **kwargs)

    def get_site_details(self, user_token, site_id, user_type=None, **kwargs):
        """
        Retrieve details for a specific site.
        
        Parameters:
            user_token (str): Authentication token for the user.
            site_id (str|int): Identifier of the site to retrieve.
            user_type (str, optional): Optional user type to include in the query parameters.
            **kwargs: Additional transport-control options or query filters; transport options include
                async_req, _return_http_data_only, _preload_content and _request_timeout.
        
        Returns:
            The deserialised response object containing the site's details.
        """
        return self._call('GET', '/hess/api/site/{siteId}/details',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_site_installer(self, user_token, site_id, user_type=None, **kwargs):
        """
        Retrieve installer details for the specified site.
        
        Parameters:
            user_token (str): Authentication token for the user.
            site_id (str|int): Identifier of the site.
            user_type (str, optional): Optional user type to include in the request query.
            **kwargs: Additional transport or filter keyword arguments forwarded to the underlying request (e.g. pagination or request options).
        
        Returns:
            dict: Deserialised response containing the site's installer details.
        """
        return self._call('GET', '/hess/api/site/{siteId}/siteInstaller',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_site_historical_power_flow(self, user_token, site_id, user_type=None, **kwargs):
        """
        Retrieve historical power flow data for a site.
        
        Parameters:
            user_token (str): Authentication token identifying the user.
            site_id (str|int): Identifier of the site to query.
            user_type (str, optional): Optional user type to include in the query parameters.
            **kwargs: Additional query filters and transport-control options (e.g. pagination filters, async_req, _return_http_data_only, _preload_content, _request_timeout).
        
        Returns:
            Parsed response containing the site's historical power flow data.
        """
        call_kwargs, filters = self._split_call_kwargs(kwargs)
        return self._call('GET', '/hess/api/site/{siteId}/HisPowerflow',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type, filters), **call_kwargs)

    def get_site_historical_active_power(self, user_token, site_id, user_type=None, **kwargs):
        """
        Retrieve historical active power data for a site.
        
        Parameters:
        	user_token (str): User authentication token to include in the query.
        	site_id (str|int): Identifier of the site whose historical active power is requested.
        	user_type (str, optional): Optional user type to include in the query parameters.
        	**kwargs: Additional query filters (for example date range or pagination) and transport-control options:
        		accepted transport kwargs are `async_req`, `_return_http_data_only`, `_preload_content`, `_request_timeout`.
        
        Returns:
        	Parsed API response as a Python object.
        """
        call_kwargs, filters = self._split_call_kwargs(kwargs)
        return self._call('GET', '/hess/api/site/{siteId}/power',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type, filters), **call_kwargs)

    def get_device_historical_alarm(self, user_token, site_id, serial_number, user_type=None, **kwargs):
        """
        Retrieve the historical alarm records for a specific device at a site.
        
        Parameters:
            user_token (str): User authentication token included in the query parameters.
            site_id (str): Identifier of the site containing the device.
            serial_number (str): Device serial number.
            user_type (str, optional): Optional user type included in the query parameters.
            **kwargs: Additional query filters (e.g. time-range, paging) and transport control options such as
                `async_req`, `_return_http_data_only`, `_preload_content`, `_request_timeout`.
        
        Returns:
            The device's historical alarm data as returned by the API.
        """
        call_kwargs, filters = self._split_call_kwargs(kwargs)
        return self._call('GET', '/hess/api/device/{siteId}/{serialNumber}/alarm',
                          path_params={'siteId': site_id, 'serialNumber': serial_number},
                          query_params=self._token_query(user_token, user_type, filters), **call_kwargs)

    def get_site_social_contribution(self, user_token, site_id, user_type=None, **kwargs):
        """
        Fetches social contribution metrics for the specified site.
        
        Parameters:
            user_token (str): Authentication token identifying the user.
            site_id (str|int): Identifier of the site to query.
            user_type (str, optional): Optional user type to include in the query parameters.
        
        Returns:
            object: The social contribution data returned by the API, parsed as an object.
        """
        return self._call('GET', '/hess/api/site/{siteId}/socialContr',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_device_technical_parameters(self, user_token, site_id, serial_number, user_type=None, **kwargs):
        """
        Retrieve real-time technical parameters for a device.

        Parameters:
            user_token (str): User authentication token included in the query string.
            site_id (str|int): Identifier of the site that contains the device.
            serial_number (str): Device serial number.
            user_type (str, optional): Optional user type included in the query string.
            **kwargs: Additional query parameters to include in the request and transport-control options (async_req, _return_http_data_only, _preload_content, _request_timeout).

        Returns:
            object: The parsed response object from the device real-time parameters endpoint.
        """
        call_kwargs, filters = self._split_call_kwargs(kwargs)
        return self._call('GET', '/hess/api/device/{siteId}/{serialNumber}/realTime',
                          path_params={'siteId': site_id, 'serialNumber': serial_number},
                          query_params=self._token_query(user_token, user_type, filters), **call_kwargs)

    def get_site_historical_solar_generation(self, user_token, site_id, user_type=None, **kwargs):
        """
        Retrieve historical solar generation data for the specified site.
        
        Parameters:
            user_token (str): Authentication token identifying the user.
            site_id (str|int): Identifier of the site to query.
            user_type (str, optional): Optional user type to include in the request query.
            **kwargs: Additional query filters and transport-control options. Query filters are forwarded as request parameters; transport-control options recognised and removed by the client are: `async_req`, `_return_http_data_only`, `_preload_content`, `_request_timeout`.
        
        Returns:
            InlineResponse2009: Response object containing the site's historical solar generation data.
        """
        call_kwargs, filters = self._split_call_kwargs(kwargs)
        return self._call('GET', '/hess/api/site/{siteId}/solarEnergy',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type, filters), **call_kwargs)

    def get_site_historical_grid_import_export(self, user_token, site_id, user_type=None, **kwargs):
        """
        Retrieve historical grid import/export data for the specified site.
        
        Parameters:
            user_token (str): Authentication token identifying the user.
            site_id (str|int): Identifier of the site to query.
            user_type (str, optional): Optional user category to include in the query.
            **kwargs: Optional query filters (for example pagination or time-range filters) and transport-control options; transport-specific kwargs are separated from query filters automatically.
        
        Returns:
            The parsed response from the API containing the site's historical grid import/export data.
        """
        call_kwargs, filters = self._split_call_kwargs(kwargs)
        return self._call('GET', '/hess/api/site/{siteId}/utilityEnergy',
                          path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type, filters), **call_kwargs)

    def create_charging_station(self, user_token, body, user_type=None, **kwargs):
        """
        Create a new charging station for the authenticated user.
        
        Parameters:
            user_token (str): Authentication token to include as `userToken` in the query.
            body (dict): Payload describing the charging station to create.
            user_type (str, optional): Optional `userType` value to include in the query.
        
        Returns:
            The parsed response returned by the API.
        """
        return self._call('POST', '/hess/api/chargeSite/create', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def query_charging_stations(self, user_token, body, user_type=None, **kwargs):
        """
        Query charging stations for the specified user.
        
        Parameters:
            user_token (str): Authentication token identifying the user.
            body (dict): Request payload containing query parameters for charging stations.
            user_type (str, optional): Optional user type to include in the query parameters.
            **kwargs: Additional transport or filter keyword arguments forwarded to the request.
        
        Returns:
            The API response containing the queried charging station data.
        """
        return self._call('POST', '/hess/api/chargeSite/querySite', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def update_charging_station(self, user_token, body, user_type=None, **kwargs):
        """
        Update an existing charging station.
        
        Parameters:
            user_token (str): Authentication token identifying the user.
            body (dict): Payload containing charging station fields to update.
            user_type (str, optional): Optional user type included in the query parameters.
            **kwargs: Additional transport or call options accepted by the client (for example `async_req`, `_return_http_data_only`, `_preload_content`, `_request_timeout`).
        
        Returns:
            object: Parsed response from the API representing the result of the update operation.
        """
        return self._call('POST', '/hess/api/chargeSite/update', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def delete_charging_station(self, user_token, body, user_type=None, **kwargs):
        """
        Disable a charging station.
        
        Parameters:
            user_token (str): Authentication token identifying the user.
            body (dict): Payload containing charging station identification and any fields required to disable it.
            user_type (str, optional): Optional type of the user to include alongside the token.
            **kwargs: Transport and request-control options (for example `async_req`, `_return_http_data_only`, `_preload_content`, `_request_timeout`).
        
        Returns:
            The parsed response object returned by the API.
        """
        return self._call('POST', '/hess/api/chargeSite/disable', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def create_charging_device(self, user_token, body, user_type=None, **kwargs):
        """
        Create a new charging device associated with the authenticated user.
        
        Parameters:
            user_token (str): Authentication token to include as `userToken` in the query string.
            body (dict): Request payload to send as the JSON body when creating the charging device.
            user_type (str, optional): If provided, included as `userType` in the query string.
            **kwargs: Additional transport-control or query-filter keyword arguments forwarded to the request (for example `page`, `size`, `async_req`, `_request_timeout`).
        
        Returns:
            object: The deserialised response returned by the API.
        """
        return self._call('POST', '/hess/api/chargeDevice/create', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def query_charging_devices(self, user_token, body, user_type=None, **kwargs):
        """
        Query charging devices for the specified user using the provided request body.
        
        Parameters:
            user_token (str): Authentication token for the user.
            body (dict): Request payload containing query criteria.
            user_type (str, optional): Optional user type to include in the query parameters.
            **kwargs: Optional transport-level keyword arguments (e.g. async_req, _return_http_data_only).
        
        Returns:
            object: The API response deserialised into a Python object (typically a dict).
        """
        return self._call('POST', '/hess/api/chargeDevice/queryEv', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def delete_charging_device(self, user_token, body, user_type=None, **kwargs):
        """
        Disable a charging device for the authorised user.
        
        Parameters:
            user_token (str): Authentication token sent as the `userToken` query parameter.
            body (dict): Request payload containing the charging device information required to disable it.
            user_type (str, optional): Optional user type sent as the `userType` query parameter.
        
        Returns:
            dict: Parsed response data returned by the disable charging device endpoint.
        """
        return self._call('POST', '/hess/api/chargeDevice/disable', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def query_charging_records(self, user_token, body, user_type=None, **kwargs):
        """
        Query charging records for the authorised user.
        
        Parameters:
            user_token (str): Authentication token identifying the user.
            body (dict): Request payload containing query criteria for charging records.
            user_type (str, optional): Optional user type to include in the request query parameters.
        
        Returns:
            object: Parsed response from the API containing the matching charging records.
        """
        return self._call('POST', '/hess/api/chargeRecord', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def send_charging_command(self, user_token, body, user_type=None, **kwargs):
        """
        Send a remote charging command to a charging device associated with the authenticated user.
        
        Parameters:
            user_token (str): Authentication token identifying the user making the request.
            body (dict): Payload describing the charging command and its parameters.
            user_type (str, optional): Optional user type to include in the request query parameters.
            **kwargs: Transport-level keyword arguments (for example timeout or async options) are forwarded to the underlying client and are not documented here.
        
        Returns:
            object: The API response body deserialised to a Python object.
        """
        return self._call('POST', '/hess/api/chargeCommandDown', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def set_charging_schedule(self, user_token, body, user_type=None, **kwargs):
        """
        Set or update the charging schedule for a site or device.
        
        Parameters:
            user_token (str): Authentication token identifying the user.
            body (dict): Payload describing the charging schedule.
            user_type (str, optional): Optional user type to include in the request query.
        
        Returns:
            object: Deserialised response from the API.
        """
        return self._call('POST', '/hess/api/chargeSchedule', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def get_power_station_id_by_device_sn(self, user_token, serial_number, user_type=None, **kwargs):
        """
        Retrieve the power station (site) identifier associated with a device serial number.
        
        Parameters:
            user_token (str): Authentication token for the requesting user.
            serial_number (str): Device serial number used to look up the site.
            user_type (str, optional): Optional user type to include in the request.
            **kwargs: Additional query filters or transport-control options (e.g. pagination filters, async_req).
        
        Returns:
            The API response containing the power station (site) identifier for the given device.
        """
        return self._call('GET', '/hess/api/site/{serialNumber}', path_params={'serialNumber': serial_number},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_site_owner(self, user_token, site_id, user_type=None, **kwargs):
        """
        Retrieve owner information for the specified site.
        
        Parameters:
        	user_token (str): Authentication token identifying the user.
        	site_id (str|int): Identifier of the site.
        	user_type (str, optional): Optional user type to include in the query.
        	**kwargs: Optional transport-control and query-filter parameters; transport-related keys (e.g. async_req, _return_http_data_only, _preload_content, _request_timeout) are handled separately.
        
        Returns:
        	Owner information for the site as returned by the API.
        """
        return self._call('GET', '/hess/api/site/{siteId}/siteOwner', path_params={'siteId': site_id},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def get_device_basic_data(self, user_token, user_type=None, **kwargs):
        """
        Retrieve basic device data for the authorised user.

        Parameters:
            user_token (str): Authentication token identifying the user.
            user_type (str, optional): Optional user type to include in the query parameters.
            **kwargs: Additional query filters to include and transport-control options (async_req, _return_http_data_only, _preload_content, _request_timeout).

        Returns:
            object: Parsed JSON response containing the device basic data.
        """
        call_kwargs, filters = self._split_call_kwargs(kwargs)
        return self._call('GET', '/hess/api/device/basicData',
                          query_params=self._token_query(user_token, user_type, filters), **call_kwargs)

    def get_device_one_day_fault_alarm(self, user_token, site_id, serial_number, user_type=None, **kwargs):
        """
        Retrieve one-day fault alarm data for a specific device.
        
        Parameters:
        	user_token (str): Authentication token identifying the user.
        	site_id (str|int): Identifier of the site containing the device.
        	serial_number (str): Device serial number.
        	user_type (str, optional): Optional user type filter to include in the request.
        	**kwargs: Additional transport/control keyword arguments such as `async_req`, `_return_http_data_only`, `_preload_content`, `_request_timeout`.
        
        Returns:
        	Parsed response object representing the device's one-day fault alarm data.
        """
        return self._call('GET', '/hess/api/device/{siteId}/{serialNumber}/oneDayFaultAlarm',
                          path_params={'siteId': site_id, 'serialNumber': serial_number},
                          query_params=self._token_query(user_token, user_type), **kwargs)

    def generate_user_token(self, body, user_type=None, **kwargs):
        """
        Generate a user token for the given request payload.
        
        Parameters:
            body (dict): Request payload sent in the POST body to create or retrieve a user token.
            user_type (str, optional): If provided, adds `userType` as a query parameter to the request.
        
        Returns:
            The parsed response from the server containing token information.
        """
        query_params = []
        if user_type is not None:
            query_params.append(('userType', user_type))
        return self._call('POST', '/hess/api/user/userToken', query_params=query_params, body=body, **kwargs)

    def list_user_tokens(self, body, user_type=None, **kwargs):
        """
        List user tokens for the supplied request payload.
        
        Parameters:
            body (dict): Request payload sent in the POST body.
            user_type (str, optional): Filter to include as the `userType` query parameter.
        
        Returns:
            dict: Parsed JSON response from the server containing the user token list.
        """
        query_params = []
        if user_type is not None:
            query_params.append(('userType', user_type))
        return self._call('POST', '/hess/api/user/userTokenList', query_params=query_params, body=body, **kwargs)

    def get_device_power_report(self, user_token, body, user_type=None, **kwargs):
        """
        Request a device power report for the site or device described by the request body.
        
        Parameters:
            user_token (str): User authentication token sent as the `userToken` query parameter.
            body (dict): Request payload specifying report parameters (for example time range or aggregation).
            user_type (str, optional): Optional user type sent as the `userType` query parameter.
            **kwargs: Additional transport/client options forwarded to the API client (e.g. timeout, async flags).
        
        Returns:
            object: Parsed response returned by the API client (typically a dict representing the power report).
        """
        return self._call('POST', '/hess/api/sample/energy', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    def get_site_day_energy(self, user_token, body, user_type=None, **kwargs):
        """
        Retrieve daily energy data for a site.
        
        Parameters:
        	user_token (str): Authentication token for the user.
        	body (dict): Request payload specifying the site and day-range parameters required by the endpoint.
        	user_type (str, optional): Optional user type to include in the query parameters.
        	**kwargs: Optional transport and filtering keyword arguments (e.g. pagination, timeout, async flags).
        
        Returns:
        	Parsed response object from the /hess/api/sample/energy/site/day endpoint.
        """
        return self._call('POST', '/hess/api/sample/energy/site/day', query_params=self._token_query(user_token, user_type), body=body, **kwargs)

    # ---- Deprecated generated wrappers ----
    def _deprecated(self, old_name, new_name):
        """
        Emit a deprecation warning indicating an old API name has been replaced by a new name.
        
        Parameters:
            old_name (str): The deprecated identifier or function name.
            new_name (str): The identifier or function name that should be used instead.
        """
        warnings.warn('%s is deprecated; use %s instead.' % (old_name, new_name), DeprecationWarning, stacklevel=2)

    def hess_api_user_sites_list_get(self, user_token, page, size, **kwargs):
        """
        Deprecated wrapper kept for backward compatibility; use `list_sites` instead.
        
        Parameters:
            user_token (str): Authentication token identifying the user.
            page (int): Page number for paginated results.
            size (int): Number of items per page.
            **kwargs: Transport-control or filter keyword arguments accepted by the API client.
        
        Returns:
            InlineResponse200: Paginated list of user sites.
        """
        self._deprecated('hess_api_user_sites_list_get', 'list_sites')
        return self.list_sites(user_token, page, size, **kwargs)

    def hess_api_device_site_id_list_get(self, user_token, site_id, page, size, **kwargs):
        """
        Deprecated wrapper that lists devices for a site and emits a DeprecationWarning.
        
        Parameters:
            user_token (str): Authentication token for the user.
            site_id (str|int): Identifier of the site whose devices are requested.
            page (int): Page number for paginated results (zero- or one-based as accepted by the API).
            size (int): Number of items per page.
        
        Returns:
            object: API response object containing the requested page of devices and pagination metadata.
        """
        self._deprecated('hess_api_device_site_id_list_get', 'list_devices')
        return self.list_devices(user_token, site_id, page, size, **kwargs)

    def hess_api_site_site_id_cur_powerflow_get(self, user_token, site_id, **kwargs):
        self._deprecated('hess_api_site_site_id_cur_powerflow_get', 'get_current_power_flow')
        return self.get_current_power_flow(user_token, site_id, **kwargs)

    def hess_api_device_device_id_real_electricity_get(self, user_token, device_id, **kwargs):
        """
        Deprecated wrapper that retrieves a device's real electricity generation or consumption data.
        
        Deprecated: retained for backwards compatibility and will emit a deprecation warning when called.
        
        Returns:
            The response object representing the device's real electricity generation or consumption data.
        """
        self._deprecated('hess_api_device_device_id_real_electricity_get', 'get_device_generation_or_consumption')
        return self.get_device_generation_or_consumption(user_token, device_id, **kwargs)

    def hess_api_site_site_id_overview_get(self, user_token, site_id, **kwargs):
        """
        Retrieve the generation overview for a site (deprecated alias).
        
        Note: this function is deprecated and delegates to get_site_generation_overview.
        
        Parameters:
            user_token (str): Authentication token for the user.
            site_id (str|int): Identifier of the site.
            **kwargs: Additional transport or query options forwarded to the underlying call.
        
        Returns:
            The site generation overview response object.
        """
        self._deprecated('hess_api_site_site_id_overview_get', 'get_site_generation_overview')
        return self.get_site_generation_overview(user_token, site_id, **kwargs)

    def hess_api_login_post(self, body, **kwargs):
        self._deprecated('hess_api_login_post', 'login')
        return self.login(body, **kwargs)
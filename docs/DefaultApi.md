# pylivoltek.DefaultApi

All URIs are relative to *https://api.livoltek-portal.com:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_details**](DefaultApi.md#get_device_details) | **GET** /hess/api/device/{siteId}/{serialNumber}/details | Device Details
[**get_energy_storage**](DefaultApi.md#get_energy_storage) | **GET** /hess/api/site/{siteId}/ESS | Energy Storage Information
[**get_recent_grid_import_export**](DefaultApi.md#get_recent_grid_import_export) | **GET** /hess/api/site/{siteId}/reissueUtilityEnergy | Site historical grid import &amp; export in recent 3 days
[**get_site_utility_energy**](DefaultApi.md#get_site_utility_energy) | **GET** /hess/api/site/{siteId}/utilityEnergy | Site historical grid import &amp; export in recent 2 years
[**hess_api_device_device_id_real_electricity_get**](DefaultApi.md#hess_api_device_device_id_real_electricity_get) | **GET** /hess/api/device/{deviceId}/realElectricity | Device Generation or Consumption
[**hess_api_device_site_id_list_get**](DefaultApi.md#hess_api_device_site_id_list_get) | **GET** /hess/api/device/{siteId}/list | Device List
[**hess_api_login_post**](DefaultApi.md#hess_api_login_post) | **POST** /hess/api/login | API User Login and Get Token
[**hess_api_site_site_id_cur_powerflow_get**](DefaultApi.md#hess_api_site_site_id_cur_powerflow_get) | **GET** /hess/api/site/{siteId}/curPowerflow | Current Power Flow
[**hess_api_site_site_id_overview_get**](DefaultApi.md#hess_api_site_site_id_overview_get) | **GET** /hess/api/site/{siteId}/overview | Site Generation Overview
[**hess_api_user_sites_list_get**](DefaultApi.md#hess_api_user_sites_list_get) | **GET** /hess/api/userSites/list | Site List

# **get_device_details**
> InlineResponse2005 get_device_details(user_token, site_id, serial_number, user_type=user_type)

Device Details

Query the equipment information of the specified device to obtain the device model, SN, working condition (offline, normal, fault, etc.) and its update time, firmware version, device type and manufacturer.

### Example
```python
from __future__ import print_function
import time
import pylivoltek
from pylivoltek.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pylivoltek.DefaultApi(pylivoltek.ApiClient(configuration))
user_token = NULL # object | User token
site_id = NULL # object | Site ID
serial_number = NULL # object | Site ID
user_type = NULL # object | User Type (optional)

try:
    # Device Details
    api_response = api_instance.get_device_details(user_token, site_id, serial_number, user_type=user_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | [**object**](.md)| User token | 
 **site_id** | [**object**](.md)| Site ID | 
 **serial_number** | [**object**](.md)| Site ID | 
 **user_type** | [**object**](.md)| User Type | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_energy_storage**
> InlineResponse2007 get_energy_storage(user_token, site_id, user_type=user_type)

Energy Storage Information

Query the information of the energy storage battery within the specified site to obtain the BAT capacity, BMS SN, current SOC/voltage, battery type, and power / voltage / SOC in recent 7 days, and daily charge and discharge capacity in the last 7 days.

### Example
```python
from __future__ import print_function
import time
import pylivoltek
from pylivoltek.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pylivoltek.DefaultApi(pylivoltek.ApiClient(configuration))
user_token = NULL # object | User token
site_id = NULL # object | Site ID
user_type = NULL # object | User Type (optional)

try:
    # Energy Storage Information
    api_response = api_instance.get_energy_storage(user_token, site_id, user_type=user_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_energy_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | [**object**](.md)| User token | 
 **site_id** | [**object**](.md)| Site ID | 
 **user_type** | [**object**](.md)| User Type | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recent_grid_import_export**
> InlineResponse2009 get_recent_grid_import_export(site_id, user_token, user_type=user_type)

Site historical grid import & export in recent 3 days

Query the power grid electricity in the past three days of the specified power station (Wh).

### Example
```python
from __future__ import print_function
import time
import pylivoltek
from pylivoltek.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pylivoltek.DefaultApi(pylivoltek.ApiClient(configuration))
site_id = NULL # object | 
user_token = NULL # object | 
user_type = NULL # object |  (optional)

try:
    # Site historical grid import & export in recent 3 days
    api_response = api_instance.get_recent_grid_import_export(site_id, user_token, user_type=user_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_recent_grid_import_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**object**](.md)|  | 
 **user_token** | [**object**](.md)|  | 
 **user_type** | [**object**](.md)|  | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_utility_energy**
> InlineResponse2008 get_site_utility_energy(site_id, user_token, time_type, start_time, end_time, size, page, user_type=user_type)

Site historical grid import & export in recent 2 years

Query the historical grid energy, total solar generation, grid import, and export energy in the specified time period.

### Example
```python
from __future__ import print_function
import time
import pylivoltek
from pylivoltek.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pylivoltek.DefaultApi(pylivoltek.ApiClient(configuration))
site_id = NULL # object | 
user_token = NULL # object | 
time_type = NULL # object | 0: day; 1: week; 2: month; 3: year
start_time = NULL # object | 
end_time = NULL # object | 
size = NULL # object | 
page = NULL # object | 
user_type = NULL # object |  (optional)

try:
    # Site historical grid import & export in recent 2 years
    api_response = api_instance.get_site_utility_energy(site_id, user_token, time_type, start_time, end_time, size, page, user_type=user_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_site_utility_energy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**object**](.md)|  | 
 **user_token** | [**object**](.md)|  | 
 **time_type** | [**object**](.md)| 0: day; 1: week; 2: month; 3: year | 
 **start_time** | [**object**](.md)|  | 
 **end_time** | [**object**](.md)|  | 
 **size** | [**object**](.md)|  | 
 **page** | [**object**](.md)|  | 
 **user_type** | [**object**](.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hess_api_device_device_id_real_electricity_get**
> InlineResponse2003 hess_api_device_device_id_real_electricity_get(user_token, device_id, user_type=user_type)

Device Generation or Consumption

Return device lifetime generation or consumption

### Example
```python
from __future__ import print_function
import time
import pylivoltek
from pylivoltek.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pylivoltek.DefaultApi(pylivoltek.ApiClient(configuration))
user_token = NULL # object | User token
device_id = NULL # object | Device ID
user_type = NULL # object | User Type (optional)

try:
    # Device Generation or Consumption
    api_response = api_instance.hess_api_device_device_id_real_electricity_get(user_token, device_id, user_type=user_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hess_api_device_device_id_real_electricity_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | [**object**](.md)| User token | 
 **device_id** | [**object**](.md)| Device ID | 
 **user_type** | [**object**](.md)| User Type | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hess_api_device_site_id_list_get**
> InlineResponse2006 hess_api_device_site_id_list_get(user_token, site_id, page, size, user_type=user_type)

Device List

Return the number of equipment in the specified site, equipment ID, equipment type (inverter, charging pile, electricity meter, etc.), equipment model, equipment SN and equipment manufacturer

### Example
```python
from __future__ import print_function
import time
import pylivoltek
from pylivoltek.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pylivoltek.DefaultApi(pylivoltek.ApiClient(configuration))
user_token = NULL # object | User token
site_id = NULL # object | Site ID
page = NULL # object | The first device index to be returned in the results, default=1
size = NULL # object | Pagesize of each page
user_type = NULL # object | User Type (optional)

try:
    # Device List
    api_response = api_instance.hess_api_device_site_id_list_get(user_token, site_id, page, size, user_type=user_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hess_api_device_site_id_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | [**object**](.md)| User token | 
 **site_id** | [**object**](.md)| Site ID | 
 **page** | [**object**](.md)| The first device index to be returned in the results, default&#x3D;1 | 
 **size** | [**object**](.md)| Pagesize of each page | 
 **user_type** | [**object**](.md)| User Type | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hess_api_login_post**
> InlineResponse200 hess_api_login_post(body)

API User Login and Get Token

Get api user token and verify whether the API caller has permission

### Example
```python
from __future__ import print_function
import time
import pylivoltek
from pylivoltek.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pylivoltek.DefaultApi(pylivoltek.ApiClient(configuration))
body = pylivoltek.ApiLoginBody() # ApiLoginBody | 

try:
    # API User Login and Get Token
    api_response = api_instance.hess_api_login_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hess_api_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiLoginBody**](ApiLoginBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hess_api_site_site_id_cur_powerflow_get**
> InlineResponse2004 hess_api_site_site_id_cur_powerflow_get(user_token, site_id, user_type=user_type)

Current Power Flow

Query the current energy flow of the specified power station to obtain the last update time, status of each system type, parameter unit (W) and value

### Example
```python
from __future__ import print_function
import time
import pylivoltek
from pylivoltek.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pylivoltek.DefaultApi(pylivoltek.ApiClient(configuration))
user_token = NULL # object | User token
site_id = NULL # object | Site ID
user_type = NULL # object | User Type (optional)

try:
    # Current Power Flow
    api_response = api_instance.hess_api_site_site_id_cur_powerflow_get(user_token, site_id, user_type=user_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hess_api_site_site_id_cur_powerflow_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | [**object**](.md)| User token | 
 **site_id** | [**object**](.md)| Site ID | 
 **user_type** | [**object**](.md)| User Type | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hess_api_site_site_id_overview_get**
> InlineResponse2002 hess_api_site_site_id_overview_get(user_token, site_id, user_type=user_type)

Site Generation Overview

Return generation review of selected site, including site name，amount of online equipment, latest updated timestamp, power, daily generation, monthly generation, yearly generation, lifetime generation

### Example
```python
from __future__ import print_function
import time
import pylivoltek
from pylivoltek.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pylivoltek.DefaultApi(pylivoltek.ApiClient(configuration))
user_token = NULL # object | User token
site_id = NULL # object | Site ID
user_type = NULL # object | User Type (optional)

try:
    # Site Generation Overview
    api_response = api_instance.hess_api_site_site_id_overview_get(user_token, site_id, user_type=user_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hess_api_site_site_id_overview_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | [**object**](.md)| User token | 
 **site_id** | [**object**](.md)| Site ID | 
 **user_type** | [**object**](.md)| User Type | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hess_api_user_sites_list_get**
> InlineResponse2001 hess_api_user_sites_list_get(user_token, page, size, user_type=user_type, power_station_type=power_station_type)

Site List

Returns a list of sites related to the given token, which is the account api_key. This API accepts parameters for convenient search, sort and pagination.Limit: Only support to 2 searh text at once; Only support to 1 sort text at once

### Example
```python
from __future__ import print_function
import time
import pylivoltek
from pylivoltek.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pylivoltek.DefaultApi(pylivoltek.ApiClient(configuration))
user_token = NULL # object | User token
page = NULL # object | The first site index to be returned in the results
size = NULL # object | Pagesize of each page: - 5 - 10 - 30
user_type = NULL # object | User Type (optional)
power_station_type = NULL # object | Power Station Type: 1 - Grid-tied solar system 2 - Solar storage system 3 - EV charging hub 4 - EV charging hub with solar storage (optional)

try:
    # Site List
    api_response = api_instance.hess_api_user_sites_list_get(user_token, page, size, user_type=user_type, power_station_type=power_station_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hess_api_user_sites_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | [**object**](.md)| User token | 
 **page** | [**object**](.md)| The first site index to be returned in the results | 
 **size** | [**object**](.md)| Pagesize of each page: - 5 - 10 - 30 | 
 **user_type** | [**object**](.md)| User Type | [optional] 
 **power_station_type** | [**object**](.md)| Power Station Type: 1 - Grid-tied solar system 2 - Solar storage system 3 - EV charging hub 4 - EV charging hub with solar storage | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


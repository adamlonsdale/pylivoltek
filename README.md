# pylivoltek
Python API Client for the Livoltek API

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

You can install directly from Github

```sh
pip install git+https://github.com/adamlonsdale/pylivoltek.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/adamlonsdale/pylivoltek.git`)

Then import the package:
```python
import pylivoltek 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pylivoltek
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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


# create an instance of the API class
api_instance = pylivoltek.DefaultApi(pylivoltek.ApiClient(configuration))
body = pylivoltek.ApiLoginBody() # ApiLoginBody | 

try:
    # API User Login and Get Token
    api_response = api_instance.hess_api_login_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hess_api_login_post: %s\n" % e)


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

## Documentation for API Endpoints

All URIs are relative to *https://api.livoltek-portal.com:8081*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**get_device_details**](docs/DefaultApi.md#get_device_details) | **GET** /hess/api/device/{siteId}/{serialNumber}/details | Device Details
*DefaultApi* | [**get_energy_storage**](docs/DefaultApi.md#get_energy_storage) | **GET** /hess/api/site/{siteId}/ESS | Energy Storage Information
*DefaultApi* | [**get_recent_grid_import_export**](docs/DefaultApi.md#get_recent_grid_import_export) | **GET** /hess/api/site/{siteId}/reissueUtilityEnergy | Site historical grid import &amp; export in recent 3 days
*DefaultApi* | [**get_site_utility_energy**](docs/DefaultApi.md#get_site_utility_energy) | **GET** /hess/api/site/{siteId}/utilityEnergy | Site historical grid import &amp; export in recent 2 years
*DefaultApi* | [**hess_api_device_device_id_real_electricity_get**](docs/DefaultApi.md#hess_api_device_device_id_real_electricity_get) | **GET** /hess/api/device/{deviceId}/realElectricity | Device Generation or Consumption
*DefaultApi* | [**hess_api_device_site_id_list_get**](docs/DefaultApi.md#hess_api_device_site_id_list_get) | **GET** /hess/api/device/{siteId}/list | Device List
*DefaultApi* | [**hess_api_login_post**](docs/DefaultApi.md#hess_api_login_post) | **POST** /hess/api/login | API User Login and Get Token
*DefaultApi* | [**hess_api_site_site_id_cur_powerflow_get**](docs/DefaultApi.md#hess_api_site_site_id_cur_powerflow_get) | **GET** /hess/api/site/{siteId}/curPowerflow | Current Power Flow
*DefaultApi* | [**hess_api_site_site_id_overview_get**](docs/DefaultApi.md#hess_api_site_site_id_overview_get) | **GET** /hess/api/site/{siteId}/overview | Site Generation Overview
*DefaultApi* | [**hess_api_user_sites_list_get**](docs/DefaultApi.md#hess_api_user_sites_list_get) | **GET** /hess/api/userSites/list | Site List

## Documentation For Models

 - [ApiLoginBody](docs/ApiLoginBody.md)
 - [CurrentPowerFlow](docs/CurrentPowerFlow.md)
 - [Device](docs/Device.md)
 - [DeviceDetails](docs/DeviceDetails.md)
 - [DeviceList](docs/DeviceList.md)
 - [EnergyStore](docs/EnergyStore.md)
 - [EnergyStoreBatteryType](docs/EnergyStoreBatteryType.md)
 - [EnergyStoreHistoryMap](docs/EnergyStoreHistoryMap.md)
 - [EnergyStoreHistoryMapItem](docs/EnergyStoreHistoryMapItem.md)
 - [HistoryItem](docs/HistoryItem.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2001Data](docs/InlineResponse2001Data.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2008Data](docs/InlineResponse2008Data.md)
 - [InlineResponse2008DataEtotalToGrid](docs/InlineResponse2008DataEtotalToGrid.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [RecentGridImportExport](docs/RecentGridImportExport.md)
 - [Site](docs/Site.md)
 - [SiteList](docs/SiteList.md)
 - [SiteOverview](docs/SiteOverview.md)

## Documentation For Authorization


## token



## Author



# coding: utf-8

"""
    Livoltek API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EnergyStoreBatteryType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'device_sn': 'object',
        'device_id': 'object',
        'battery_type': 'object'
    }

    attribute_map = {
        'device_sn': 'deviceSn',
        'device_id': 'deviceId',
        'battery_type': 'batteryType'
    }

    def __init__(self, device_sn=None, device_id=None, battery_type=None):  # noqa: E501
        """EnergyStoreBatteryType - a model defined in Swagger"""  # noqa: E501
        self._device_sn = None
        self._device_id = None
        self._battery_type = None
        self.discriminator = None
        if device_sn is not None:
            self.device_sn = device_sn
        if device_id is not None:
            self.device_id = device_id
        if battery_type is not None:
            self.battery_type = battery_type

    @property
    def device_sn(self):
        """Gets the device_sn of this EnergyStoreBatteryType.  # noqa: E501

        Device Serial Number  # noqa: E501

        :return: The device_sn of this EnergyStoreBatteryType.  # noqa: E501
        :rtype: object
        """
        return self._device_sn

    @device_sn.setter
    def device_sn(self, device_sn):
        """Sets the device_sn of this EnergyStoreBatteryType.

        Device Serial Number  # noqa: E501

        :param device_sn: The device_sn of this EnergyStoreBatteryType.  # noqa: E501
        :type: object
        """

        self._device_sn = device_sn

    @property
    def device_id(self):
        """Gets the device_id of this EnergyStoreBatteryType.  # noqa: E501

        Device ID  # noqa: E501

        :return: The device_id of this EnergyStoreBatteryType.  # noqa: E501
        :rtype: object
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this EnergyStoreBatteryType.

        Device ID  # noqa: E501

        :param device_id: The device_id of this EnergyStoreBatteryType.  # noqa: E501
        :type: object
        """

        self._device_id = device_id

    @property
    def battery_type(self):
        """Gets the battery_type of this EnergyStoreBatteryType.  # noqa: E501

        Battery Type  # noqa: E501

        :return: The battery_type of this EnergyStoreBatteryType.  # noqa: E501
        :rtype: object
        """
        return self._battery_type

    @battery_type.setter
    def battery_type(self, battery_type):
        """Sets the battery_type of this EnergyStoreBatteryType.

        Battery Type  # noqa: E501

        :param battery_type: The battery_type of this EnergyStoreBatteryType.  # noqa: E501
        :type: object
        """

        self._battery_type = battery_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EnergyStoreBatteryType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EnergyStoreBatteryType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

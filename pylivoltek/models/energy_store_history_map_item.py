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

class EnergyStoreHistoryMapItem(object):
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
        'energy_power': 'object',
        'energy_soc': 'object',
        'energy_voltage': 'object',
        'charge': 'object',
        'discharge': 'object',
        'time': 'object'
    }

    attribute_map = {
        'energy_power': 'energyPower',
        'energy_soc': 'energySoc',
        'energy_voltage': 'energyVoltage',
        'charge': 'charge',
        'discharge': 'discharge',
        'time': 'time'
    }

    def __init__(self, energy_power=None, energy_soc=None, energy_voltage=None, charge=None, discharge=None, time=None):  # noqa: E501
        """EnergyStoreHistoryMapItem - a model defined in Swagger"""  # noqa: E501
        self._energy_power = None
        self._energy_soc = None
        self._energy_voltage = None
        self._charge = None
        self._discharge = None
        self._time = None
        self.discriminator = None
        if energy_power is not None:
            self.energy_power = energy_power
        if energy_soc is not None:
            self.energy_soc = energy_soc
        if energy_voltage is not None:
            self.energy_voltage = energy_voltage
        if charge is not None:
            self.charge = charge
        if discharge is not None:
            self.discharge = discharge
        if time is not None:
            self.time = time

    @property
    def energy_power(self):
        """Gets the energy_power of this EnergyStoreHistoryMapItem.  # noqa: E501

        Battery power  # noqa: E501

        :return: The energy_power of this EnergyStoreHistoryMapItem.  # noqa: E501
        :rtype: object
        """
        return self._energy_power

    @energy_power.setter
    def energy_power(self, energy_power):
        """Sets the energy_power of this EnergyStoreHistoryMapItem.

        Battery power  # noqa: E501

        :param energy_power: The energy_power of this EnergyStoreHistoryMapItem.  # noqa: E501
        :type: object
        """

        self._energy_power = energy_power

    @property
    def energy_soc(self):
        """Gets the energy_soc of this EnergyStoreHistoryMapItem.  # noqa: E501

        Battery SoC  # noqa: E501

        :return: The energy_soc of this EnergyStoreHistoryMapItem.  # noqa: E501
        :rtype: object
        """
        return self._energy_soc

    @energy_soc.setter
    def energy_soc(self, energy_soc):
        """Sets the energy_soc of this EnergyStoreHistoryMapItem.

        Battery SoC  # noqa: E501

        :param energy_soc: The energy_soc of this EnergyStoreHistoryMapItem.  # noqa: E501
        :type: object
        """

        self._energy_soc = energy_soc

    @property
    def energy_voltage(self):
        """Gets the energy_voltage of this EnergyStoreHistoryMapItem.  # noqa: E501

        Battery voltage  # noqa: E501

        :return: The energy_voltage of this EnergyStoreHistoryMapItem.  # noqa: E501
        :rtype: object
        """
        return self._energy_voltage

    @energy_voltage.setter
    def energy_voltage(self, energy_voltage):
        """Sets the energy_voltage of this EnergyStoreHistoryMapItem.

        Battery voltage  # noqa: E501

        :param energy_voltage: The energy_voltage of this EnergyStoreHistoryMapItem.  # noqa: E501
        :type: object
        """

        self._energy_voltage = energy_voltage

    @property
    def charge(self):
        """Gets the charge of this EnergyStoreHistoryMapItem.  # noqa: E501

        Charging energy  # noqa: E501

        :return: The charge of this EnergyStoreHistoryMapItem.  # noqa: E501
        :rtype: object
        """
        return self._charge

    @charge.setter
    def charge(self, charge):
        """Sets the charge of this EnergyStoreHistoryMapItem.

        Charging energy  # noqa: E501

        :param charge: The charge of this EnergyStoreHistoryMapItem.  # noqa: E501
        :type: object
        """

        self._charge = charge

    @property
    def discharge(self):
        """Gets the discharge of this EnergyStoreHistoryMapItem.  # noqa: E501

        Discharging energy  # noqa: E501

        :return: The discharge of this EnergyStoreHistoryMapItem.  # noqa: E501
        :rtype: object
        """
        return self._discharge

    @discharge.setter
    def discharge(self, discharge):
        """Sets the discharge of this EnergyStoreHistoryMapItem.

        Discharging energy  # noqa: E501

        :param discharge: The discharge of this EnergyStoreHistoryMapItem.  # noqa: E501
        :type: object
        """

        self._discharge = discharge

    @property
    def time(self):
        """Gets the time of this EnergyStoreHistoryMapItem.  # noqa: E501

        Timestamp (ms)  # noqa: E501

        :return: The time of this EnergyStoreHistoryMapItem.  # noqa: E501
        :rtype: object
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this EnergyStoreHistoryMapItem.

        Timestamp (ms)  # noqa: E501

        :param time: The time of this EnergyStoreHistoryMapItem.  # noqa: E501
        :type: object
        """

        self._time = time

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
        if issubclass(EnergyStoreHistoryMapItem, dict):
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
        if not isinstance(other, EnergyStoreHistoryMapItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

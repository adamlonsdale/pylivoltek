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

class CurrentPowerFlow(object):
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
        'energy_status': 'object',
        'energy_power': 'object',
        'energy_soc': 'object',
        'pv_status': 'object',
        'pv_power': 'object',
        'power_grid_status': 'object',
        'power_grid_power': 'object',
        'load_status': 'object',
        'load_power': 'object',
        'charging_pile_status': 'object',
        'charging_pile_power': 'object',
        'timestamp': 'object'
    }

    attribute_map = {
        'energy_status': 'energyStatus',
        'energy_power': 'energyPower',
        'energy_soc': 'energySoc',
        'pv_status': 'pvStatus',
        'pv_power': 'pvPower',
        'power_grid_status': 'powerGridStatus',
        'power_grid_power': 'powerGridPower',
        'load_status': 'loadStatus',
        'load_power': 'loadPower',
        'charging_pile_status': 'chargingPileStatus',
        'charging_pile_power': 'chargingPilePower',
        'timestamp': 'timestamp'
    }

    def __init__(self, energy_status=None, energy_power=None, energy_soc=None, pv_status=None, pv_power=None, power_grid_status=None, power_grid_power=None, load_status=None, load_power=None, charging_pile_status=None, charging_pile_power=None, timestamp=None):  # noqa: E501
        """CurrentPowerFlow - a model defined in Swagger"""  # noqa: E501
        self._energy_status = None
        self._energy_power = None
        self._energy_soc = None
        self._pv_status = None
        self._pv_power = None
        self._power_grid_status = None
        self._power_grid_power = None
        self._load_status = None
        self._load_power = None
        self._charging_pile_status = None
        self._charging_pile_power = None
        self._timestamp = None
        self.discriminator = None
        if energy_status is not None:
            self.energy_status = energy_status
        if energy_power is not None:
            self.energy_power = energy_power
        if energy_soc is not None:
            self.energy_soc = energy_soc
        if pv_status is not None:
            self.pv_status = pv_status
        if pv_power is not None:
            self.pv_power = pv_power
        if power_grid_status is not None:
            self.power_grid_status = power_grid_status
        if power_grid_power is not None:
            self.power_grid_power = power_grid_power
        if load_status is not None:
            self.load_status = load_status
        if load_power is not None:
            self.load_power = load_power
        if charging_pile_status is not None:
            self.charging_pile_status = charging_pile_status
        if charging_pile_power is not None:
            self.charging_pile_power = charging_pile_power
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def energy_status(self):
        """Gets the energy_status of this CurrentPowerFlow.  # noqa: E501

        Battery working status  # noqa: E501

        :return: The energy_status of this CurrentPowerFlow.  # noqa: E501
        :rtype: object
        """
        return self._energy_status

    @energy_status.setter
    def energy_status(self, energy_status):
        """Sets the energy_status of this CurrentPowerFlow.

        Battery working status  # noqa: E501

        :param energy_status: The energy_status of this CurrentPowerFlow.  # noqa: E501
        :type: object
        """

        self._energy_status = energy_status

    @property
    def energy_power(self):
        """Gets the energy_power of this CurrentPowerFlow.  # noqa: E501

        Battery working power  # noqa: E501

        :return: The energy_power of this CurrentPowerFlow.  # noqa: E501
        :rtype: object
        """
        return self._energy_power

    @energy_power.setter
    def energy_power(self, energy_power):
        """Sets the energy_power of this CurrentPowerFlow.

        Battery working power  # noqa: E501

        :param energy_power: The energy_power of this CurrentPowerFlow.  # noqa: E501
        :type: object
        """

        self._energy_power = energy_power

    @property
    def energy_soc(self):
        """Gets the energy_soc of this CurrentPowerFlow.  # noqa: E501

        Battery SoC  # noqa: E501

        :return: The energy_soc of this CurrentPowerFlow.  # noqa: E501
        :rtype: object
        """
        return self._energy_soc

    @energy_soc.setter
    def energy_soc(self, energy_soc):
        """Sets the energy_soc of this CurrentPowerFlow.

        Battery SoC  # noqa: E501

        :param energy_soc: The energy_soc of this CurrentPowerFlow.  # noqa: E501
        :type: object
        """

        self._energy_soc = energy_soc

    @property
    def pv_status(self):
        """Gets the pv_status of this CurrentPowerFlow.  # noqa: E501

        PV working status  # noqa: E501

        :return: The pv_status of this CurrentPowerFlow.  # noqa: E501
        :rtype: object
        """
        return self._pv_status

    @pv_status.setter
    def pv_status(self, pv_status):
        """Sets the pv_status of this CurrentPowerFlow.

        PV working status  # noqa: E501

        :param pv_status: The pv_status of this CurrentPowerFlow.  # noqa: E501
        :type: object
        """

        self._pv_status = pv_status

    @property
    def pv_power(self):
        """Gets the pv_power of this CurrentPowerFlow.  # noqa: E501

        PV generating power  # noqa: E501

        :return: The pv_power of this CurrentPowerFlow.  # noqa: E501
        :rtype: object
        """
        return self._pv_power

    @pv_power.setter
    def pv_power(self, pv_power):
        """Sets the pv_power of this CurrentPowerFlow.

        PV generating power  # noqa: E501

        :param pv_power: The pv_power of this CurrentPowerFlow.  # noqa: E501
        :type: object
        """

        self._pv_power = pv_power

    @property
    def power_grid_status(self):
        """Gets the power_grid_status of this CurrentPowerFlow.  # noqa: E501

        Power grid working status  # noqa: E501

        :return: The power_grid_status of this CurrentPowerFlow.  # noqa: E501
        :rtype: object
        """
        return self._power_grid_status

    @power_grid_status.setter
    def power_grid_status(self, power_grid_status):
        """Sets the power_grid_status of this CurrentPowerFlow.

        Power grid working status  # noqa: E501

        :param power_grid_status: The power_grid_status of this CurrentPowerFlow.  # noqa: E501
        :type: object
        """

        self._power_grid_status = power_grid_status

    @property
    def power_grid_power(self):
        """Gets the power_grid_power of this CurrentPowerFlow.  # noqa: E501

        Power grid working power  # noqa: E501

        :return: The power_grid_power of this CurrentPowerFlow.  # noqa: E501
        :rtype: object
        """
        return self._power_grid_power

    @power_grid_power.setter
    def power_grid_power(self, power_grid_power):
        """Sets the power_grid_power of this CurrentPowerFlow.

        Power grid working power  # noqa: E501

        :param power_grid_power: The power_grid_power of this CurrentPowerFlow.  # noqa: E501
        :type: object
        """

        self._power_grid_power = power_grid_power

    @property
    def load_status(self):
        """Gets the load_status of this CurrentPowerFlow.  # noqa: E501

        Load working status  # noqa: E501

        :return: The load_status of this CurrentPowerFlow.  # noqa: E501
        :rtype: object
        """
        return self._load_status

    @load_status.setter
    def load_status(self, load_status):
        """Sets the load_status of this CurrentPowerFlow.

        Load working status  # noqa: E501

        :param load_status: The load_status of this CurrentPowerFlow.  # noqa: E501
        :type: object
        """

        self._load_status = load_status

    @property
    def load_power(self):
        """Gets the load_power of this CurrentPowerFlow.  # noqa: E501

        Load consuming power  # noqa: E501

        :return: The load_power of this CurrentPowerFlow.  # noqa: E501
        :rtype: object
        """
        return self._load_power

    @load_power.setter
    def load_power(self, load_power):
        """Sets the load_power of this CurrentPowerFlow.

        Load consuming power  # noqa: E501

        :param load_power: The load_power of this CurrentPowerFlow.  # noqa: E501
        :type: object
        """

        self._load_power = load_power

    @property
    def charging_pile_status(self):
        """Gets the charging_pile_status of this CurrentPowerFlow.  # noqa: E501

        EV charger working status  # noqa: E501

        :return: The charging_pile_status of this CurrentPowerFlow.  # noqa: E501
        :rtype: object
        """
        return self._charging_pile_status

    @charging_pile_status.setter
    def charging_pile_status(self, charging_pile_status):
        """Sets the charging_pile_status of this CurrentPowerFlow.

        EV charger working status  # noqa: E501

        :param charging_pile_status: The charging_pile_status of this CurrentPowerFlow.  # noqa: E501
        :type: object
        """

        self._charging_pile_status = charging_pile_status

    @property
    def charging_pile_power(self):
        """Gets the charging_pile_power of this CurrentPowerFlow.  # noqa: E501

        EV charger charging power  # noqa: E501

        :return: The charging_pile_power of this CurrentPowerFlow.  # noqa: E501
        :rtype: object
        """
        return self._charging_pile_power

    @charging_pile_power.setter
    def charging_pile_power(self, charging_pile_power):
        """Sets the charging_pile_power of this CurrentPowerFlow.

        EV charger charging power  # noqa: E501

        :param charging_pile_power: The charging_pile_power of this CurrentPowerFlow.  # noqa: E501
        :type: object
        """

        self._charging_pile_power = charging_pile_power

    @property
    def timestamp(self):
        """Gets the timestamp of this CurrentPowerFlow.  # noqa: E501

        Latest data update time  # noqa: E501

        :return: The timestamp of this CurrentPowerFlow.  # noqa: E501
        :rtype: object
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CurrentPowerFlow.

        Latest data update time  # noqa: E501

        :param timestamp: The timestamp of this CurrentPowerFlow.  # noqa: E501
        :type: object
        """

        self._timestamp = timestamp

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
        if issubclass(CurrentPowerFlow, dict):
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
        if not isinstance(other, CurrentPowerFlow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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

class InlineResponse2003(object):
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
        'pv_produce_electric': 'object',
        'load_customer_electric': 'object',
        'timestamp': 'object',
        'code': 'object',
        'message': 'object'
    }

    attribute_map = {
        'pv_produce_electric': 'pvProduceElectric',
        'load_customer_electric': 'loadCustomerElectric',
        'timestamp': 'timestamp',
        'code': 'code',
        'message': 'message'
    }

    def __init__(self, pv_produce_electric=None, load_customer_electric=None, timestamp=None, code=None, message=None):  # noqa: E501
        """InlineResponse2003 - a model defined in Swagger"""  # noqa: E501
        self._pv_produce_electric = None
        self._load_customer_electric = None
        self._timestamp = None
        self._code = None
        self._message = None
        self.discriminator = None
        if pv_produce_electric is not None:
            self.pv_produce_electric = pv_produce_electric
        if load_customer_electric is not None:
            self.load_customer_electric = load_customer_electric
        if timestamp is not None:
            self.timestamp = timestamp
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message

    @property
    def pv_produce_electric(self):
        """Gets the pv_produce_electric of this InlineResponse2003.  # noqa: E501

        Inver solar generation  # noqa: E501

        :return: The pv_produce_electric of this InlineResponse2003.  # noqa: E501
        :rtype: object
        """
        return self._pv_produce_electric

    @pv_produce_electric.setter
    def pv_produce_electric(self, pv_produce_electric):
        """Sets the pv_produce_electric of this InlineResponse2003.

        Inver solar generation  # noqa: E501

        :param pv_produce_electric: The pv_produce_electric of this InlineResponse2003.  # noqa: E501
        :type: object
        """

        self._pv_produce_electric = pv_produce_electric

    @property
    def load_customer_electric(self):
        """Gets the load_customer_electric of this InlineResponse2003.  # noqa: E501

        load consumptions (only when there is RS485 meter connected to inverter)  # noqa: E501

        :return: The load_customer_electric of this InlineResponse2003.  # noqa: E501
        :rtype: object
        """
        return self._load_customer_electric

    @load_customer_electric.setter
    def load_customer_electric(self, load_customer_electric):
        """Sets the load_customer_electric of this InlineResponse2003.

        load consumptions (only when there is RS485 meter connected to inverter)  # noqa: E501

        :param load_customer_electric: The load_customer_electric of this InlineResponse2003.  # noqa: E501
        :type: object
        """

        self._load_customer_electric = load_customer_electric

    @property
    def timestamp(self):
        """Gets the timestamp of this InlineResponse2003.  # noqa: E501

        Latest data update time  # noqa: E501

        :return: The timestamp of this InlineResponse2003.  # noqa: E501
        :rtype: object
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this InlineResponse2003.

        Latest data update time  # noqa: E501

        :param timestamp: The timestamp of this InlineResponse2003.  # noqa: E501
        :type: object
        """

        self._timestamp = timestamp

    @property
    def code(self):
        """Gets the code of this InlineResponse2003.  # noqa: E501

        http/https response code  # noqa: E501

        :return: The code of this InlineResponse2003.  # noqa: E501
        :rtype: object
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InlineResponse2003.

        http/https response code  # noqa: E501

        :param code: The code of this InlineResponse2003.  # noqa: E501
        :type: object
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this InlineResponse2003.  # noqa: E501

        Message code  # noqa: E501

        :return: The message of this InlineResponse2003.  # noqa: E501
        :rtype: object
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse2003.

        Message code  # noqa: E501

        :param message: The message of this InlineResponse2003.  # noqa: E501
        :type: object
        """

        self._message = message

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
        if issubclass(InlineResponse2003, dict):
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
        if not isinstance(other, InlineResponse2003):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
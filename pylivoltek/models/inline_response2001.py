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

class InlineResponse2001(object):
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
        'code': 'object',
        'message': 'object',
        'data': 'InlineResponse2001Data'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'data': 'data'
    }

    def __init__(self, code=None, message=None, data=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._message = None
        self._data = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if data is not None:
            self.data = data

    @property
    def code(self):
        """Gets the code of this InlineResponse2001.  # noqa: E501

        Message Code  # noqa: E501

        :return: The code of this InlineResponse2001.  # noqa: E501
        :rtype: object
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InlineResponse2001.

        Message Code  # noqa: E501

        :param code: The code of this InlineResponse2001.  # noqa: E501
        :type: object
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this InlineResponse2001.  # noqa: E501

        HTTP/HTTPS response code  # noqa: E501

        :return: The message of this InlineResponse2001.  # noqa: E501
        :rtype: object
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse2001.

        HTTP/HTTPS response code  # noqa: E501

        :param message: The message of this InlineResponse2001.  # noqa: E501
        :type: object
        """

        self._message = message

    @property
    def data(self):
        """Gets the data of this InlineResponse2001.  # noqa: E501


        :return: The data of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001Data
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse2001.


        :param data: The data of this InlineResponse2001.  # noqa: E501
        :type: InlineResponse2001Data
        """

        self._data = data

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
        if issubclass(InlineResponse2001, dict):
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
        if not isinstance(other, InlineResponse2001):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
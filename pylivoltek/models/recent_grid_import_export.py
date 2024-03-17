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

class RecentGridImportExport(object):
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
        'site_id': 'object',
        'ts': 'object',
        'positive': 'object',
        'negative': 'object'
    }

    attribute_map = {
        'site_id': 'siteId',
        'ts': 'ts',
        'positive': 'positive',
        'negative': 'negative'
    }

    def __init__(self, site_id=None, ts=None, positive=None, negative=None):  # noqa: E501
        """RecentGridImportExport - a model defined in Swagger"""  # noqa: E501
        self._site_id = None
        self._ts = None
        self._positive = None
        self._negative = None
        self.discriminator = None
        if site_id is not None:
            self.site_id = site_id
        if ts is not None:
            self.ts = ts
        if positive is not None:
            self.positive = positive
        if negative is not None:
            self.negative = negative

    @property
    def site_id(self):
        """Gets the site_id of this RecentGridImportExport.  # noqa: E501

        Site ID  # noqa: E501

        :return: The site_id of this RecentGridImportExport.  # noqa: E501
        :rtype: object
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this RecentGridImportExport.

        Site ID  # noqa: E501

        :param site_id: The site_id of this RecentGridImportExport.  # noqa: E501
        :type: object
        """

        self._site_id = site_id

    @property
    def ts(self):
        """Gets the ts of this RecentGridImportExport.  # noqa: E501

        Time Stamp  # noqa: E501

        :return: The ts of this RecentGridImportExport.  # noqa: E501
        :rtype: object
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """Sets the ts of this RecentGridImportExport.

        Time Stamp  # noqa: E501

        :param ts: The ts of this RecentGridImportExport.  # noqa: E501
        :type: object
        """

        self._ts = ts

    @property
    def positive(self):
        """Gets the positive of this RecentGridImportExport.  # noqa: E501

        Grid Imported Energy (kWh)  # noqa: E501

        :return: The positive of this RecentGridImportExport.  # noqa: E501
        :rtype: object
        """
        return self._positive

    @positive.setter
    def positive(self, positive):
        """Sets the positive of this RecentGridImportExport.

        Grid Imported Energy (kWh)  # noqa: E501

        :param positive: The positive of this RecentGridImportExport.  # noqa: E501
        :type: object
        """

        self._positive = positive

    @property
    def negative(self):
        """Gets the negative of this RecentGridImportExport.  # noqa: E501

        Grid Exported Energy (kWh)  # noqa: E501

        :return: The negative of this RecentGridImportExport.  # noqa: E501
        :rtype: object
        """
        return self._negative

    @negative.setter
    def negative(self, negative):
        """Sets the negative of this RecentGridImportExport.

        Grid Exported Energy (kWh)  # noqa: E501

        :param negative: The negative of this RecentGridImportExport.  # noqa: E501
        :type: object
        """

        self._negative = negative

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
        if issubclass(RecentGridImportExport, dict):
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
        if not isinstance(other, RecentGridImportExport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
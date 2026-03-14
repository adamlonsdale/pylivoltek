# coding: utf-8

"""
    Livoltek API
"""

import pprint
import re  # noqa: F401

import six


class InlineResponse2005Data(object):
    swagger_types = {
        'count': 'object',
        'list': 'DeviceDetails'
    }

    attribute_map = {
        'count': 'count',
        'list': 'list'
    }

    def __init__(self, count=None, list=None):  # noqa: A002
        self._count = None
        self._list = None
        self.discriminator = None
        if count is not None:
            self.count = count
        if list is not None:
            self.list = list

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        self._count = count

    @property
    def list(self):  # noqa: A003
        return self._list

    @list.setter
    def list(self, list):  # noqa: A002,A003
        self._list = list

    def to_dict(self):
        result = {}
        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if hasattr(value, 'to_dict'):
                result[attr] = value.to_dict()
            else:
                result[attr] = value
        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        return isinstance(other, InlineResponse2005Data) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

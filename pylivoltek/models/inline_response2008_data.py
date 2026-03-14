# coding: utf-8

"""
    Livoltek API
"""

import pprint
import re  # noqa: F401

import six


class InlineResponse2008Data(object):
    swagger_types = {
        'history_list': 'object',
        'etotal_to_grid': 'InlineResponse2008DataEtotalToGrid'
    }

    attribute_map = {
        'history_list': 'historyList',
        'etotal_to_grid': 'etotalToGrid'
    }

    def __init__(self, history_list=None, etotal_to_grid=None):
        self._history_list = None
        self._etotal_to_grid = None
        self.discriminator = None
        if history_list is not None:
            self.history_list = history_list
        if etotal_to_grid is not None:
            self.etotal_to_grid = etotal_to_grid

    @property
    def history_list(self):
        return self._history_list

    @history_list.setter
    def history_list(self, history_list):
        self._history_list = history_list

    @property
    def etotal_to_grid(self):
        return self._etotal_to_grid

    @etotal_to_grid.setter
    def etotal_to_grid(self, etotal_to_grid):
        self._etotal_to_grid = etotal_to_grid

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
        return isinstance(other, InlineResponse2008Data) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

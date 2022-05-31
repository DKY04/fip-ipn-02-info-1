# -*- coding: utf-8 -*-
"""
@author : david.yama-yama

Description

"""

from juice import JuiceSize


class Card:
    _obj_counter = 0

    def __init__(self):
        self._num = self._obj_counter
        Card._obj_counter += 1
        self._selected_juices = []

    @property
    def num(self):
        return self._num

    @property
    def selected_juices(self):
        return self._selected_juices

    def add_juice(self, juice):
        if not isinstance(juice, JuiceSize):
            raise TypeError('jsize type must be an instance of JuiceSize')
        self._selected_juices.append(juice)

    def delete_juice(self, index):
        self._selected_juices.pop(index)

# -*- coding: utf-8 -*-
"""
@author : david.yama-yama

Description

"""

from juice import Juice


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
        """ Get list of user selected juices which are in stock """
        return self._selected_juices

    def add_juice(self, juice):
        if not isinstance(juice, Juice):
            raise TypeError('jsize type must be an instance of JuiceSize')
        self._selected_juices.append(juice)

    def delete_juice(self, index):
        if len(self._selected_juices) >= index:
            return False
        else:
            self._selected_juices.pop(index)
            return True

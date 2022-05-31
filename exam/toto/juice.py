# -*- coding: utf-8 -*-
"""
@author : david.yama-yama

Description

"""

from enum import Enum


def _juice_type_to_price(jtype):
    """ Convert JuiceType to a price in dollars """
    if jtype == JuiceType.Boost:
        return 5
    elif jtype == JuiceType.Fresh:
        return 4
    elif jtype == JuiceType.Fusion:
        return 5
    elif jtype == JuiceType.Detox:
        return 3.5


def _juice_size_to_offset_price(jsize):
    """ Convert offset price """
    if jsize == JuiceSize.Small:
        return 0.5
    elif jsize == JuiceSize.Medium:
        return 1
    elif jsize == JuiceSize.Large:
        return 1.5


class JuiceType(Enum):
    Boost = 1
    Fresh = 2
    Fusion = 3
    Detox = 4


class JuiceSize(Enum):
    Small = 1
    Medium = 2
    Large = 3


class Juice:
    _type = None
    _size = None

    def __init__(self, jtype, jsize):
        self._set_juice_type(jtype)
        self._set_juice_size(jsize)
        self._base_price = _juice_type_to_price(self._type)

    @property
    def type(self):
        """ Get juice type """
        return self._type

    @property
    def size(self):
        """ Get juice size """
        return self._size

    @property
    def price(self):
        return self._base_price + _juice_size_to_offset_price(self._size)

    # ## PRIVATES ##
    # --------------
    def _set_juice_type(self, jtype):
        if not isinstance(jtype, JuiceType):
            raise TypeError('jtype type must be an instance of JuiceType')
        self._type = jtype

    def _set_juice_size(self, jsize):
        if not isinstance(jsize, JuiceSize):
            raise TypeError('jsize type must be an instance of JuiceSize')
        self._size = jsize
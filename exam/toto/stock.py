# -*- coding: utf-8 -*-
"""
@author : david.yama-yama

Description

"""
import itertools
import random
from juice import JuiceType, JuiceSize, Juice


class Stock:
    _instance = None
    _products = []

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Stock, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def get_quantity(self, juice):
        count = 0
        for j in self._products:
            if j.type == juice.type:
                if j.size == j.size:
                    count += 1

        return count

    @property
    def products(self):
        return self._products

    def remove_products(self, jtype, qte):
        for i in range(qte):
            self._remove_product(jtype)

    # ## PRIVATES ##
    # --------------
    def _initialize(self):
        # Initialize 10 random products in stock
        combi = list(itertools.product([jtyte for jtyte in JuiceType], [jsize for jsize in JuiceSize]))
        self._products = [Juice(*random.choice(combi)) for _ in range(10)]
        x = 2

    def _remove_product(self, jtype):
        temp = map(lambda v: v.type, self._products)
        # TODO: reimplement
        for i, jt in enumerate(temp):
            if jtype == jt:
                self._products.pop(i)
                break

    def _add_juice(self, juice):
        self._products.append(juice)

    def add_juices(self, juices):
        for juice in juices:
            self._add_juice(juices)

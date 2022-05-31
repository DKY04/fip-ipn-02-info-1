# -*- coding: utf-8 -*-
"""
@author : david.yama-yama

Description

"""

from juice import Juice
from card import Card


class Barmaid:

    def __init__(self, stock):
        self._stock = stock
        self._card = Card()

    def add_juice_in_stock(self, juice):
        if not isinstance(juice, Juice):
            raise TypeError('juice type must be an instance of Juice')
        self._stock.append(juice)

    def add_juices_for_order(self, juices):
        for juice in juices:
            if self._stock.get_quantity() == 0:
                print("Juice not in stock ")
            else:
                self._card.add_juice(juice)

    def prepare(self):
        pass

    def prepare(self, juice):
        pass

    # ## PRIVATES


    # def _add_selected_juice_from_user(self, juice):
    #     if self._stock.get_quantity(juice.type) > 0:
    #         self._card.add_juice(juice)
    #     else:
    #         print(f"{Juice.type} not available in the stock")
    #

# -*- coding: utf-8 -*-
"""
@author : david.yama-yama

Description

"""
import time

from juice import Juice
from card import Card
from tabulate import tabulate


class Barmaid:

    def __init__(self, stock):
        self._stock = stock
        self._card = Card()
        self._orders_validate = False

    def add_juice_in_stock(self, juice):
        if not isinstance(juice, Juice):
            raise TypeError('juice type must be an instance of Juice')
        self._stock.append(juice)

    def add_juices_for_order(self, juices):
        for juice in juices:
            if self._stock.get_quantity(juice) == 0:
                print("Juice not in stock ")
            else:
                self._card.add_juice(juice)

    def _prepare(self):
        print("Preparing...")
        time.sleep(4000)
        print("finished !! ")

    def pay(self, value):
        total = self._get_total_order()

        rest = value - total
        if rest < 0:
            print(f"Unabled to complete order. Rest in charge {rest} euros")

        else:
            print("Order paid successfully")
            self._prepare()

    def display_invoce(self):
        l = [["JuiceType", "JuiceSize"]]
        for i, juice in enumerate(self._card.selected_juices):
            l.append([juice.type.name, juice.size.name, str(juice.price) + " €"])

        print()
        print(tabulate(l, headers="firstrow"))
        print(f"\ntotal = {self._get_total_order()} €\n\n")

    # ## PRIVATES
    def _get_total_order(self):
        return sum(map(lambda v: v.price, self._card.selected_juices))

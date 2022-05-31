# -*- coding: utf-8 -*-
"""
@author : david.yama-yama

Description

"""

from barmaid import Barmaid
from stock import Stock
from card import Card
from juice import *

from juice import *

if __name__ == '__main__':

    print('Select a Juice')
    user_selected_juices = []
    jtypes = list(map(lambda v : v.name, JuiceType))
    while True:
        jtype_name = input("Select type of juice :\n 1.{0}\t 2.{1}\t 3.{2}\t 4.{3} \n".format(*jtypes))
        if jtype_name in ("1", "2", "3", "4"):
            user_selected_juices.append(getattr(JuiceType, jtypes[int(jtype_name)]))
        else:
            print("Wrong type selection ! ")
    # stock = Stock()
    # barmaid = Barmaid(stock)
    # user_selected_juices = [Juice(JuiceType.Fresh, JuiceSize.Small), Juice(JuiceType.Fresh, JuiceSize.Large)]
    # barmaid.add_juices_for_order(user_selected_juices)
    # barmaid.prepare()
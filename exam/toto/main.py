# -*- coding: utf-8 -*-
"""
@author : david.yama-yama

Description

"""

from barmaid import Barmaid
from stock import Stock

from juice import *


def select(l_xtype, x_type):
    sjtype = "\n1.{0}\t 2.{1}\t 3.{2}\t 4.{3} \n ".format(*jtypes)
    sjsize = "\n1.{0}\t 2.{1}\t 3.{2} \n ".format(*jsizes)

    print("Enter juiceType and juiceSize separated by ',' ")
    usr_input = input(sjsize + "|" + sjtype)

    if usr_input.upper() == "Q":
        return "Quit"
    else:
        return True


if __name__ == '__main__':

    stock = Stock()
    barmaid = Barmaid(stock)

    print("Select type of juice (type 'Q' to if done) : ")
    user_selected_juices = []
    jtypes = list(map(lambda v: v.name, JuiceType))
    jsizes = list(map(lambda v: v.name, JuiceSize))
    while True:
        x = jtypes + jsizes
        toto = "\n1.{0}\t 2.{1}\t 3.{2}\t 4.{3} | 1.{4}\t 2.{5}\t 3.{6} \n ".format(*x)

        print("Enter juiceType and juiceSize separated by ',' ")
        usr_input = input(toto)

        v = usr_input.split(",")

        if usr_input.upper() == "Q":
            break
        jt = getattr(JuiceType, jtypes[int(v[0])])
        js = getattr(JuiceSize, jsizes[int(v[0])])
        juice = Juice(jt, js)
        user_selected_juices.append(juice)
        print(f"selected = {list(map(lambda v : str(v), user_selected_juices))}")

    print('\n################')
    print(user_selected_juices)
    barmaid.add_juices_for_order(user_selected_juices)
    a = input("confirm order (yes/no) ?")
    if a == "yes":
        barmaid.display_invoce()
        amount = int(input("Pay the incvoice : "))
        barmaid.pay(amount)
    else:
        print("Order canceled ! ")

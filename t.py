#!/usr/bin/env python
# -*-coding:utf-8-*-
# File Name     : t.py
# Description   :
# Author        :
# Creation Date : 2019-10-30
# Last Modified : Wed 30 Oct 2019 11:09:07 AM CST
# Created By    : lsl

def goodbye(name, adjective):
    print('Goodbye, %s, it was %s to meet you.' % (name, adjective))

import atexit
atexit.register(goodbye, 'Donny', 'nice')


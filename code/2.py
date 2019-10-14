#!/usr/bin/env python
# -*-coding:utf-8-*-
# File Name     : 2.py
# Description   :
# Author        :
# Creation Date : 2019-10-14
# Last Modified : Mon 14 Oct 2019 11:18:59 AM CST
# Created By    : lsl
import queue
from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)



q = queue.PriorityQueue()

q.put(2)
q.put(1)
q.put(3)
q.put(4)
q.put(7)
print(q.get())

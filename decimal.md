# decimal 
十进制定点和浮点运算




```

>>> a = 4.2
>>> b = 2.1
>>> a + b
6.300000000000001
>>> (a + b) == 6.3
False
>>>

```

解决

```

>>> from decimal import Decimal
>>> a = Decimal('4.2')
>>> b = Decimal('2.1')
>>> a + b
Decimal('6.3')
>>> print(a + b)
6.3
>>> (a + b) == Decimal('6.3')
True

```

## 总结

decimal 模块主要用在涉及到金融的领域



## 参考

https://python3-cookbook.readthedocs.io/zh_CN/latest/c03/p02_accurate_decimal_calculations.html

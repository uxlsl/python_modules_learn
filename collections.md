# collections 

+ ChainMap 快速从多个表进行查询
+ OrderedDict 
+ deque 提供双端队列进行操作




LRU例子
```

class LRU(OrderedDict):
    'Limit size, evicting the least recently looked-up key when full'

    def __init__(self, maxsize=128, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]

```


## 总结

ChainMap场景是有多个表，要查询.
Counter场景是统计健出现的次数.

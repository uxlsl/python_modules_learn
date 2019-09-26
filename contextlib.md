# contextlib
为with语句提供通用方法


with 要求object有这二个方法

```

object.__enter__
object.__exit__

```


+ contextlib.contextmanager 使用with的另一种方式，便捷!
+ contextlib.asynccontextmanager
+ contextlib.closing 关闭资源的另一种方式

例子

```

from contextlib import contextmanager

@contextmanager
def managed_resource(*args, **kwds):
    # Code to acquire resource, e.g.:
    resource = acquire_resource(*args, **kwds)
    try:
        yield resource
    finally:
        # Code to release resource, e.g.:
        release_resource(resource)

>>> with managed_resource(timeout=3600) as resource:
...     # Resource is released at the end of this block,
...     # even if code in the block raises an exception



```


## 总结
个人理解,一般情况下使用with,就是定义一个类，
类是有enter和exit,这样使用起来会比较复杂，
于是contextlib出来了，把定义变成使用函数.

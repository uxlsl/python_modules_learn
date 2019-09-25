# functools
主要是为高阶函数服务，通过包装函数或者返回新函数,实际上，任何可以调用的对象都可以使用这个模块


+ functools.cmp_to_key 在sorted使用
+ *functools.lru_cache* 缓存结果
+ functools.total_ordering 自动定义其他对比方法
+ *functools.partial*  修改函数默认参数
+ functools.partialmethod
+ functools.reduce
+ *functools.singledispatch* 多重函数
+ functools.update_wrapper
+ *functools.wraps* 装饰函数时，保存函数的信息 


```

__name__
__doc__

```


## 例子

functools.cmp_to_key

```python

sorted(iterable, key=cmp_to_key(locale.strcoll))  # locale-aware sort order

```

functools.lru_cache

```python

@lru_cache(maxsize=None)
def fib(n):
	if n < 2:
		return n
	return fib(n-1) + fib(n-2)

```

```

@total_ordering
class Student:
    def _is_valid_operand(self, other):
        return (hasattr(other, "lastname") and
                hasattr(other, "firstname"))
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))
```

functools.singledispatch

```python

from functools import singledispatch
@singledispatch
def fun(arg, verbose=False):
	if verbose:
		print("Let me just say,", end=" ")
	print(arg)

@fun.register
def _(arg int, verbose=False):
	if verbose:
		print("Strength is numbers, eh?", end= " ")
	print(arg)

```

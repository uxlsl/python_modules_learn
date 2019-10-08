# doctest
交互式测试python示例

这个好处是使用例子和源代码紧密地连接在一起

使用方法，在源代码编写类似python交互式的代码

test.py

```python
def fib(n):
	"""
	>>> fib(1)
	1

	>>> fib(2)
	2

	>>> fib(3)
	3

	"""
	if n < 1:
		return 1
	else:
		return f(n-1) + f(n-2)
```

python -m doctest -v test.py

## 总结
在编写代码，先使用例子，可以使编写目的更加明确!

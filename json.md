# json的解码和编码


## api
+ json.dumps
+ json.loads


## 例子

```python

json.dumps({'name':'lsl'}, sort_keys=True, indent=3)

```


```python

json.loads('{"name":"lsl"}')

```

## 总结
使用和pickle,marshal差不多

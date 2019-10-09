# asyncio 

## key

async, await


## 协程和任务

协和转换为任务


```

asyncio.create_task(coroutines)

```

运行

```

asyncio.run

```

并行运行

```

await t1
await t2
await t3

```

实测要串在一起,其他方法,使用asyncio.gather,使同时运行的任务同时调用

```python
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

```

### 超时

```python


asyncio.wait_for


```


## 总结

+ 使用asyncio运行协程，串行运行，感觉用处不大
+ 使用asyncio运行任务，并行运行，用处大
+ 在一个任务中，可以多次使用await,但task状态是新建才行

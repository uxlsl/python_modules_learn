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
实测要串在



## 总结

+ 使用asyncio运行协程，串行运行，感觉用处不大
+ 使用asyncio运行任务，并行运行，用处大
+ 在一个任务中，可以多次使用await,但task状态是新建才行

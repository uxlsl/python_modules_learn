# queue 一个同步队列类

+ queue.Queue fifo
+ queue.LifoQueue lifo
+ queue.PriorityQueue
异常
+ queue.Empty
+ queue.Full

方法
队列大小
+ Queue.qsize
+ Queue.empty
+ Queue.full

动作
+ Queue.put
+ Queue.put_nowait 会异常
+ Queue.get
+ Queue.get_nowait 会异常


## queue.PriorityQueue
取出最少元素

例子
```

q = queue.PriorityQueue()
q.put(2)
q.put(1)
q.put(3)
q.put(4)
q.put(7)
print(q.get())

```

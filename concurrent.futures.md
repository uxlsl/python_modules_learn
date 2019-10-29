# concurrent.futures 

提供高级的接口去执行异步操作

+ map 马上返回,但查看结果，就阻塞
+ submit 马上返回，但查看结果，就阻塞


Future
查看状态
+ cancel
+ cancelled
+ running
+ done
+ result 查看结果，常用



```

with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(pow, 323, 1235)
    print(future.result())


```

## 总结

1. 如果没有在查看future结果，执行结果在executor exit时候阻塞

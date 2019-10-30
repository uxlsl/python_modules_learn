# atexit 

退出调用


```

def goodbye(name, adjective):
    print('Goodbye, %s, it was %s to meet you.' % (name, adjective))

import atexit
atexit.register(goodbye, 'Donny', 'nice')

# or:
atexit.register(goodbye, adjective='nice', name='Donny')

```

## 总结

注册的函数是反序执行,如果注册的函数有相互影响关系，请确定能正确运动

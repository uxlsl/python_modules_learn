# sqlite3


+ sqlite3.connect >- Connection

+ conn.cursor()
+ c.execute
+ conn.commit
+ conn.close


安全使用参数版本

```

t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)

```


## 总结
使用sqlite3时，语句多，也许是使用dataset的时候!

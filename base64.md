# base64

Base64是一种用64个字符来表示任意二进制数据的方法。

+ base64.b64encode
+ base64.b64decode


```

>>> import base64
>>> encoded = base64.b64encode(b'data to be encoded')
>>> encoded
b'ZGF0YSB0byBiZSBlbmNvZGVk'
>>> data = base64.b64decode(encoded)
>>> data
b'data to be encoded'

```


## 例子

常见与v2ex网站，encode一些用户名

## 为什么使用base64编码

而在网络上交换数据时，比如说从A地传到B地，往往要经过多个路由设备，由于不同的设备对字符的处理方式有一些不同，这样那些不可见字符就有可能被处理错误，这是不利于传输的。所以就先把数据先做一个Base64编码，统统变成可见字符，这样出错的可能性就大降低了。

## 总结
进行数据交换时，可以考虑使用这个!

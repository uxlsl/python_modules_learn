# pathlib

提供类来操作文件系统


+ Path.resolve() 返回路径的绝对值
+ Path.mkdir() 新建目录
+ Path.is.. 一些判断


```

from pathlib import Path

p = Path('.')
[x for x in p.iterdir() if x.is_dir()]

list(p.glob('*/*.py'))

```

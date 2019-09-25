# subprocess
subprocess 让你可以调用新进程，并且连接input/out/err pipes,并且获取它的返回值，与此同时也是替换一个旧的模块和函数


## 使用subprocess.run

使用subprocess.run

+ args
+ shell
+ check


## 对比subprocess的旧方法

+ subprocess.call ~ run(…).returncode
+ subprocess.check_call ~ run(…, check=True)
+ subprocess.check_output ~ run(..., check=True, stdout=PIPE).stdout
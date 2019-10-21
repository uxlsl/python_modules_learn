# venv 


```

python -m venv

  --system-site-packages 使用系统的site-packages ,表示可以免得重新安装包
                        Give the virtual environment access to the system
                        site-packages dir.
  --symlinks            Try to use symlinks rather than copies, when symlinks
                        are not the default for the platform.
  --copies              Try to use copies rather than symlinks, even when
                        symlinks are the default for the platform.
  --clear               删除环境，重新安装，这个可以方便安装脚本,免得使用rm -rf 删除目录，使用命令一次性使用
						Delete the contents of the environment directory if it
                        already exists, before environment creation.
  --upgrade             Upgrade the environment directory to use this version
                        of Python, assuming Python has been upgraded in-place.
  --without-pip         不安装pip
						Skips installing or upgrading pip in the virtual
                        environment (pip is bootstrapped by default)
  --prompt PROMPT       Provides an alternative prompt prefix for this
                        environment.

```


## 日常使用

```

python -m venv venv

```


```

python -m venv venv --clear --system-site-packages

```

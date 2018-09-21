# IDA

## 吾爱破解下载liunx版或者使用Windows远程连接docker

1. 复制linux_server 到容器中，运行即可进行远程调试
2. 可直接运行调试，也可以附加到进程



## pwn

> pwntool

1. 在docker容器中运行：socat tcp-listen:10001,reuseaddr,fork EXEC:【执行的程序】,pty,raw,echo=0 可将程序输出什么的转到10001端口上
2. python 中使用pwntool
```python
import pwntool
io = remote("127.0.0.1",10001) 
```


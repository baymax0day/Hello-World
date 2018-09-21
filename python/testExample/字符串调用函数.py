#coding:utf8

# 使用getattr从字符串中调用函数

def bay():
    print("Hello World! baymax")

def max():
    print("baymax! Hello World")


if __name__ == '__main__':

    d = {'bay':bay}
    d['bay']()

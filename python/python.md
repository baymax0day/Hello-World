> Python元素

	1.dict是一个字典,key和value对应 {'key':'value'}
	2.list 相当于个数组 ['a','b','c']

> json操作

    1.json.dumps 将Python对象转换为json对象,type是一个字符串str
    2.json.loads 将一个json对象转换成一个Python对象,type是一个list或是dict

> 异常处理

    1.出错即可看到错误信息
    try:
        执行的语句
        =================
    except [异常名称]:
        执行语句
        =================
    else:
        执行语句, 如果没有异常,接着 这里运行
        =================
    例:
        try:
            fh = open("testfile", "w")
            fh.write("这是一个测试文件，用于测试异常!!")
        except IOError:
            print "Error: 没有找到文件或读取文件失败"
        else:
            print "内容写入文件成功"
            fh.close()

> 魔法函数

    1.查看一个对象是否为某个类型,可以用type直接输出 类型, 可以用isinstance(变量,类型)应用,返回值是一个bool类型 例: isinstance(['a'],list)

> 子类调用父类中的方法

```python
class A(object): #如果需要这样调用 父类必须继承object
      def __init__(self):
      self.s = 'I is A'

    def printA(self,s):
      print self.s + '=====' + s

class B(A):
  def printB(self,s):
    print '==========B'
    super(B,self).printA(s)

b = B()
b.printB('sssssss')    #输出:I is A =========== ssssssssss
```

> 去除unicode中不可以转换为gbk的字符

```python
a = u'\u20e3\ud83d' # 特殊字符,主要是表情                                                     
def reunicode(a):                                                                   
    try:                                                                            
        txt = a.encode('gbk')                                                       
        return txt                                                                  
    except  Exception,e:                                                            
        err = str(e).split("'")       # 捕获异常信息                                              
        errUnicode = err[4]           # 获取异常信息中不可转换的字符  
        errUnicode = eval("u" + "\'" + "\\" + errUnicode[1:] + "\'") #使用eval字符转成u'\u20e3'
        a = a.replace(unicode(errUnicode),'@')   # 替换成@                                   
        return reunicode(a)                      # 递归调用转换全部字符
print reunicode(a)                                                                    
```





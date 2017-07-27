# Hello-World
========================

>## Markdown语法 &copy;

###　**兼容HTML**

>区块元素,段落元素,属于内联样式,p标签

**无序列表**

* 列表1
- 列表2
+ 列表3

**有序列表**

1.  Bird
2.  McHale
3.  Parish

**代码块**

    <div>
        jfklsajfklsa
    <div>

**分割线**


**链接**

This is [an example](http://example.com/ "Title") inline link.

[This link](http://example.net/) has no title attribute.

__代码__

Use the `printf()` function.

``There is a literal backtick (`) here.``

![Alt text](/path/to/img.jpg)

![Alt text](/path/to/img.jpg "Optional title")

 <div style="height:30px;background-color:grey;text-align:center;line-height:30px;margin-bottom:30px;">
 分割线
 </div>

 # GIT 的操作,学习

># git 本地仓库,操作.
>>   ## 一、 基础操作
* 1. *git init* 初始化一个版本仓库
* 2. *git add filename* 添加一个文件 到暂存区
* 3. *git commit -m "备注说明"* 提交一个文件到仓库
* 4. *git status* 查看当前文件的提交,修改等状态
* 5. *git diff filename* 查看文件修改的内容
>>   ## 二、 版本修改,回退
* 1. *git log* 查看改动的历史记录,commit 指的就是每次提交的版本号,简略列出用 git log –pretty=oneline 
* 2. #### 回退操作
    * 1. *git reset  –hard HEAD^* 回退到上一个版本,或者是git reset  –hard HEAD~num,num是数字
    * 2. *git reflog* 可以获取关闭命令行之后再开的版本号
    * 3. *git reset  –hard 版本号* 可以到达任何一次版本
    * 4. *git checkout  — filename* 撤销文件在工作区的所有修改,仍可用上一个回退
>> ## 三、 远程仓库

* >创建ssh key

* 1. 运行ssh-keygen  -t rsa –C “youremail@example.com”
* 2. 登录github,打开” settings”中的SSH Keys页面，然后点击“Add SSH Key”,填上任意title，在Key文本框里黏贴id_rsa.pub文件的内容。在GitHub上的这个testgit仓库还是空的，GitHub告诉我们，可以从这个仓库克隆出新的仓库，也可以把一个已有的本地仓库与之关联，然后，把本地仓库的内容推送到GitHub仓库。
* 3. 运行 git remote add origin [git地址]("git地址")
* 4. *git push -u origin master*将本地master分支推送到远程仓库(第一次,此后git push origin master)
* 5. *git  clone [git地址]()* 克隆github 项目到本地
* 6. *git checkout -b **分支名** * 创建并切换分支,相当于git branch *分支名*, git checkout *分支名*,**git branch -d *分支名***,删除分支
* 7. 在分支上修改文件之后,add和commit操作之后,在master分支上是看不到修改的内容的,可以合并分支,在主分支上**git merge *文件名***

>> ## 四、 删除文件
* 1. rm -rf 删除一个文件或者文件夹,只是在工作区的修改,git status 可以知道哪些文件被删除了
* 2. > 若确实要在版本库中删除文件,则用git rm 删除掉,并且git commit

       > 若只是删错了,则git checkout "一键还原"到与版本库中一致的文件

# git远程服务器地址:*.*.*.*

> Note
    
    1.命令手册中,  {}里面的内容表示必选参数,可从里面的多个参数中选择一个,但是最少选一个;[]里面的内容表示可选参数,可加可不加


> 初始化git仓库:

    获取仓库( a,b 二取一)[git密码:baymax123]:
        
        a)git clone git@*.*.*.*:/home/git/baymax/shoping.git  会在当前目录生成一个shop文件夹,然后之后的工作在这个文件夹展开就行了 

        b)自己新建一个文件夹,然后在文件夹中运行 git init (初始化目录的命令),再运行 git remote add origin git@*.*.*.*:/home/git/baymax/shoping.git(添加远程仓库),git pull origin master(相当于将远程服务器上的文件下载到本地)

        c)两者的区别是:a用于本地没有文件的情况下使用git;b用于在本地已经有文件需要提交,不想初始化仓库再复制.

> git基本命令讲解(前三步 就表示可以使用git管理项目文件了)

    1.git add {文件名称或者目录} 将文件或者目录添加到暂存区
        例如:git add .  表示 将当前目录下所有文件添加到暂存区
    
    2.git commit -m '文件提交的备注说明' 将所有存在暂存区的文件放在本地仓库中

    3.git push -u origin 将文件推送到远程git服务器

    4.git log 查看改动的历史记录,commit表示提交的版本号

    5.git reset -hard HEAD^ 表示回退到上一个版本,或者 git reset -hard HEAD~num 回退到num(数字)之前的版本

    6.git reset -hard 版本号 回退到任意一个版本

# Centos-大数据

## 网络配置

### 静态IP配置
    修改 /etc/sysconfig/network-scripts/ifcfg-eth0
    其中 onboot 表示 开机启动
    bootproto=static 表示静态IP，一般是dhcp
    dns1 表示 dns
    ipaddr=IP地址
    netmask=子网掩码
    gateway=网关

### dhcp客户端
    使用 dhclient eth0 可以重新获取ip

## 源的配置
    1、备份
    mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup

    2、下载新的CentOS-Base.repo 到/etc/yum.repos.d/
        CentOS 5
        wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-5.repo
   
        CentOS 6
        wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo
        
        CentOS 7
        wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
    
    3、之后运行yum makecache生成缓存

## 环境变量
>   1.在/etc/profile文件中添加变量【对所有用户生效(永久的)】 

    用VI在文件/etc/profile文件中增加变量，该变量将会对Linux下所有用户有效，并且是“永久的”。 
    例如：编辑/etc/profile文件，添加CLASSPATH变量 
    # vi /etc/profile 
 shiziport CLASSPATH=./JAVA_HOME/lib;$JAVA_HOME/jre/lib

    注：修改文件后要想马上生效还要运行# source /etc/profile不然只能在下次重进此用户时生效。

>   2.在用户目录下的.bash_profile文件中增加变量【对单一用户生效(永久的)】 

    用VI在用户目录下的.bash_profile文件中增加变量，改变量仅会对当前用户有效，并且是“永久的”。 
    例如：编辑guok用户目录(/home/guok)下的.bash_profile 
    $ vi /home/guok/.bash.profile 
    添加如下内容： 
    export CLASSPATH=./JAVA_HOME/lib;$JAVA_HOME/jcre/lib 
    注：修改文件后要想马上生效还要运行$ source /home/guok/.bash_profile不然只能在下次重进此用户时生效。

>   3 直接运行export命令定义变量【只对当前shell(BASH)有效(临时的)】 

    在shell的命令行下直接使用[export 变量名=变量值] 定义变量，

    该变量只在当前的shell(BASH)或其子shell(BASH)下是有效的，

    shell关闭了，变量也就失效了，再打开新shell时就没有这个变量，需要使用的话还需要重新定义。

## Hadoop（v3.0.0） 单点安装

>下载和配置（1-3单点式配置）

**1.首先下载jdk，然后设置环境变量：JAVA_HOME 必须有这个环境变量值**

**2.将Hadoop文件夹下面的/bin文件夹 设置到环境变量中**
    
**3.$ hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduceexamples-2.2.0.jar  wordcount input ouput （其中input 是用户自己的文件夹，里面的内容 自定义。 output 是输出文件夹）【暂未测试】**
    
**4.再将/sbin 文件夹 加入环境变量中[java的环境变量 可以配置在./hadoop/etc/hadoop/hadoop-env.sh文件中,此文件是环境变量配置文件]**
    
**5.core-site.xml**

    core-site.xml文件中包含如读/写缓冲器用于Hadoop的实例的端口号的信息，分配给文件系统存储，用于存储所述数据存储器的限制和大小。

    打开core-site.xml 并在<configuration>，</configuration>标记之间添加以下属性。[注意空格]

    <configuration>
        <property>
            <name>fs.default.name </name>
            <value>hdfs://localhost:9000</value> 
        </property>        
    </configuration>

**6.hdfs-site.xml**

    hdfs-site.xml 文件中包含如复制数据的值，NameNode路径的信息，，本地文件系统的数据节点的路径。这意味着是存储Hadoop基础工具的地方。

    打开这个文件，并在这个文件中的<configuration></configuration>标签之间添加以下属性。

    <configuration>
        <property>
            <name>dfs.replication</name>
            <value>1</value>
        </property>                
        <property>
            <name>dfs.name.dir</name>
            <value>file:///home/baymax/hadoopinfra/hdfs/namenode </value>
        </property>                
        <property>
            <name>dfs.data.dir</name> 
            <value>file:///home/baymax/hadoopinfra/hdfs/datanode </value> 
        </property>                
    </configuration>

**7.yarn-site.xml**

    此文件用于配置成yarn在Hadoop中。打开 yarn-site.xml文件，并在文件中的<configuration></configuration>标签之间添加以下属性。

    <configuration>        
        <property>
            <name>yarn.nodemanager.aux-services</name>
            <value>mapreduce_shuffle</value> 
        </property>        
    </configuration>

**8.mapred-site.xml**

    此文件用于指定正在使用MapReduce框架。缺省情况下，包含Hadoop的模板yarn-site.xml。首先，它需要从mapred-site.xml复制。获得mapred-site.xml模板文件使用以下命令。

    $ cp mapred-site.xml.template mapred-site.xml 
    打开mapred-site.xml文件，并在此文件中的<configuration></configuration>标签之间添加以下属性。

    <configuration>
        <property> 
            <name>mapreduce.framework.name</name>
            <value>yarn</value>
        </property>    
    </configuration>

>验证Hadoop安装

***NOTE***

    Q1: 
        Starting namenodes on [localhost] 
        ERROR: Attempting to launch hdfs namenode as root 
        ERROR: but there is no HDFS_NAMENODE_USER defined. Aborting launch. 
    解决1： 
        是因为缺少用户定义造成的，所以分别编辑开始和关闭脚本 
        $ vim sbin/start-dfs.sh 
        $ vim sbin/stop-dfs.sh 
        在顶部空白处添加内容： 
        HDFS_DATANODE_USER=root 
        HADOOP_SECURE_DN_USER=hdfs 
        HDFS_NAMENODE_USER=root 
        HDFS_SECONDARYNAMENODE_USER=root 

    Q2: 
        Starting resourcemanager 
        ERROR: Attempting to launch yarn resourcemanager as root 
        ERROR: but there is no YARN_RESOURCEMANAGER_USER defined. Aborting launch. 
        Starting nodemanagers 
        ERROR: Attempting to launch yarn nodemanager as root 
        ERROR: but there is no YARN_NODEMANAGER_USER defined. Aborting launch. 
    解决2： 
        是因为缺少用户定义造成的，所以分别编辑开始和关闭脚本 
        $ vim sbin/start-yarn.sh 
        $ vim sbin/stop-yarn.sh 

        YARN_RESOURCEMANAGER_USER=root
        HADOOP_SECURE_DN_USER=yarn
        YARN_NODEMANAGER_USER=root

    Q3:
        localhost:permision denied
    解决3：
        设置下ssh免密码登陆，试试【可以】
        1.ssh-keygen -t rsa
        2.cp ~/.ssh/id_rsa.pub ~/.ssh/authorized_keys
    
    Q4：
        hadoop start-dfs.sh Error: JAVA_HOME is not set and could not be found
    解决4：
        在hadoop/etc/hadoop_env.sh 中设置Java的环境变量。
        【不要将 这个文件放在root文件夹下，可能会出错】

    Q5:
        ERROR: Cannot set priority of datanode process 5752
    解决5：
        暂未解决方式，回退版本到2.7.5
    


**1.名称节点设置**
    使用命令“hdfs namenode -format”如下设置名称节点。
        $ cd ~ 
        $ hdfs namenode -format 
    
    预期的结果如下：

    10/24/14 21:30:55 INFO namenode.NameNode: STARTUP_MSG: 
    /************************************************************ 
    STARTUP_MSG: Starting NameNode 
    STARTUP_MSG:   host = localhost/192.168.1.11 
    STARTUP_MSG:   args = [-format] 
    STARTUP_MSG:   version = 2.4.1 
    ...
    ...
    10/24/14 21:30:56 INFO common.Storage: Storage directory 
    /home/hadoop/hadoopinfra/hdfs/namenode has been successfully formatted. 
    10/24/14 21:30:56 INFO namenode.NNStorageRetentionManager: Going to 
    retain 1 images with txid >= 0 
    10/24/14 21:30:56 INFO util.ExitUtil: Exiting with status 0 
    10/24/14 21:30:56 INFO namenode.NameNode: SHUTDOWN_MSG: 
    /************************************************************ 
    SHUTDOWN_MSG: Shutting down NameNode at localhost/192.168.1.11 
    ************************************************************/

**2.验证Hadoop的DFS**

    下面的命令用来启动DFS。执行这个命令将启动Hadoop文件系统。
        $ start-dfs.sh 

    期望的输出如下所示：

    10/24/14 21:37:56 
    Starting namenodes on [localhost] 
    localhost: starting namenode, logging to /home/hadoop/hadoop
    2.4.1/logs/hadoop-hadoop-namenode-localhost.out 
    localhost: starting datanode, logging to /home/hadoop/hadoop
    2.4.1/logs/hadoop-hadoop-datanode-localhost.out 
    Starting secondary namenodes [0.0.0.0]

**3.验证Yarn 脚本**
    
    下面的命令用来启动yarn脚本。执行此命令将启动yarn守护进程。
        $ start-yarn.sh 
    
    预期输出如下：

    starting yarn daemons 
    starting resourcemanager, logging to /home/hadoop/hadoop
    2.4.1/logs/yarn-hadoop-resourcemanager-localhost.out 
    localhost: starting nodemanager, logging to /home/hadoop/hadoop
    2.4.1/logs/yarn-hadoop-nodemanager-localhost.out 

>HDFS的操作

***NOTE***

    Q1:
        Call to localhost/127.0.0.1:9000 failed on connection exception:java.net.ConnectException
    解决1：
        a）首先关闭全部已启动的服务；
        b）执行bin/hdfs namenode -format；
        c）/etc/hosts中不要有 ::1 的段，屏蔽掉；再重启试试；

    Q2：
        mkdir: `/user/hive/warehouse': No such file or directory    ls也是
    解决2：
        $HADOOP_HOME/bin/hadoop fs -mkdir -p /user/hive/warehouse 用一下这个命令 就可以了s
        


**1、启动HDFS**

    首先，格式化配置HDFS文件系统，打开NameNode(HDFS服务器)，然后执行以下命令。

    $ hadoop namenode -format 
    格式化HDFS后，启动分布式文件系统。以下命令将启动名称节点和数据节点的集群。

    $ start-dfs.sh 

**2.将数据插入到HDFS**

    假设在本地系统，这是所谓的file.txt文件中的数据,应当保存在HDFS文件系统。按照下面给出插入在Hadoop的文件系统所需要的文件的步骤。

*第1步*

    必须创建一个输入目录。

    $ $HADOOP_HOME/bin/hadoop fs -mkdir /user/input 
*第2步*

    传输并使用本地系统put命令，Hadoop文件系统中存储的数据文件。

    $ $HADOOP_HOME/bin/hadoop fs -put /home/file.txt /user/input 
*第3步*

    可以使用ls命令验证文件。

    $ $HADOOP_HOME/bin/hadoop fs -ls /user/input **

**HDFS命令参考**

    1.	
    ls <path>

    列出路径指定的目录中的内容，示出了名称，权限，拥有者，大小和修改日期的每个条目。

    2.	
    lsr <path>
    
    行为类似于-ls，但递归显示路径的所有子目录项。

    3.	
    du <path>

    显示磁盘使用率，以字节为单位，对所有的文件，这些文件匹配的路径;文件名报告使用完整HDFS协议前缀。

    4.	
    dus <path>

    类似-du，但打印路径中的所有文件/目录的磁盘使用情况的摘要。

    5.	
    mv <src><dest>

    通过移动表示src到dest，在HDFS的文件或目录。

    6.	
    cp <src> <dest>

    在HDFS复制确定src中的文件或目录到dest。

    7.	
    rm <path>

    删除文件或路径标识的空目录。

    8.	
    rmr <path>

    删除路径标识的文件或目录。递归删除所有子条目（例如，文件或路径的子目录）。

    9.	
    put <localSrc> <dest>

    从本地localSrc文件系统中的DFS标识文件或目录内复制到dest。

    10.	
    copyFromLocal <localSrc> <dest>

    等同于-put

    11.	
    moveFromLocal <localSrc> <dest>

    从标识 localSrc本地文件系统中的文件或目录中HDFS复制到dest，然后删除本地副本上成功。

    12.	
    get [-crc] <src> <localDest>

    拷贝标识 src 来确定localDest本地文件系统路径HDFS文件或目录。

    13.	
    getmerge <src> <localDest>

    检索匹配的路径的src HDFS中的所有文件，并将它们复制合并文件到标识localDest本地文件系统中。

    14.	
    cat <filen-ame>

    显示在标准输出文件名的内容。

    15.	
    copyToLocal <src> <localDest>

    等同于 -get

    16.	
    moveToLocal <src> <localDest>

    工作方式类似于-get，但删除HDFS复制成功。

    17.	
    mkdir <path>

    在创建一个HDFS命名的目录路径。

    创建任何父目录的路径丢失（例如，命令mkdir-p在Linux中）。

    18.	
    setrep [-R] [-w] rep <path>

    设置标识路径代表文件的目标文件复制因子。 （实际的复制因子会向着随着时间的推移目标移动）

    19.	
    touchz <path>

    创建在路径包含当前时间作为时间戳的文件。失败如果文件已经存在于路径，除非文件已经大小为0。

    20.	
    test -[ezd] <path>

    返回1，如果路径存在;长度为零;或者是一个目录，否则为0。

    21.	
    stat [format] <path>

    打印有关的路径信息。格式是接受块文件大小（％b），文件名（％n），块大小（%o），复制（％r）和修改日期（％y，％Y）的字符串。

    22.	
    tail [-f] <file2name>

    显示在标准输出文件的最后1KB。

    23.	
    chmod [-R] mode,mode,... <path>...

    变化符合路径标识的一个或多个对象关联的文件权限....递归执行变更与R.模式是3位八进制模式，或{augo}+/-{rwxX}。假设如果没有指定范围，则不适用umask。

    24.	
    chown [-R] [owner][:[group]] <path>...

    设置拥有用户和/或组标识路径的文件或目录....设置所有者递归，如果指定-R。

    25.	
    chgrp [-R] group <path>...

    设置所属组标识路径的文件或目录....设置组递归，如果指定-R。

    26.	
    help <cmd-name>

    返回使用上面列出的命令之一信息。必须省略了'-' 字符在cmd。
## 装机配置

> 软件目录

	1. zsh安装, oh-my-zsh 主题 bira
	
	2. conky安装

	3. JAVA 环境变量
		安装  curl -s http://get.sdkman.io | bash
		sdk -h
		sdk list java 
		sdk use java 8.0.181-oracle
		sdk detault java 8.0.181-oracle

	4. 更换kali源, 源错误转 
		1. sqlmap
		2. apktool dex2jar jd-gui 
		3. postgresql msf
		4. nmap zmap netcat 
		5. rdesktop
		6. burpsuite
		7. hydra
		8. binwalk
		9. docker 添加源 deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/debian wheezy stable
		10. qemu

	5. git安装
		├── android-backup-extractor
		├── cloacked-pixel
		├── dirsearch
		├── githack
		├── GitHack
		├── outguess
		├── P4wnP1
		├── pwndbg
		└── tplmap

	6. 常用的软件安装:

		1. boostnote 笔记软件
		2. 




> 源错误的问题
	
	server:
		hkp://p80.pool.sks-keyservers.net:80 
		ubuntu

	sudo apt-key adv --recv-keys --keyserver keyserver.Ubuntu.com --recv-keys 40976EAF437D05B5{错误的公钥}



## web配置

> apache2 site-enable和site-available的区别

	Linux下 Apache的配置文件是 /etc/apache2/apache2.conf，Apache在启动时会自动读取这个文件的配置信息。而其他的一些配置文件，如 httpd.conf等，则是通过Include指令包含进来。
	在apache2.conf里有sites-enabled目录，而在 /etc/apache2下还有一个sites-available目录，其实，这里面才是真正的配置文件，而sites- enabled目录存放的只是一些指向这里的文件的符号链接，可以通过ls -al /etc/apache2/sites-enabled/来查看。
	所以，如果apache上配置了多个虚拟主机，每个虚拟主机的配置文件都放在 sites-available下，那么对于虚拟主机的停用、启用就非常方便了：当在sites-enabled下建立一个指向某个虚拟主机配置文件的链接时，就启用了它；如果要关闭某个虚拟主机的话，只需删除相应的链接即可，无需去改配置文件，还是很方便的。


> mysql创建用户和授权
	
	1. CREATE USER 'username'@'host' IDENTIFIED BY 'password';
	2. GRANT privileges ON databasename.tablename TO 'username'@'host'
		privileges：用户的操作权限，如SELECT，INSERT，UPDATE等，如果要授予所的权限则使用ALL
		databasename：数据库名
		tablename：表名，如果要授予该用户对所有数据库和表的相应操作权限则可用*表示，如*.*

		例子:
			GRANT SELECT, INSERT ON test.user TO 'pig'@'%';
			GRANT ALL ON *.* TO 'pig'@'%';
			GRANT ALL ON maindataplus.* TO 'pig'@'%';

> ftp的配置问题
	
	fpt配置不成功,出现530错误,可以试试下面的方法
		sudo apt-get remove vsftpd
		sudo rm /etc/pam.d/vsftpd
		sudo apt-get install vsftpd 


## Tensorflow 的配置(Deepin-15.7)

> 显卡的安装

1. 卸载显卡 apt-get purge nvidia*  # 卸载原来的显卡驱动

2. 下载显卡驱动, https://www.nvidia.cn/Download/index.aspx?lang=cn, 忽略所有鸡儿错误

3. 禁用nouveau驱动, 不懂有没用.  在 /etc/modprobe.d/blacklist-nouveau.conf里面添加:
	
	blacklist nouveau 
	options nouveau modeset=0

	执行sudo update-initramfs -u,然后重启

4. 关闭x界面, Ctrl+Alt+F2, 执行 service lightdm stop. 然后安装下载的显卡驱动, 中间提示编译内核和编译器, 忽略就行

5. 执行 nvidia-smi, 有带显卡的输出就可以了(是不是可以玩游戏了)

6. 后续还需要大黄蜂,安装bumblebee, 然后使用显卡的时候

	在终端输入sudo tee /proc/acpi/bbswitch <<< ON，可开启显卡。 
	在终端输入sudo tee /proc/acpi/bbswitch <<< OFF，可关闭显卡。



> CUDA 和 CUDNN 的安装

1. 下载CUDA-9.0 https://developer.nvidia.com/cuda-90-download-archive?

2. 安装下载的文件(按q直接跳过阅读协议，然后accept，除了Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 384.81选择n, 其他自行决定)

	可能会遇到gcc版本的问题, 运行 sudo ./cuda_9.0.176_384.81_linux.run -override

3. 当前终端环境变量(zshrc)里面添加:

	#cuda
	export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64/:$LD_LIBRARY_PATH
	export PATH=/usr/local/cuda-9.0/bin:$PATH

4. 测试


	1. 在 cuda-9.0/samples/1_Utilities/deviceQuery 执行make和./deviceQuery, 成功会输出pass

	2. 在cd ~/NVIDIA_CUDA-9.0_Samples/5_Simulations/nbody 执行make和./nbody

		sudo apt-get install freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libgl1-mesa-glx libglu1-mesa libglu1-mesa-dev libglfw3-dev libgles2-mesa-dev
		然后执行 GLPATH=/usr/lib make
	
	3. 可能还会遇到gcc版本的问题

		apt-get install g++-6
		sudo ln -s /usr/bin/gcc-6 /usr/local/cuda/bin/gcc
		sudo ln -s /usr/bin/g++-6 /usr/local/cuda/bin/g++

5. 下载https://developer.nvidia.com/rdp/cudnn-download 符合版本的

	tar -zvxf cudnn-9.0-linux-x64-v7.tgz
	cd cuda
	sudo cp -P lib64/* /usr/local/cuda/lib64/
	sudo cp -P include/* /usr/local/cuda/include/
	sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*

	环境变量中添加
	#cudnn
	export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64"
	export CUDA_HOME=/usr/local/cuda

 
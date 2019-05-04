#### Docker相关

> docker文件的导入导出

    1. docker commit ea38661157c9 lamp:blog // 提交现在的容器作为镜像
    2. export 和 import 是针对 容器的
        docker export ea38661157c9 > blog.tar
        docker import - update < update.tar 

    3. save 和 load 是针对镜像的
        docker save -o blog.tar lamp:blog
        docker load blog.tar 



> 下载lamp环境

    下载镜像:
        docker pull mattrayner/lamp:latest-1604-php5  // php5 的环境

    创建容器:
        docker run -d -p 80:80 镜像ID

    导出容器:

    导入容器:

> MySQL相关

    更改密码:
        mysqladmin -u root -p 旧密码 password 新密码
        
        set password for admin=password('新密码');

        UPDATE user SET password=PASSWORD('123456') WHERE user='root';
        FLUSH PRIVILEGES;
#JAVAEE

## 使用 maven 搭建 spring-mvc 

> 新建一个maven项目

    配置build-path，将 tomcat 加入到library中， 在 【order and export】将 webapp 和 tomcat 勾选。

    配置test， 在Java resource 中 有 src/main/java  src/main/resources  src/test/java src/test/resources  如缺少就新建。

    配置test/resoutces的 build-path，output folder 为 /target/classes.选择
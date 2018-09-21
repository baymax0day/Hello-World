# adb 安卓手机调试

## 连接手机

> 列出所有可连接设备

    # adb devices

> 连接手机

    # adb shell 直接进入手机的 shell 
    # adb -s serial_number  command 对制定编号 执行命令

> 命令

    目标设备    -d    将 adb 命令发送至唯一连接的 USB 设备。    如果连接了多个 USB 设备，将返回错误。
            -e    将 adb 命令发送至唯一运行的模拟器实例。    如果有多个模拟器实例在运行，将返回错误。
            -s serial_number    将 adb 命令发送至以其 adb 分配的序列号命名的特定模拟器/设备实例（如“emulator-5556”）。    请参阅将命令发送至特定模拟器/设备实例。
    
    常规    devices    输出所有连接的模拟器/设备实例的列表。    如需了解详细信息，请参阅查询模拟器/设备实例。
            help    输出支持的 adb 命令的列表。     
            version    输出 adb 版本号。     
    
    调试    logcat [option] [filter-specs]    将日志数据输出到屏幕。     
            bugreport    将 dumpsys、dumpstate 和 logcat 数据输出到屏幕，以用于报告错误。     
            jdwp    输出给定设备上可用的 JDWP 进程的列表。    您可以使用 forward jdwp:pid 端口转发规范以连接到特定的 JDWP 进程。例如：
    adb forward tcp:8000 jdwp:472
            jdb -attach localhost:8000
    
    数据    install path_to_apk    将 Android 应用（使用 APK 文件的完整路径表示）推送到模拟器/设备。     
            pull remote local    从模拟器/设备实例将指定文件复制到开发计算机。     
            push local remote    从开发计算机将指定文件复制到模拟器/设备实例。     
    
    端口和网络连接    forward local remote    将来自指定本地端口的套接字连接转发到模拟器/设备实例上的指定远程端口。    端口规范可使用以下架构：
    tcp:port_number
    local:unix_domain_socket_name
    dev:character_device_name
    jdwp:pid
    ppp tty [parm]...    通过 USB 运行 PPP。
    tty — 用于 PPP 流的 tty。例如，dev:/dev/omap_csmi_ttyl。
    [parm]... — 零个或多个 PPP/PPPD 选项，如 defaultroute、local、notty 等。
    请注意，不得自动启动 PPP 连接。
    
    脚本    get-serialno    输出 adb 实例序列号字符串。    如需了解详细信息，请参阅查询模拟器/设备实例。
        get-state    输出模拟器/设备实例的 adb 状态。
        wait-for-device    阻止执行，直至设备处于在线状态，即直至此实例状态为 device。    您可以将此命令附加到其他 adb 命令，在此情况下，adb 在发出其他命令前将处于等待状态，直至模拟器/设备实例已连接。下面是一个示例：
        adb wait-for-device shell getprop
    请注意，此命令不会使 adb 等待整个系统已完全启动。因此，您不应将其追加到需要系统完全启动的其他命令。例如，install 需要使用 Android 软件包管理器，其仅在系统完全启动后才可用。如下命令
        adb wait-for-device install app.apk
    在模拟器或设备实例连接到 adb 服务器时立即发出 install 命令，但 Android 系统还未完全启动，因此，它将引发错误。
    
    服务器    start-server    检查 adb 服务器进程是否在运行，如果未运行则启动它。     
            kill-server    终止 adb 服务器进程。     
    
    Shell    shell    在目标模拟器/设备实例中启动远程 shell。    如需了解详细信息，请参阅发出 shell 命令。
    shell shell_command    在目标模拟器/设备实例中发出 shell 命令，然后退出远程 shell。

## 与手机交互

> 获取屏幕大小

        1.# adb shell dumpsys window displays
        2.# adb shell wm size

# 安卓逆向

## 安装好AS(AndroidStudio)

    1.Android-sdk 中会有一些工具: apktool apksigner adb 等
    2.安装完 JDK之后会有 jarsigner 的签名工具

## 签名

> 生成签名文件

    keytool -genkey -alias baymax.keystore -keyalg RSA -validity 20000 -keystore baymax.keystore

> 使用jarsigner给apk签名

    jarsigner -verbose -keystore baymax.keystore -signedjar test_signed.apk test.apk baymax.keystore 
    
    #note
    JDK8 签名时需要加上如下两个参数：
        -digestalg SHA1 -sigalg MD5withRSA
    jarsigner  -keystore baymax.keystore -storepass 123456(生成证书时候的密码)  -signedjar MyTest.apk MyTest-unsigned.apk baymax.keystore -digestalg SHA1 -sigalg MD5withRSA -tsa(可以不加) http://timestamp.digicert.com

## 调试

> 调试环境

    1.安装AS
    2.在AS中安装smalidea,教程可百度
    3.在root手机中安装xposed的一个插件,xinstaller 安装参考(http://www.open-open.com/lib/view/open1426304176732.html） 

> 调试步骤

    1.apktool d *.apk  反编译apk
    2.在AS中打开反编译的目录,配置远程调试 Run>Edit Congratulations,添加远程调试,然后Name随便填写,host填写localhost,端口是8700,打开monitor,即可查看手机
    3.在手机上安装apk,然后 运行 adb shell am start -D -n packageName/ActivityName (可以打开应用之后,运行 adb shell dumpsys activity top 查看运行在最上层的activity)
    4.然后就可以在AS中debug运行程序并调试了

# 安卓学习

## 配置

> Androidstudio 配置

```
1.自己下载gradle.zip文件，版本在gradle配置文件中
2.setting->build>gradle,配置gradle地址：linux之前下载的gradle在$USER/.gradle/wrapper
3.AndroidStudio 重新编译，安装依赖的快捷键Ctrl+F9
```

> Gradle配置国内镜像
> 
> > 对单个项目生效，在项目中的build.gradle修改内容
> 
> ```java
> buildscript {
>     repositories {
>         maven { url 'http://maven.aliyun.com/nexus/content/groups/public/' }
>                 maven{ url 'http://maven.aliyun.com/nexus/content/repositories/jcenter'}
>     }
>     dependencies {
>         classpath 'com.android.tools.build:gradle:2.2.3'
> 
>         // NOTE: Do not place your application dependencies here; they belong
>         // in the individual module build.gradle files
>     }        
> }
> 
> allprojects {
>     repositories {
>         maven { url 'http://maven.aliyun.com/nexus/content/groups/public/' }
>         maven{ url 'http://maven.aliyun.com/nexus/content/repositories/jcenter'}
>     }
> }
> ```
> 
> > 对所有项目生效，在USER_HOME/.gradle/下创建init.gradle文件
> 
> ```java
> allprojects{
>     repositories {
>         def ALIYUN_REPOSITORY_URL = 'http://maven.aliyun.com/nexus/content/groups/public'
>         def ALIYUN_JCENTER_URL = 'http://maven.aliyun.com/nexus/content/repositories/jcenter'
>         all { ArtifactRepository repo ->
>             if(repo instanceof MavenArtifactRepository){
>                 def url = repo.url.toString()
>                 if (url.startsWith('https://repo1.maven.org/maven2')) {
>                     project.logger.lifecycle "Repository ${repo.url} replaced by $ALIYUN_REPOSITORY_URL."
>                     remove repo
>                 }
>                 if (url.startsWith('https://jcenter.bintray.com/')) {
>                     project.logger.lifecycle "Repository ${repo.url} replaced by $ALIYUN_JCENTER_URL."
>                     remove repo
>                 }
>             }
>         }
>         maven {
>                 url ALIYUN_REPOSITORY_URL
>             url ALIYUN_JCENTER_URL
>         }
>     }
> }
> ```

## 安卓权限

```java
<uses-permission android:name="android.permission.INTERNET"/>  使用网络的权限，如果没有则不能访问网络

文件存储权限
<uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
```

## 安卓结合HTML5开发【helloWorld】

> HTML页面跳转

```java
一般情况下，直接在HTML页面中加a标签或者js的Windows跳转；
如果不行，则需要在Activity中 重写shouldOverrideUrlLoading方法
例如；
webView.setWebViewClient(new WebViewClient(){
    @Override
    public boolean shouldOverrideUrlLoading(WebView view, String url) {
        if(url!=""){
            webView.loadUrl(url);
        }
        return true;
    }
});
```

> HTML页面返回

```java
重写onKeyDown方法

@Override
public boolean onKeyDown(int keyCode, KeyEvent event) {
    if (keyCode == KeyEvent.KEYCODE_BACK && webView.canGoBack()) {
        webView.goBack();// 返回前一个页面
        return true;
    }
    return super.onKeyDown(keyCode, event);
}
```

> android 6.0 webview加载https问题

```java
# 解决办法
webView.setWebViewClient(new WebViewClient(){
    @Override
    public void onReceivedSslError(WebView view, SslErrorHandler handler, SslError error){
       //注意：super句话一定要删除，或者注释掉，否则又走handler.cancel()默认的不支持https的了。
       //super.onReceivedSslError(view, handler, error);
       //handler.cancel(); // Android默认的处理方式
       //handler.handleMessage(Message msg); // 进行其他处理

        handler.proceed(); // 接受所有网站的证书
    }
});	
```

```java
# android6.0 解决办法
/**
 *  Webview在安卓5.0之前默认允许其加载混合网络协议内容
 *  在安卓5.0之后，默认不允许加载http与https混合内容，需要设置webview允许其加载混合网络协议内容
 */
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {                      		                 webview.getSettings().setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW);
}
```


> Android studio中导入 org.apache.http.Header（即网络请求模块）

1、在gradle-wrapper.properties中配置使用较新版本的gradle

```java
distributionUrl=https\://services.gradle.org/distributions/gradle-2.6-all.zip
```

2、在build.gradle中使用较新版本的gradle 

```java
buildtoolsbuildscript {
    repositories {
        jcenter()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:1.3.0'

        // NOTE: Do not place your application dependencies here; they belong
        // in the individual module build.gradle files
    }
}
```

3、添加以下依赖，重新使用已经deprecated 的apache http 包：

```java
android {
    useLibrary 'org.apache.http.legacy'
}
```

4、添加apache http component 的依赖，补全缺失的类，比如Header：

```java
dependencies {
    compile 'org.apache.httpcomponents:httpcore:4.4.2'
}
```

















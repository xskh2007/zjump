## 写在前面
<<<<<<< HEAD
 - 版本号变更 2.0 -> 0.2版本 3.0 -> 0.3版本

#欢迎使用Jumpserver
**Jumpserver** 是一款由python编写开源的跳板机(堡垒机)系统，实现了跳板机应有的功能。基于ssh协议来管理，客户端无需安装agent。
支持常见系统:
 1. CentOS, RedHat, Fedora, Amazon Linux
 2. Debian
 3. SUSE, Ubuntu
 4. FreeBSD
 5. 其他ssh协议硬件设备

###截图：

首页
 
=======

##项目开发背景
由于最近线上补单，数据修改，等人工操作频繁。每次都要发邮件手动执行，很容易导致出错，没有很好的历史纪录。而且浪费时间。虽然后台系统在不停完善，但是那些功能都是死的，无法针对所有sql。所以本人就写了dbtool这个web数据库管理后台。

##项目开发目标
1、	web端数据查询
2、	web端sql检测，保证每次线上执行的sql准确性，时实性
3、	每次检测sql将在从库执行，但不commit，返回sql将会影响的行数，sql执行状态等。然后rollback。
4、	开发提交sql，主管审核，最后运维确认执行或者作废。所有sql提交，审核，执行。等状态记录。（后续添加更详细的流程，比如修改数据超过1000行需要总监审核等）
5、	Sql执行时间记录
6、	统计哪些表修改最频繁，说明涉及该表的需要优化（后续计划）
7、	Sql语法高亮(后续计划)

##项目的开发方法
	本系统采用在jumpserver开源堡垒机上面二次开发。省去大量开发时间。登陆，权限验证等都采用jumpserver的。快速实现公司需要的功能

##项目用到的知识
	Python,django, tornado,javascript, jquery,easyui等

##项目地址
	Git		地址
	Demo	地址

###项目功能附图:

首页

>>>>>>> remotes/origin/test
![webterminal](https://github.com/ibuler/static/raw/master/jumpserver3/index.jpg)

WebTerminal:

![webterminal](https://github.com/ibuler/static/raw/master/jumpserver3/webTerminal.gif)

Web批量执行命令

![WebExecCommand](https://github.com/ibuler/static/raw/master/jumpserver3/webExec.gif)

录像回放

![录像](https://github.com/ibuler/static/raw/master/jumpserver3/record.gif)

跳转和批量命令

![跳转](https://github.com/ibuler/static/raw/master/jumpserver3/connect.gif)

命令统计

![跳转](https://github.com/ibuler/static/raw/master/jumpserver3/command.jpg)

<<<<<<< HEAD
### 文档

* [访问wiki](https://github.com/jumpserver/jumpserver/wiki)
* [概览](https://github.com/jumpserver/jumpserver/wiki/%E6%A6%82%E8%A7%88)
* [名词解释](https://github.com/jumpserver/jumpserver/wiki/%E5%90%8D%E8%AF%8D%E8%A7%A3%E9%87%8A)
* [常见问题](https://github.com/jumpserver/jumpserver/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98)
* 安装基于：[RedHat 的系统](https://github.com/jumpserver/jumpserver/wiki/%E5%9F%BA%E4%BA%8E-RedHat-%E7%9A%84%E7%B3%BB%E7%BB%9F)，[Debian 的系统](https://github.com/jumpserver/jumpserver/wiki/%E5%9F%BA%E4%BA%8E-Debian-%E7%9A%84%E7%B3%BB%E7%BB%9F)
* [快速开始](https://github.com/jumpserver/jumpserver/wiki/%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)
* [安装图解](https://github.com/jumpserver/jumpserver/wiki/%E5%AE%89%E8%A3%85%E5%9B%BE%E8%A7%A3)
* [应用图解](https://github.com/jumpserver/jumpserver/wiki/%E5%BA%94%E7%94%A8%E5%9B%BE%E8%A7%A3)

### 特点

* 完全开源，GPL授权
* Python编写，容易再次开发
* 实现了跳板机基本功能，认证、授权、审计
* 集成了Ansible，批量命令等
* 支持WebTerminal
* Bootstrap编写，界面美观
* 自动收集硬件信息
* 录像回放
* 命令搜索
* 实时监控
* 批量上传下载

### 其它
=======



>>>>>>> remotes/origin/test

[Jumpserver官网](http://www.jumpserver.org)

[论坛](http://bbs.jumpserver.org)

[demo站点](http://demo.jumpserver.org)

交流群: 552054376

<<<<<<< HEAD
### 团队

![](https://github.com/ibuler/static/raw/master/jumpserver3/team.jpg)
=======

https://github.com/xskh2007/zjump/blob/master/static/dbtool.jpg
https://github.com/xskh2007/zjump/raw/master/static/dbtool.jpg
>>>>>>> remotes/origin/test





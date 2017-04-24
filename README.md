## 写在前面

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





[Jumpserver官网](http://www.jumpserver.org)

[论坛](http://bbs.jumpserver.org)

[demo站点](http://demo.jumpserver.org)

交流群: 552054376


https://github.com/xskh2007/zjump/blob/master/static/dbtool.jpg
https://github.com/xskh2007/zjump/raw/master/static/dbtool.jpg





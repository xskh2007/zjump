## 项目开发背景 ##

	由于最近线上补单，数据修改，等人工操作频繁。每次都要发邮件手动执行，很容易导致出错，  
	没有很好的历史纪录。而且浪费时间。虽然后台系统在不停完善，但是那些功能都是死的，无法针对所有sql。  
	所以本人就写了dbtool这个web数据库管理后台。  

## 项目开发目标 ##

	web端数据查询
	web端sql检测，保证每次线上执行的sql准确性，时实性
	每次检测sql将在从库执行，但不commit，返回sql将会影响的行数，sql执行状态等。然后rollback。
	开发提交sql，主管审核，最后运维确认执行或者作废。所有sql提交，审核，执行。等状态记录。（后续添加更详细的流程，比如修改数据超过1000行需要总监审核等）
	Sql执行时间记录
	统计哪些表修改最频繁，说明涉及该表的需要优化（后续计划）
	Sql语法高亮(后续计划)

## 项目的开发方法
	本系统采用在jumpserver开源堡垒机上面二次开发。省去大量开发时间。  
	登陆，权限验证等都采用jumpserver的。快速实现公司需要的功能  

## 项目用到的知识
	Python,django, tornado,javascript, jquery,easyui等  

## 项目地址
	Git 地址  https://github.com/xskh2007/zjump 
	QQ群：391096485
## 项目心得
	这是我第一次做项目，也是第一次二次开发开源项目，在这之前我甚至不会jq，不会js,但是看看网上demo,依葫芦画瓢也算实现基本功能了。
	我觉的看别人的代码对提高自己有很大帮助。有一次跟一同事聊高中学习的事，他说他以前都不会写作文，至从跟语文课代表坐一起，
	看了他的作文后，忽然恍然大悟，原来作文可以这么写。其实都是套路，写代码也差不多。jumpserver的注释并不是很多，但命名还是能看出大概作用。
	
## 项目功能附图
#### 线上sql查询界面
![Screenshot](https://raw.githubusercontent.com/xskh2007/xskh2007.github.io/master/images/zjump/select.jpg) 
#### 线上sql检测界面
![Screenshot](https://raw.githubusercontent.com/xskh2007/xskh2007.github.io/master/images/zjump/check.png) 
#### 线上sql提交界面
![Screenshot](https://raw.githubusercontent.com/xskh2007/xskh2007.github.io/master/images/zjump/submit.png) 
#### 线上sql操作界面，可以执行，和作废
![Screenshot](https://raw.githubusercontent.com/xskh2007/xskh2007.github.io/master/images/zjump/deail_list.png) 
#### 具体sql查看界面
![Screenshot](https://raw.githubusercontent.com/xskh2007/xskh2007.github.io/master/images/zjump/deail.png) 


# -*- coding: UTF-8 -*-
# 来源：疯狂的蚂蚁的博客www.crazyant.net总结整理

import MySQLdb as mdb
import sys

#获取数据库的链接对象
#con = mdb.connect('192.168.2.117', 'root', 'zzjr#2015', 'disconf')
con = mdb.connect('localhost', 'root', '', 'jumpserver')

with con:
    #获取普通的查询cursor
    cur = con.cursor()
    cur.execute("select * from juser_user")

    rows = cur.fetchall()

    #获取连接对象的描述信息
    desc = cur.description
    print 'cur.description:',desc

    #打印表头，就是字段名字
    for i in desc:
        print i[0]
    print "%s %3s" % (desc[0][0], desc[1][0])

    # print rows[2][11].decode('ascii').encode('utf-8')
    print rows[2][11]

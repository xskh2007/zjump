#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: qiantu
#qq 261767353
# !/usr/bin/env python

# from django.db import connection
import MySQLdb as mdb
from dbtool.models import Dblist

db_host="192.168.1.175"
db_user="zzjr"
db_password='zzjr#2015'
dbname='zzjr_server'


cmd='''INSERT INTO `zzjr_server`.`dbtool_dblist`
            (
             `dbname`)
VALUES (
        'zzjr_pms2');'''

def exec_db(db_name,cmd):
    con = mdb.connect(db_host, db_user, db_password, db_name, charset='utf8')
    cur = con.cursor()
    cur.execute(cmd)
    cur.close()
    mod_rows = cur.rowcount
    print mod_rows
    con.commit()
    return mod_rows

# exec_db('zzjr_bank',cmd)



def db_list(db_role):
    dblist=Dblist.objects.filter(db_role=db_role)

    return dblist
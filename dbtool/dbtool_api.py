#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: qiantu
#qq 261767353
# !/usr/bin/env python

# from django.db import connection
import MySQLdb as mdb
from dbtool.models import Dblist
from warnings import filterwarnings
filterwarnings('ignore', category = mdb.Warning)

exec_db_host="192.168.1.175"
exec_db_user="zzjr"
exec_db_password='zzjr#2015'
exec_db_name='zzjr_server'




def exec_db(db_name,cmd):
    try:
        con = mdb.connect(exec_db_host, exec_db_user, exec_db_password, exec_db_name, charset='utf8')
        cur = con.cursor()
        cur.execute(cmd)
        cur.close()
        mod_rows = cur.rowcount
        print mod_rows
        con.commit()
        return mod_rows
    except mdb.Warning as e:
        return e

# exec_db('zzjr_bank',cmd)



def db_list(db_role):
    dblist=Dblist.objects.filter(db_role=db_role)

    return dblist
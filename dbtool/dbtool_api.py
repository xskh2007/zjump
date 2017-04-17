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



import os
import ConfigParser

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
config = ConfigParser.ConfigParser()
config.readfp(open(os.path.join(BASE_DIR, 'jumpserver.conf')), "rb")

master_db_host=config.get("master_db","master_db_host")
master_db_user=config.get("master_db","master_db_user")
master_db_password=config.get("master_db","master_db_password")
master_db_name=config.get("master_db","master_db_name")

# master_db_host="192.168.1.175"
# master_db_user="zzjr"
# master_db_password='zzjr#2015'
# master_db_name='zzjr_server'




def exec_db(db_name,cmd):
    try:
        con = mdb.connect(master_db_host, master_db_user, master_db_password, master_db_name, charset='utf8')
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
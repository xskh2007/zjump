from django.test import TestCase
import MySQLdb as mdb
# Create your tests here.


readonly_db_host="192.168.1.175"
readonly_db_user="zzjr"
readonly_db_password="zzjr#2015"
readonly_dbname='zzjr_server'



db='zzjr_server'

cmd='''INSERT INTO `zzjr_server`.`dbtool_dblist`
            (
             `dbname`)
VALUES (
        'aaaaaaaaa');'''

con = mdb.connect(readonly_db_host, readonly_db_user, readonly_db_password, db, charset='utf8')
con.autocommit(0)
cur = con.cursor()
cur.execute(cmd)
cur.close()
mod_rows = cur.rowcount
# con.commit()   not commit sql
# res["cmd"] = cmd
# res["mod_rows"] = mod_rows
# con.rollback()
con.close()
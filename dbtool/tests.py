from django.test import TestCase
import MySQLdb as mdb
# Create your tests here.


readonly_db_host="192.168.1.175"
readonly_db_user="zzjr"
readonly_db_password="zzjr#2015"
readonly_dbname='zzjr_server'



db='zzjr_server'

cmd='''

  update
zzjr_server.member_money_record m,
zzjr_server.trade_order t
SET
m.stream_sn = concat( 'UN', m.stream_sn )
where
m.stream_sn = t.order_sn
and t.trade_type = 3
and t.status = 1
and t.bank_sync_status = 4
and t.gmt_create BETWEEN '2017-04-13 13:00:11' AND '2017-04-14 09:00:25';
            



'''

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
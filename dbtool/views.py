# coding: utf-8
from juser.user_api import *
from jperm.perm_api import get_group_user_perm
import re
import json
from django.http import HttpResponse
from django.db import connection
import MySQLdb as mdb
import chardet

db_host="192.168.1.175"
db_user="zzjr"
db_password="zzjr#2015"
dbname='zzjr_server'

@require_role(role='user')
def index(request):

    return my_render('dbtool/dbtool.html', locals(), request)

@require_role(role='user')
def dbtool_execute(request):
    if request.method == 'POST':
        defend_attack(request)
        cmd = request.POST.get('cmd', '')
        url = "http://127.0.0.1:8000/dbtool/myjson/?cmd=" + cmd
        print cmd
        con = mdb.connect(db_host, db_user, db_password, dbname,charset='utf8')
        with con:
            # 获取普通的查询cursor
            cur = con.cursor()
            cur.execute(cmd)
            desc = cur.description
            #print desc[0]
            field_name=[]
            for i in desc:
                field_name.append(i[0])

    users_list = User.objects.all().order_by('name')
    print users_list
    for i in users_list:
        print i

    #print cmd,fetchall
    #print locals()
    return my_render('dbtool/dbtool.html', locals(), request)
    #return my_render('dbtool/dbtool.html', {"a":"aaa"}, request)

@require_role(role='user')
def dbtool_myjson(request):
    defend_attack(request)

    cmd = request.GET.get('cmd')

    con = mdb.connect(db_host, db_user, db_password, dbname,charset='utf8')
    with con:
        cur = con.cursor()
        cur.execute(cmd)
        rows = cur.fetchall()
        desc = cur.description
        #print len(rows)
    mylist=[]
    for i in rows:
        mydisc={}
        for num in range(0, len(i)):
            #values=str(i[num]).decode("ascii").encode("utf-8")
            values = str(i[num])
            mydisc[desc[num][0]] = values

            # print chardet.detect(str(i[num]))
            #print chardet.detect(values)
        mylist.append(mydisc)
    myjson = {}
    myjson['total'] = 2800
    myjson['rows'] = mylist

    return HttpResponse(json.dumps(myjson), content_type="application/json")





#def index(request):
#    #sers=serveices.objects.all().values('ser_name').order_by('datetime')
#    sers = serveices.objects.raw("select * from serveices_serveices GROUP BY ser_name ORDER BY datetime")
#    #sers=serveices.objects.all()
#    #print sers.ser_name
#
#    return render(request,'index2.html',{'sers': sers})
# Create your views here.

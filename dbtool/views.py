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
        db = request.POST.get('database','')
        cmd = request.POST.get('cmd', '')
        print db, 111111111111111111, cmd
        json_name="data_list"
        str_url = "http://127.0.0.1:8000/dbtool/myjson/?cmd=%s&db=%s&json_name=%s" %(cmd,db,json_name)
        url = str_url.replace("\r\n"," ")
        print url
        print cmd
        con = mdb.connect(db_host, db_user, db_password, db,charset='utf8')
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
    db  = request.GET.get('db')
    cmd = request.GET.get('cmd')
    con = mdb.connect(db_host, db_user, db_password, db,charset='utf8')
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


@require_role(role='user')
def dbtool_dblistjson(request):
    defend_attack(request)
    db_list = [{"id": 'zzjr_server', "text": "zzjr_server", "icon": "database.ico"}, {"id": 'zentao', "text": "zentao", "icon": "database.ico"},{"id": 'zzjr_bank', "text": "zzjr_bank", "icon": "database.ico", "selected": "true"}]
    return HttpResponse(json.dumps(db_list), content_type="application/json")

#def index(request):
#    #sers=serveices.objects.all().values('ser_name').order_by('datetime')
#    sers = serveices.objects.raw("select * from serveices_serveices GROUP BY ser_name ORDER BY datetime")
#    #sers=serveices.objects.all()
#    #print sers.ser_name
#
#    return render(request,'index2.html',{'sers': sers})
# Create your views here.






@require_role('user')
def dbtool_dbimport(request):
    """
    the role push page
    """
    # 渲染数据
    # header_title, path1, path2 = "系统用户", "系统用户管理", "系统用户推送"
    role_id = request.GET.get('id')
    asset_ids = request.GET.get('asset_id')
    role = get_object(PermRole, id=role_id)
    assets = Asset.objects.all()
    asset_groups = AssetGroup.objects.all()
    # if asset_ids:
    #     need_push_asset = [get_object(Asset, id=asset_id) for asset_id in asset_ids.split(',')]
    #
    # if request.method == "POST":
    #     # 获取推荐角色的名称列表
    #     # 计算出需要推送的资产列表
    #     asset_ids = request.POST.getlist("assets")
    #     asset_group_ids = request.POST.getlist("asset_groups")
    #     assets_obj = [Asset.objects.get(id=asset_id) for asset_id in asset_ids]
    #     asset_groups_obj = [AssetGroup.objects.get(id=asset_group_id) for asset_group_id in asset_group_ids]
    #     group_assets_obj = []
    #     for asset_group in asset_groups_obj:
    #         group_assets_obj.extend(asset_group.asset_set.all())
    #     calc_assets = list(set(assets_obj) | set(group_assets_obj))
    #
    #     push_resource = gen_resource(calc_assets)
    #
    #     # 调用Ansible API 进行推送
    #     password_push = True if request.POST.get("use_password") else False
    #     key_push = True if request.POST.get("use_publicKey") else False
    #     task = MyTask(push_resource)
    #     ret = {}
    #
    #     # 因为要先建立用户，而push key是在 password也完成的情况下的 可选项
    #     # 1. 以秘钥 方式推送角色
    #     if key_push:
    #         ret["pass_push"] = task.add_user(role.name)
    #         ret["key_push"] = task.push_key(role.name, os.path.join(role.key_path, 'id_rsa.pub'))
    #
    #     # 2. 推送账号密码 <为了安全 系统用户统一使用秘钥进行通信， 不再提供密码方式的推送>
    #     # elif password_push:
    #     #     ret["pass_push"] = task.add_user(role.name, CRYPTOR.decrypt(role.password))
    #
    #     # 3. 推送sudo配置文件
    #     if key_push:
    #         sudo_list = set([sudo for sudo in role.sudo.all()])  # set(sudo1, sudo2, sudo3)
    #         if sudo_list:
    #             ret['sudo'] = task.push_sudo_file([role], sudo_list)
    #         else:
    #             ret['sudo'] = task.recyle_cmd_alias(role.name)
    #
    #     logger.debug('推送role结果: %s' % ret)
    #     success_asset = {}
    #     failed_asset = {}
    #     logger.debug(ret)
    #     for push_type, result in ret.items():
    #         if result.get('failed'):
    #             for hostname, info in result.get('failed').items():
    #                 if hostname in failed_asset.keys():
    #                     if info in failed_asset.get(hostname):
    #                         failed_asset[hostname] += info
    #                 else:
    #                     failed_asset[hostname] = info
    #
    #     for push_type, result in ret.items():
    #         if result.get('ok'):
    #             for hostname, info in result.get('ok').items():
    #                 if hostname in failed_asset.keys():
    #                     continue
    #                 elif hostname in success_asset.keys():
    #                     if str(info) in success_asset.get(hostname, ''):
    #                         success_asset[hostname] += str(info)
    #                 else:
    #                     success_asset[hostname] = str(info)
    #
    #     # 推送成功 回写push表
    #     for asset in calc_assets:
    #         push_check = PermPush.objects.filter(role=role, asset=asset)
    #         if push_check:
    #             func = push_check.update
    #         else:
    #             def func(**kwargs):
    #                 PermPush(**kwargs).save()
    #
    #         if failed_asset.get(asset.hostname):
    #             func(is_password=password_push, is_public_key=key_push, role=role, asset=asset, success=False,
    #                  result=failed_asset.get(asset.hostname))
    #         else:
    #             func(is_password=password_push, is_public_key=key_push, role=role, asset=asset, success=True)
    #
    #     if not failed_asset:
    #         msg = u'系统用户 %s 推送成功[ %s ]' % (role.name, ','.join(success_asset.keys()))
    #     else:
    #         error = u'系统用户 %s 推送失败 [ %s ], 推送成功 [ %s ] 请点系统用户->点对应名称->点失败，查看失败原因' % (role.name,
    #                                                             ','.join(failed_asset.keys()),
    #                                                             ','.join(success_asset.keys()))
    return my_render('dbtool/dbtool_import.html', locals(), request)
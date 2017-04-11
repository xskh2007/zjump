# coding: utf-8
from juser.user_api import *
from jperm.perm_api import get_group_user_perm
from dbtool.models import Sqllog
import re
import json
from dbtool.models import Dblist
from dbtool.forms import SqllogForm
from django.http import HttpResponse
from django.db import connection
import MySQLdb as mdb
import datetime
import chardet
from django.db.models import Q
# from operator import attrgetter
import dbtool_api



readonly_db_host="192.168.1.175"
readonly_db_user="zzjr"
readonly_db_password="zzjr#2015"
readonly_dbname='zzjr_server'



@require_role(role='user')
def index(request):

    return my_render('dbtool/dbtool.html', locals(), request)

@require_role(role='user')
def dbtool_execute(request):
    if request.method == 'POST':
        defend_attack(request)
        db = request.POST.get('database','')
        cmd = request.POST.get('cmd', '')
        # str_url = "http://127.0.0.1:8000/dbtool/myjson/?cmd=%s&db=%s" %(cmd,db)
        # url = str_url.replace("\r\n"," ")
        con = mdb.connect(readonly_db_host, readonly_db_user, readonly_db_password, db,charset='utf8')
        with con:
            # 获取普通的查询cursor
            cur = con.cursor()
            cur.execute(cmd)
            desc = cur.description
            #print desc[0]
            field_name=[]
            for i in desc:
                field_name.append(i[0])

    return my_render('dbtool/dbtool.html', locals(), request)
    #return my_render('dbtool/dbtool.html', {"a":"aaa"}, request)


#######返回查询数据结果的json
@require_role(role='user')
def dbtool_myjson(request):
    defend_attack(request)
    db  = request.POST.get('db')
    cmd = request.POST.get('cmd')
    cmd=cmd.replace("\r\n", " ")
    con = mdb.connect(readonly_db_host, readonly_db_user, readonly_db_password, db,charset='utf8')
    with con:
        cur = con.cursor()
        cur.execute(cmd)
        rows = cur.fetchall()
        desc = cur.description
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
    db_list=[{"id": '请选择数据库', "text": "请选择数据库", "icon": "database.ico", "selected": "true"}]
    defend_attack(request)
    mylist=dbtool_api.db_list("slave")
    for i in mylist:
        i=i.dbname.encode("utf-8")
        db_list.append({"id": i, "text": i, "icon": "database.ico"})
    # db_list = [{"id": 'zzjr_server', "text": "zzjr_server", "icon": "database.ico"}, {"id": 'zentao', "text": "zentao", "icon": "database.ico"},{"id": 'zzjr_bank', "text": "zzjr_bank", "icon": "database.ico", "selected": "true"}]
    return HttpResponse(json.dumps(db_list), content_type="application/json")

@require_role(role='user')
def dbtool_master_db_list(request):
    db_list=[{"id": '请选择数据库', "text": "请选择数据库", "icon": "database.ico", "selected": "true"}]
    defend_attack(request)
    mylist=dbtool_api.db_list("master")
    for i in mylist:
        i=i.dbname.encode("utf-8")
        db_list.append({"id": i, "text": i, "icon": "database.ico"})
    # db_list = [{"id": 'zzjr_server', "text": "zzjr_server", "icon": "database.ico"}, {"id": 'zentao', "text": "zentao", "icon": "database.ico"},{"id": 'zzjr_bank', "text": "zzjr_bank", "icon": "database.ico", "selected": "true"}]
    return HttpResponse(json.dumps(db_list), content_type="application/json")

@require_role(role='user')
def dbtool_field_name(request):
    defend_attack(request)
    db  = request.POST.get('db')
    cmd = request.POST.get('cmd')
    cmd=cmd.replace("\r\n", " ")
    con = mdb.connect(readonly_db_host, readonly_db_user, readonly_db_password, db,charset='utf8')
    with con:
        cur = con.cursor()
        cur.execute(cmd)
        rows = cur.fetchall()

        desc = cur.description
        field_name=[]
        for i in desc:
            mydisc = {}
            mydisc['field']=i[0]
            mydisc['title'] = i[0]
            mydisc['width'] = 100
            field_name.append(mydisc)


        print field_name


    return HttpResponse(json.dumps(field_name), content_type="application/json")


########check_sql######
@require_role(role='user')
def dbtool_check_sql(request):
    defend_attack(request)



    if request.method == 'POST':
        db = request.POST.get('db')
        cmd = request.POST.get('cmd')
        cmd = cmd.replace("\r\n", " ")
        res = {}
        res['sqltype'] = cmd.split()[0]

        try:

            con = mdb.connect(readonly_db_host, readonly_db_user, readonly_db_password, db, charset='utf8')
            cur = con.cursor()
            cur.execute(cmd)
            cur.close()
            mod_rows= cur.rowcount
            # con.commit()   not commit sql
            res["cmd"]=cmd
            res["mod_rows"]=mod_rows
            con.rollback()

            return HttpResponse(json.dumps(res), content_type="application/json")

        except mdb.Error, e:
            res["err_code"]=e.args[0]
            res["err_text"] = e.args[1]
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

            # return HttpResponse(e.args[1])
            return HttpResponse(json.dumps(res), content_type="application/json")
    return my_render('dbtool/check_sql.html', locals(), request)




########submit_sql######
@require_role(role='user')
def dbtool_submit_sql(request):
    defend_attack(request)
    dblist=Dblist.objects.all()
    # Sqllog_Form = SqllogForm(request.POST)
    # print Sqllog_Form
    # print dblist
    # db  = request.POST.get('db')
    # cmd = request.POST.get('cmd')
    # cmd=cmd.replace("\r\n", " ")
    # res = {}
    # res['sqltype']=cmd.split()[0]
    if request.method == 'POST':
        sf_post = SqllogForm(request.POST)
        print sf_post
        db_name = request.POST.get('db')
        sqllog = request.POST.get('cmd')
        sqllog = sqllog.replace("\r\n", " ")
        create_time=datetime.datetime.now()
        user_id = request.user.id
        user = get_object(User, id=user_id)
        print user.username
        try:
            if Sqllog.objects.filter(Q(sqllog=unicode(sqllog)) & ~Q(status = 0)):
                print 2222
                error = u'sql重复提交!'
                return HttpResponse(error, content_type="application/json")
            if len(sqllog) > 10000:
                error = u"sql长度不能超过10000!"
                return HttpResponse(error, content_type="application/json")
        except ServerError:
            pass
        else:
            print 4444
            if sf_post.is_valid():
                sqllog_save = sf_post.save(commit=False)
                print 555
                sqllog_save.user_id=user_id
                sqllog_save.user_name=user.username
                sqllog_save.db_name=db_name
                sqllog_save.sqllog = sqllog
                sqllog_save.create_time=create_time
                sqllog_save.status = 1
                sqllog_save.save()
                sf_post.save_m2m()
                print sqllog_save.sqllog
                msg = u'sql  添加成功'
            else:
                esg = u'sql  添加失败'


        return HttpResponse('ok', content_type="application/json")
    return my_render('dbtool/submit_sql.html', locals(), request)




@require_role('admin')
def sql_list(request):
    """ 显示日志 """
    header_title, path1 = u'审计', u'操作审计'
    date_seven_day = request.GET.get('start', '')
    date_now_str = request.GET.get('end', '')
    username_list = request.GET.getlist('username', [])
    dbname_list = request.GET.getlist('dbname', [])
    cmd = request.GET.get('cmd', '')
    status_list = request.GET.get('status', '')

    # if offset == 'online':
    #     keyword = request.GET.get('keyword', '')
    #     posts = Log.objects.filter(is_finished=False).order_by('-start_time')
    #     if keyword:
    #         posts = posts.filter(Q(user__icontains=keyword) | Q(host__icontains=keyword) |
    #                              Q(login_type__icontains=keyword))
    #
    # elif offset == 'exec':
    #     posts = ExecLog.objects.all().order_by('-id')
    #     keyword = request.GET.get('keyword', '')
    #     if keyword:
    #         posts = posts.filter(Q(user__icontains=keyword) | Q(host__icontains=keyword) | Q(cmd__icontains=keyword))
    # elif offset == 'file':
    #     posts = FileLog.objects.all().order_by('-id')
    #     keyword = request.GET.get('keyword', '')
    #     if keyword:
    #         posts = posts.filter(
    #             Q(user__icontains=keyword) | Q(host__icontains=keyword) | Q(filename__icontains=keyword))
    # else:
    # posts = Sqllog.objects.filter(status=0).order_by('create_time')
    posts = Sqllog.objects.order_by('create_time')
    username_all = set([sqllog.user_name for sqllog in Sqllog.objects.all()])
    db_all = set([sqllog.db_name for sqllog in Sqllog.objects.all()])
    cmd = request.GET.get('cmd', '')
    status_all = set([sqllog.status for sqllog in Sqllog.objects.all()])


    if date_seven_day and date_now_str:
        datetime_start = datetime.datetime.strptime(date_seven_day + ' 00:00:01', '%m/%d/%Y %H:%M:%S')
        datetime_end = datetime.datetime.strptime(date_now_str + ' 23:59:59', '%m/%d/%Y %H:%M:%S')
        posts = posts.filter(create_time__gte=datetime_start).filter(create_time__lte=datetime_end)

    if username_list:
        posts = posts.filter(user_name__in=username_list)

    if dbname_list:
        posts = posts.filter(db_name__in=dbname_list)

    if cmd:
        posts = posts.filter(sqllog__contains=cmd)
        # posts=sorted(posts, key=attrgetter('create_time'),reverse=False)
    if status_list:
        posts = posts.filter(status__in=status_list)

    if not date_seven_day:
        date_now = datetime.datetime.now()
        date_now_str = date_now.strftime('%m/%d/%Y')
        date_seven_day = (date_now + datetime.timedelta(days=-7)).strftime('%m/%d/%Y')

################   end if

    contact_list, p, contacts, page_range, current_page, show_first, show_end = pages(posts, request)

    session_id = request.session.session_key
    return render_to_response('dbtool/list_sql.html', locals(), context_instance=RequestContext(request))



@require_role('admin')
def sql_detail(request):
    """ sql_detail """
    sql_id = request.GET.get('id', 0)
    # sqllog = Sqllog.objects.filter(id=sql_id)
    mysqllog=get_object(Sqllog, id=sql_id)
    if mysqllog:
        mycontent=mysqllog.sqllog.encode("utf-8")
        return HttpResponse(mycontent)

        # if tty_logs:
        #     content = ''
        #     for tty_log in tty_logs:
        #         content += '%s: %s\n' % (tty_log.datetime.strftime('%Y-%m-%d %H:%M:%S'), tty_log.cmd)
        #     return HttpResponse(content)

    return HttpResponse('无sql记录!')



@require_role('admin')
def sql_cancel(request):
    """ sql_cancel """
    sql_id = request.GET.get('id', 0)
    # sqllog = Sqllog.objects.filter(id=sql_id)
    mysqllog = get_object(Sqllog, id=sql_id)

    user_name=request.user.username
    print sql_id,user_name
    if mysqllog:
        if mysqllog.status!=0:
            mysqllog.status=3
            mysqllog.save()
            return HttpResponse("sql已作废")
        else:
            return HttpResponse("sql状态不符合")
    else:
        return HttpResponse('无sql记录!')



@require_role('admin')
def sql_exec(request):
    """ sql_exec """
    sql_id = request.GET.get('id', 0)
    # sqllog = Sqllog.objects.filter(id=sql_id)
    mysqllog = get_object(Sqllog, id=sql_id)

    user_name=request.user.username
    print sql_id,user_name
    if mysqllog:
        if mysqllog.status==1:
            db = mysqllog.db_name.encode("utf-8")
            cmd = mysqllog.sqllog.encode("utf-8")
            print db,cmd
            mod_rows=dbtool_api.exec_db(db,cmd)
            mysqllog.status=0
            mysqllog.save()
            # print mod_rows
            return HttpResponse(mod_rows)
        else:
            return HttpResponse("sql已执行")
    else:
        return HttpResponse('无sql记录!')





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
# coding: utf-8
from django.shortcuts import render
from juser.user_api import *
from cachemanage.models import Redislist
import os
# Create your views here.


redis_path='/root/jumpserver-master/redis-3.2.8/src/redis-cli -c '

notallowcmds=["del","flushall","flushdb","set"]

# @require_role(role='user')
def cachemanage_redislistjson(request):
    redis_list=[{"id": '请选择数据库', "text": "请选择数据库", "icon": "database.ico", "selected": "true"}]
    defend_attack(request)
    mylist=Redislist.objects.filter(redis_role="master")
    for i in mylist:
        i=i.redis_host.encode("utf-8")
        redis_list.append({"id": i, "text": i, "icon": "database.ico"})
    return HttpResponse(json.dumps(redis_list), content_type="application/json")

    # return HttpResponse(mylist, content_type="application/json")

@require_role(role='user')
def cachemanage_select(request):
    if request.method == 'POST':
        myrole=request.user.role.encode("utf-8")
        print myrole
        redis_host = request.POST.get('redis_host')
        rediscmd = request.POST.get('rediscmd')
        firststr=rediscmd.split()[0].lower()
        if myrole=="CU":
            if firststr in notallowcmds:
                return HttpResponse("无权限进行此操作", content_type="application/json")
        message = os.popen(redis_path+redis_host+' '+rediscmd).readlines()
        # print redis_path+redis_host+' '+rediscmd
        # print ''.join(message)
        return HttpResponse('<br />'.join(message), content_type="application/json")
        # return HttpResponse(message, content_type="application/json")

    return my_render('cachemanage/redis_select.html', locals(), request)

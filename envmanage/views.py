# coding: utf-8
from django.shortcuts import render
import time
#
from envmanage.tasks import myclonevm

from juser.user_api import *
from envmanage.forms import EnvForm





@require_role('user')
def envmanage_clone_index(request):
    # env = EnvForm()
    # env_post = EnvForm(request.POST)
    # print dir(env_post)
    # time.sleep(1000)
    if request.method == 'POST':
        # myclonevm.delay(old_env="zstack",new_env="qiantu888")
        # myprint.delay()
        mystatus='clone vm ing'
    print "ok"
    return my_render('envmanage/envmanage_clone.html', locals(), request)

@require_role('user')
def envmanage_clone(request):
    # env = EnvForm()
    # env_post = EnvForm(request.POST)
    # print dir(env_post)
    # time.sleep(1000)
    if request.method == 'POST':
        # myclonevm.delay(old_env="zstack",new_env="qiantu888")
        # myprint.delay()
        mystatus='clone vm ing'
    print "ok"
    # return my_render('envmanage/envmanage_clone.html', locals(), request)
    return HttpResponse(mystatus)
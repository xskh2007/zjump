# coding:utf-8
from django.conf.urls import patterns, include, url
from dbtool.views import *


urlpatterns = patterns('',
    url(r'^$', index, name='dbtool'),
    url(r'^execute/$', dbtool_execute, name='dbtool_execute'),
    url(r'^myjson/$', dbtool_myjson, name='dbtool_myjson'),
    url(r'^dblistjson/$', dbtool_dblistjson, name='dbtool_dblistjson'),
    url(r'^dbimport/$', dbtool_dbimport, name='dbtool_dbimport'),
    url(r'^field_name/$', dbtool_field_name, name='dbtool_field_name'),




)
# coding:utf-8
from django.conf.urls import patterns, include, url
from dbtool.views import *


urlpatterns = patterns('',
    url(r'^$', index, name='dbtool_select'),
    url(r'^execute/$', dbtool_execute, name='dbtool_execute'),
    url(r'^myjson/$', dbtool_myjson, name='dbtool_myjson'),
    url(r'^dblistjson/$', dbtool_dblistjson, name='dbtool_dblistjson'),
    url(r'^dbimport/$', dbtool_dbimport, name='dbtool_dbimport'),
    url(r'^field_name/$', dbtool_field_name, name='dbtool_field_name'),
    url(r'^check_sql/$', dbtool_check_sql, name='dbtool_check_sql'),
    url(r'^submit_sql/$', dbtool_submit_sql, name='dbtool_submit_sql'),
    url(r'^list/(\w+)/$', sql_list, name='sql_list'),
    url(r'^sql_detail/$', sql_detail, name='sql_detail'),
    url(r'^sql_exec/$', sql_exec, name='sql_exec'),





)
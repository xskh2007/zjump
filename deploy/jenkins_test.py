#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: qiantu
#qq 261767353

from jenkinsapi.jenkins import Jenkins as Jenkins2

import jenkins
giturl="git@gitlab.lark.wiki:nbgold/"
template_xml="/root/jumpserver-master/tmp/jenkins_job.xml"
view_name = "xiasha_AAA_"
server = jenkins.Jenkins('http://192.168.2.169:8080/jenkins/', username='admin', password='zzjr#2015')

server2 = Jenkins2('http://192.168.2.169:8080/jenkins/', username='admin', password='zzjr#2015')

import xml.etree.cElementTree as ET
job_list=["bank","mldp","pms","cms","pay","member","weapon","trade","wealth","statistics","bops","napp","site","crm","channel","tiger","rams","activity","api","eagle","squirrel","wap","dragon","tengu"]
tree = ET.ElementTree(file=template_xml)

def create_job_file(model):
    # for ele in tree.iterfind("properties/hudson.model.ParametersDefinitionProperty/parameterDefinitions/hudson.model.StringParameterDefinition/defaultValue"):
    for ele in tree.findall("properties/hudson.model.ParametersDefinitionProperty/parameterDefinitions/hudson.model.StringParameterDefinition/defaultValue"):
        ele.text=model
        ele.set("updated","up")
    # for ele in tree.iterfind("scm/userRemoteConfigs/hudson.plugins.git.UserRemoteConfig/url"):
    for ele in tree.findall("scm/userRemoteConfigs/hudson.plugins.git.UserRemoteConfig/url"):
        ele.text=giturl+model+".git"
        ele.set("updated","up")
    file_name="/root/jumpserver-master/tmp/jenkins_job_"+model+".xml"
    tree.write(file_name)
    return open(file_name).read()

for i in job_list:
    EMPTY_JOB_CONFIG=create_job_file(i)
    # print EMPTY_JOB_CONFIG

    ### 批量创建job
    # new_job = server.create_job(view_name+i, EMPTY_JOB_CONFIG)

    ### 批量发布job by python-jenkins
    # parameters = {"model":i,"branch":"origin/master"}
    # deploy=server.build_job(view_name+i,parameters=parameters)

    ### 批量发布job by jenkinsapi
    parameters = {"model":i,"branch":"origin/master"}
    deploy=server2.build_job(view_name+i,params=parameters)

    ### 批量删除job
    # del_job=server.delete_job(view_name+i)
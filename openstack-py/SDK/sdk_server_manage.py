#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：openstack-py 
@File    ：sdk_server_manage.py
@Author  ：【闲鱼】：混吃等死真君
@Date    ：2024/11/28 11:11 
'''
import openstack


def create_connect(
        auth_url,
        user_domain_name,
        username,
        password
):
    return openstack.connect(auth_url=auth_url, user_domain_name=user_domain_name, username=username, password=password)


# controller_ip = "10.0.0.10"
auth_url = "http://10.0.0.10:5000/v3/"
username = "admin"
password = "000000"
user_domain_name = 'demo'
conn = create_connect(auth_url=auth_url, user_domain_name=user_domain_name, username=username, password=password)
user = conn.list_users()
for i in user:
    # print(f"用户名{user_list['name']}]")
    print(f"用户名: {i['name']}, 用户ID: {i['id']}")

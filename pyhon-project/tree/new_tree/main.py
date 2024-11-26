#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tree
@File    ：main.py
@Author  ：【闲鱼】：混吃等死真君
@Date    ：2024/11/26 22:02
'''
import os
import json
import paramiko


def get_file_tree(path):
    """递归获取指定目录的文件结构"""
    file_tree = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            # 如果是目录，递归获取目录下的文件结构
            file_tree.append({
                "name": item,
                "type": "directory",
                "children": get_file_tree(item_path)  # 递归调用
            })
        else:
            # 如果是文件，直接加入
            file_tree.append({
                "name": item,
                "type": "file"
            })
    return file_tree


def print_file_tree(file_tree):
    """打印文件树结构"""

    def print_node(node, indent=0):
        """打印每个节点，模拟层级缩进"""
        print("  " * indent + f"{node['name']} ({node['type']})")
        if node['type'] == "directory" and "children" in node:
            for child in node["children"]:
                print_node(child, indent + 1)

    for node in file_tree:
        print_node(node)


def upload_to_server(local_file, remote_path, hostname, username, private_key_path):
    """上传文件到远程服务器（使用免密钥方式）"""
    try:
        # 创建SSH客户端
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在known_hosts中的主机

        # 使用私钥进行认证
        private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
        ssh.connect(hostname, username=username, pkey=private_key)

        # 创建SFTP客户端
        sftp = ssh.open_sftp()
        sftp.put(local_file, remote_path)  # 上传文件
        sftp.close()
        ssh.close()
        print(f"文件 {local_file} 已成功上传到 {hostname}:{remote_path}")
    except Exception as e:
        print(f"上传文件时出错: {e}")


# 调用函数获取指定路径的文件树结构
path = r"E:\User\wzy\Documents\云计算"  # 修改为目标目录
file_tree = get_file_tree(path)

# 打印文件树结构
print_file_tree(file_tree)

# 保存文件树数据到 new_tree.json
local_file = "new_tree.json"
with open(local_file, "w", encoding="utf-8") as f:
    json.dump(file_tree, f, indent=2, ensure_ascii=False)

print("文件树已保存到 new_tree.json")

# 上传文件到远程服务器（免密钥登录）
hostname = "124.70.26.87"  # 目标服务器的 IP 地址
username = "root"  # 目标服务器的 SSH 用户名
private_key_path = r"C:\Users\wzy\.ssh\id_rsa"  # 替换为你的私钥文件路径
remote_path = "/root/wzy/question_from/new_tree.json"  # 目标路径

upload_to_server(local_file, remote_path, hostname, username, private_key_path)

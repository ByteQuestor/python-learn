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

# 调用函数获取指定路径的文件树结构
path = r"E:\User\wzy\Documents\云计算"  # 修改为目标目录
file_tree = get_file_tree(path)

# 打印文件树结构
print_file_tree(file_tree)

# 保存文件树数据到 new_tree.json
with open("new_tree.json", "w", encoding="utf-8") as f:
    json.dump(file_tree, f, indent=2, ensure_ascii=False)

print("文件树已保存到 new_tree.json")

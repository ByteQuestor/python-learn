# ===========================================
# Copyright Jiangsu One Cloud Technology Development Co. LTD. All Rights Reserved.
# 版权： 江苏一道云科技发展有限公司，版权所有！
# ===========================================
# encoding:utf-8
import json, logging

import openstack


# 文档地址
# https://docs.openstack.org/openstacksdk/latest/user/index.html

def create_connection(auth_url, user_domain_name, username, password):
    """
    建立连接
    """
    return openstack.connect(
        auth_url=auth_url,
        user_domain_name=user_domain_name,
        username=username,
        password=password,
    )


# user Manager
# 参见文档
# https://docs.openstack.org/openstacksdk/latest/user/guides/identity.html
# openstack.connection.Connection
# 云主机管理
class server_manager:

    def __init__(self, connect):
        self.connect = connect

    def list_servers(self):
        """
        查询所有云主机.
        """
        # to json
        items = self.connect.compute.servers()
        server_jsons = {}
        for server in items:
            server_jsons[server['name']] = server
        # return ""
        return items  # json.dumps(server_jsons,indent=2,skipkeys=True)

    def create_server(self, server_name, image_name, flavor_name, networ_name):
        image = self.connect.compute.find_image(image_name)
        flavor = self.connect.compute.find_flavor(flavor_name)
        network = self.connect.network.find_network(networ_name)
        server = self.connect.compute.create_server(
            name=server_name, image_id=image.id, flavor_id=flavor.id,
            networks=[{"uuid": network.id}])
        result = self.connect.compute.wait_for_server(server)
        return result  # json.dumps(result,indent=2,skipkeys=True)

    def delete_server(self, server_name):
        """
        删除云主机
        """
        server = self.connect.compute.find_server(server_name)
        result = self.connect.compute.delete_server(server)
        return json.dumps(result, indent=2, skipkeys=True)

    def get_server(self, server_name):
        """
        获取云主机
        """
        server = self.connect.compute.find_server(server_name)
        if server:
            return json.dumps(server, indent=2, skipkeys=True)
        else:
            return None


class image_manager:

    def __init__(self, connect):
        self.connect = connect

    def list_images(self):
        """
        查询所有镜像
        """
        # to json
        items = self.connect.compute.images()
        images_jsons = {}
        for image in items:
            images_jsons[image['name']] = image
        return json.dumps(images_jsons, indent=2)

    def get_image(self, image_name: str):
        """
        查询镜像
        """
        # to json
        image = self.connect.compute.find_image(image_name)

        return json.dumps(image, indent=2)


class flavor_manager:

    def __init__(self, connect):
        self.connect = connect

    def list_flavors(self):
        """
        查询所有云主机类型
        """
        # to json
        items = self.connect.compute.flavors()
        flavors_jsons = {}
        for flavor in items:
            flavors_jsons[flavor['name']] = flavor
        return json.dumps(flavors_jsons, indent=2)

    def get_flavor(self, flavor_name: str):
        """
        根据名称获取云主机类.
        """
        # to json
        flavor = self.connect.compute.find_flavor(flavor_name)
        return json.dumps(flavor, indent=2)


class network_manager:

    def __init__(self, connect):
        self.connect = connect

    def list_networks(self):
        """
        查询所有网络.
        """
        # to json
        items = self.connect.network.networks()
        items_jsons = {}
        for network in items:
            items_jsons[network['name']] = network
        return json.dumps(items_jsons, indent=2)

    def get_network(self, network_name: str):
        """
        跟名称查询网络.
        """
        # to json
        flavor = self.connect.compute.find_network(network_name)
        return json.dumps(flavor, indent=2)


if __name__ == '__main__':

    # Initialize connection(通过配置文件）
    # controller_ip = "10.24.2.22"
    controller_ip = "controller"
    auth_url = "http://controller:5000/v3/"
    username = "admin"
    password = "000000"
    user_domain_name = 'demo'

    conn = create_connection(auth_url, user_domain_name, username, password)

    sdk_m = server_manager(conn)
    server = sdk_m.get_server("server001")
    if server:
        result = sdk_m.delete_server("server001")
        print("servers:", result)

    # 2 创建云主机
    print("creat server--------")
    servers = sdk_m.create_server("server001", "cirros001", "m1.tiny", "net")
    print("servers:", servers)

    # 6 查询云主机
    server_info = sdk_m.get_server("server001")
print(server_info)

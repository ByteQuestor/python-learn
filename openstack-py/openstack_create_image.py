import requests, json

url = "http://192.168.100.10:5000/v3/auth/tokens"
head = {
    "Connect-Type": "application/json"
}
body = {
    "auth": {
        "identity": {
            "methods": ["password"],
            "password": {
                "user": {
                    "domain": {"name": "demo"},
                    "name": "admin",
                    "password": "000000"
                }
            }
        },
        "scope": {
            "project": {
                "domain": {"name": "demo"},
                "name": "admin"
            }
        }
    }
}

Token = requests.post(url=url, data=json.dumps(body), headers=head).headers["X-Subject-Token"]
print(Token)


class glance_api:
    def __init__(self, headers: dict, resUrl: str):
        self.headers = headers
        self.Url = resUrl

    '''
    只执行此函数的话，会进入排队状态
    '''

    def create_image(self, image_name: str, container_format="bare", disk_format="qcow2"):
        body = {
            "container_format": container_format,
            "disk_format": disk_format,
            "name": image_name
        }
        stat_code = requests.post(url=self.Url, headers=self.headers, data=json.dumps(body)).text
        return stat_code

    '''
    传入镜像名字，返回id
    '''

    def get_glance_id(self, image_name: str):
        result = json.loads(requests.get(self.Url, headers=self.headers).text)
        for i in result['images']:
            if (i['name'] == image_name):
                return i['id']

    def update_glance(self, image_name: str, file_path=""):
        self.Url = self.Url + "/" + self.get_glance_id(image_name) + "/file"
        # 这个header表示以二进制流上传文件
        self.headers['Content-Type'] = "application/octet-stream"
        status_code = requests.put(self.Url,data=open(file_path,'rb').read(),headers=self.headers).status_code
        return status_code


head_token = {
    "X-Auth-Token": Token
}
glance_cli = glance_api(headers=head_token, resUrl="http://192.168.100.10:9292/v2/images")
result = glance_cli.create_image(image_name="wzy")
print(result)
re_id = glance_cli.get_glance_id("wzy")
print(re_id)
success = glance_cli.update_glance("wzy","cirros-0.3.4-x86_64-disk.img")
print(success)

import requests, json, time

url = "http://192.168.100.10:5000/v3/auth/tokens"
head = {
    "Content-Type": "application/json"
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


class flavor_api:
    def __init__(self, handers: dict, resUrl: str):
        self.headers = handers
        self.resUrl = resUrl

    def create_flavor(self, flavor_name: str, ram, vcpus, disk, id):
        body = {
            "flavor": {
                "name": flavor_name,
                "ram": ram,
                "vcpus": vcpus,
                "disk": disk,
                "id": id
            }
        }
        code_test = requests.post(self.resUrl, data=json.dumps(body), headers=self.headers).text
        return code_test


openstack_token = requests.post(url=url, data=json.dumps(body), headers=head).headers["X-Subject-Token"]
head = {
    "X-Auth-Token": openstack_token
}
print(openstack_token)
flavor_api = flavor_api(head, "http://192.168.100.10:8774/v2.1/flavors")
test = flavor_api.create_flavor(flavor_name="wzy", ram=1024, vcpus=1, disk=20, id=456789)
print(f"云主机创建成功{test}")

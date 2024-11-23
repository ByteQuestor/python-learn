import requests, json, time

# 全局变量
controller_ip = input("请输入控制节点IP")
try:
    url = f"http://{controller_ip}:5000/v3/auth/tokens"
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
    headers = {
        "Content-Type": "application/json"
    }
    Token = requests.post(url, data=json.dumps(body), headers=headers).headers["X-Subject-Token"]
    print(Token)
except Exception as e:
    print(f"获取Token值失败，请检查访问云主机控制节点IP是否正确？输出错误信息如下：{str(e)}")
    exit(0)
'''
关于使用requests获取openstack Token的练习
首先必备三大部分：url、head、body
其中url只需要拼接，head只需要记住，body有技巧(只需要想象成作用域即可)
'''
'''
2.3.3 自定义命令行工具
使用 python 编写命令行工具，实现类似的功能：
(1) pz-kube apply -f xxx.yaml -n ：完成和 kubectl apply -f xxx.yaml -n 相同的功能；
(2) pz-kube delete -f xxx.yaml -n ：完成和 kubectl delete -f xxx.yaml -n 相同的功能；
'''
import sys
import kubernetes
import yaml

x = sys.argv
# kubernetes.config.kube_config.load_kube_config("/root/.kube/config")
cli = kubernetes.client.AppsV1Api()


# print(x)
def pz_apply_kube():
    with open("nginx.yaml") as f:
        body = yaml.safe_load(f)
        cli.create_namespaced_deployment(namespace="pzxy", body=body)


def pz_delete_kube():
    with open("nginx.yaml") as f:
        body = yaml.safe_load(f)
        cli.create_namespaced_deployment(namespace="pzxy", body=body)


if (len(x) == 1):
    print("无参数输入")
elif (len(x) == 2):
    print("pz-kube ")
    print("pz-kube apply")
    print("pz-kube delete")
elif (len(x) == 3):
    print("pz-kube ")
    print("pz-kube apply -f ")
    print("pz-kube delete -f")
elif (len(x) == 4):
    if x[1] == "pz-kube":
        if x[2] == "apply":
            if x[3] == "-f":
                print("pz-kube apply -f xxx.yaml")
        elif x[2] == "delete":
            if x[3] == "-f":
                print("pz-kube delete -f xxx.yaml")
        else:
            print("无效输入")
elif (len(x) == 5):
    if x[1] == "pz-kube":
        if x[2] == "apply":
            if x[3] == "-f":
                pz_apply_kube()
        elif x[2] == "delete":
            if x[3] == "-f":
                pz_delete_kube()
        else:
            print("无效输入")
else:
    print("错误")

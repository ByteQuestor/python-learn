from kubernetes import client, config
import yaml

config.kube_config.load_kube_config("/root/.kube/config")
cli = client.CoreV1Api()

# 第一题
services = cli.list_service_for_all_namespaces()
for i in services.items:
    if i.metadata.name == "nginx-svc":
        cli.delete_namespaced_service(namespace=i.metadata.namespace, name=i.metadata.name)

# 第二题
with open("/root/nginx-svc.yaml") as f:
    my_body = yaml.safe_load(f)
    cli.create_namespaced_service(namespace="default", body=my_body)

# 第三题
with open("service_api_dev.json","w") as f:
    out_body = cli.read_namespaced_service(namespace="default",name="nginx-svc")
    f.write(str(out_body))

# 第四题
with open("/root/nginx-svc-update.yaml") as f:
    my_body = yaml.safe_load(f)
    cli.patch_namespaced_service(namespace="default", body=my_body,name="nginx-svc")


# 第五题
with open("service_api_dev.json","w+") as f:
    out_body = cli.read_namespaced_service(namespace="default",name="nginx-svc")
    f.write(str(out_body))



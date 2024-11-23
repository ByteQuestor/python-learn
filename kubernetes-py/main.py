import kubernetes
import yaml
kubernetes.config.kube_config.load_kube_config(config_file="/root/.kube/config")
cli = kubernetes.client.CoreV1Api()
# 第一题
namelist = cli.list_service_for_all_namespaces()
for i in namelist.items():
    if i.metadata.name == "nginx-svc":
        cli.delete_namespaced_service(i.metadata.namespace,"nginx-svc")
        break
# 第二题
with open("service.yaml","r") as file:
    service_yaml = yaml.safe_load(file)
cli.create_namespaced_service(body=service_yaml)

# 第三题
namelist = cli.list_service_for_all_namespaces()
for i in namelist.items():
    if i.metadata.name == "nginx-svc":
        with open("service_api_dev.json", "w") as jsonfile:
            jsonfile.write(i.metadata.body)
        break
# 第四题
with open("service_update.yaml","r") as file:
    service_yaml_update = yaml.safe_load(file)
cli.patch_namespaced_service(body=service_yaml_update)

# 第五题
namelist = cli.list_service_for_all_namespaces()
for i in namelist.items():
    if i.metadata.name == "nginx-svc":
        with open("service_api_dev.json", "w+") as jsonfile:
            jsonfile.write(i.metadata.body)
        break
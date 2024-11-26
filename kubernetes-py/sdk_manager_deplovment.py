import kubernetes

kubernetes.config.kube_config.load_kube_config("/root/.kube/config")
cli = kubernetes.client.AppsV1Api()
with open("deployment_sdk_dev.json", "w+") as f:
    body = cli.read_namespaced_deployment(namespace="pzxy-cloud", name="nginx-deploy")
    print(str(body))
    f.write(str(body))

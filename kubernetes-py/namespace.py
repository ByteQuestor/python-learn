from kubernetes import  client,config
import openstack
if __name__ == '__main__':
    try:
        config.kube_config.load_kube_config(config_file='/root/.kube/config')
        cli_wzt = client.CoreV1Api()
        cli2 = client.AppsV1Api()
        cli3 = openstack.connect()

        cli3.auth_token

        # Step 1：
        print("获取到的所有namespace列表：")
        namespace_list = cli_wzt.list_service_for_all_namespaces()
        service_found = False
        for n in namespace_list.items:
            print(n.metadata.name)
            if n.metadata.name == 'nginx-svc':
                cli_wzt.delete_namespaced_service(n.metadata.namespace, n.metadata.name)
                service_found = True
                break

        # Step 2：
        if not service_found:
            successed = cli_wzt.create_namespaced_service()

        # Step 3:
        namespace_list = cli_wzt.list_service_for_all_namespaces()
        service_found = False
        for n in namespace_list.items:
            print(n.metadata.name)
            if n.metadata.name == 'nginx-svc':
                with open('service_api_dev.json', 'w') as f:
                    f.write(n)
                    # Step 4:
                    cli_wzt.patch_namespaced_service()
                break

        # Step 5:
        namespace_list = cli_wzt.list_service_for_all_namespaces()
        service_found = False
        for n in namespace_list.items:
            print(n.metadata.name)
            if n.metadata.name == 'nginx-svc':
                with open('service_api_dev.json', 'w+') as f:
                    f.write(n)



    except Exception as e:
        print(f"[ERROR]出现错误:{e}")
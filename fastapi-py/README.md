# 安装环境
## 必装
```shell
pip install fastapi
```
还需要一个 `ASGI` 服务器，生产环境可以使用 `Uvicorn `，
```shell
pip install "uvicorn[standard]"
```
## 可选
顺便学习`Docker`开发【可以不安装】
```shell
pip3 install docker
```

# 基本使用
## 测试文档（端口可改）
`http://127.0.0.1/docs`
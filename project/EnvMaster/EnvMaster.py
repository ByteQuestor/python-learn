import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import sys

# 检查并安装所需依赖
def install_dependencies():
    try:
        import requests
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])

# 自检功能
def check_python_env():
    modules = ["requests", "numpy", "pandas"]
    missing_modules = []

    for module in modules:
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(module)

    if missing_modules:
        messagebox.showwarning("自检结果", f"缺少以下模块：{', '.join(missing_modules)}")
    else:
        messagebox.showinfo("自检结果", "所有常用模块均已安装！")

# 通用安装函数
def install_software(software_name, install_command):
    try:
        result = subprocess.run(install_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        messagebox.showinfo("安装成功", f"{software_name} 安装成功！")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("安装失败", f"{software_name} 安装失败：\n{e.stderr.decode()}")

# 安装 Java 的回调函数
def install_java():
    install_command = ["choco", "install", "jdk8", "-y", "--params", f"INSTALLDIR={install_path.get()}"]
    install_software("Java", install_command)

# 安装 Git 的回调函数
def install_git():
    install_command = ["choco", "install", "git", "-y", "--params", f"INSTALLDIR={install_path.get()}"]
    install_software("Git", install_command)

# 安装 Node.js 的回调函数
def install_nodejs():
    install_command = ["choco", "install", "nodejs", "-y", "--params", f"INSTALLDIR={install_path.get()}"]
    install_software("Node.js", install_command)

# 安装 MySQL 的回调函数
def install_mysql():
    install_command = ["choco", "install", "mysql", "-y", "--params", f"INSTALLDIR={install_path.get()}"]
    install_software("MySQL", install_command)

# 选择安装路径的函数
def select_install_path():
    folder_selected = filedialog.askdirectory(initialdir=install_path.get())
    if folder_selected:
        install_path.set(folder_selected)

# 安装依赖
install_dependencies()

# 创建主窗口
root = tk.Tk()
root.title("环境配置工具")

# 设置固定窗口大小
root.geometry("400x350")
root.resizable(False, False)  # 禁止调整大小

# 设置默认安装路径
install_path = tk.StringVar(value="D:/root/")

# 创建安装路径文本框
path_entry = tk.Entry(root, textvariable=install_path, width=40)
path_entry.pack(pady=10)
path_entry_label = tk.Label(root, text="所有软件安装路径:")
path_entry_label.pack()

# 创建选择路径按钮
select_path_button = tk.Button(root, text="选择安装路径", command=select_install_path)
select_path_button.pack(pady=5)

# 创建分隔线
separator = tk.Frame(root, height=2, bd=1, relief="sunken")
separator.pack(fill="x", padx=10, pady=10)

# 创建安装按钮
install_java_button = tk.Button(root, text="安装 Java", command=install_java)
install_java_button.pack(pady=5)

install_git_button = tk.Button(root, text="安装 Git", command=install_git)
install_git_button.pack(pady=5)

install_nodejs_button = tk.Button(root, text="安装 Node.js", command=install_nodejs)
install_nodejs_button.pack(pady=5)

install_mysql_button = tk.Button(root, text="安装 MySQL", command=install_mysql)
install_mysql_button.pack(pady=5)

# 创建自检按钮
check_env_button = tk.Button(root, text="检查 Python 环境", command=check_python_env)
check_env_button.pack(pady=10)

# 运行主循环
root.mainloop()

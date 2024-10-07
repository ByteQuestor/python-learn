import tkinter as tk
from tkinter import messagebox, filedialog, StringVar, ttk
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

# 安装软件的回调函数
def install_with_version(software_name, version_var):
    selected_version = version_var.get()
    if not selected_version:
        messagebox.showerror("错误", "请选择一个版本！")
        return

    install_command = ["choco", "install", software_name.lower(), "-y", "--version", selected_version, "--params", f"INSTALLDIR={install_path.get()}"]
    install_software(software_name, install_command)

# 创建下拉菜单
def create_version_dropdown(parent, software_name, versions):
    version_var = StringVar()
    version_dropdown = ttk.Combobox(parent, textvariable=version_var, values=versions)
    version_dropdown.set("选择版本")
    version_dropdown.pack(pady=5)
    return version_var

# 创建主窗口
root = tk.Tk()
root.title("环境配置工具")

# 设置固定窗口大小
root.geometry("400x600")
root.resizable(False, False)  # 禁止调整大小

# 设置默认安装路径
install_path = StringVar(value="D:/root/")

# 创建安装路径文本框
path_entry = tk.Entry(root, textvariable=install_path, width=40)
path_entry.pack(pady=10)
path_entry_label = tk.Label(root, text="所有软件安装路径:")
path_entry_label.pack()

# 创建选择路径按钮
select_path_button = tk.Button(root, text="选择安装路径", command=lambda: filedialog.askdirectory(initialdir=install_path.get()))
select_path_button.pack(pady=5)

# 创建分隔线
separator = tk.Frame(root, height=2, bd=1, relief="sunken")
separator.pack(fill="x", padx=10, pady=10)

# 安装软件的版本选项
java_versions = ["8u202", "11.0.10", "17.0.1"]
git_versions = ["2.31.1", "2.32.0", "2.33.0"]
node_versions = ["14.17.0", "16.3.0", "17.0.0"]
mysql_versions = ["5.7.34", "8.0.25"]

# Java 下拉菜单
java_version_var = create_version_dropdown(root, "Java", java_versions)
install_java_button = tk.Button(root, text="安装 Java", command=lambda: install_with_version("Java", java_version_var))
install_java_button.pack(pady=5)

# Git 下拉菜单
git_version_var = create_version_dropdown(root, "Git", git_versions)
install_git_button = tk.Button(root, text="安装 Git", command=lambda: install_with_version("Git", git_version_var))
install_git_button.pack(pady=5)

# Node.js 下拉菜单
node_version_var = create_version_dropdown(root, "Node.js", node_versions)
install_nodejs_button = tk.Button(root, text="安装 Node.js", command=lambda: install_with_version("Node.js", node_version_var))
install_nodejs_button.pack(pady=5)

# MySQL 下拉菜单
mysql_version_var = create_version_dropdown(root, "MySQL", mysql_versions)
install_mysql_button = tk.Button(root, text="安装 MySQL", command=lambda: install_with_version("MySQL", mysql_version_var))
install_mysql_button.pack(pady=5)

# 创建自检按钮
check_env_button = tk.Button(root, text="检查 Python 环境", command=check_python_env)
check_env_button.pack(pady=10)

# 安装依赖
install_dependencies()

# 运行主循环
root.mainloop()
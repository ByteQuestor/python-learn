import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import subprocess
import json
import os

# 执行 choco search 并返回结果
def search_software(software_name):
    try:
        result = subprocess.run(["choco", "search", software_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output_text.delete(1.0, tk.END)  # 清空回显区域
        output_text.insert(tk.END, result.stdout.decode() + "\n")  # 显示搜索结果
        
        # 保存结果为 JSON
        save_results_as_json(software_name, result.stdout.decode())
        
    except subprocess.CalledProcessError as e:
        output_text.insert(tk.END, e.stderr.decode() + "\n")

# 保存搜索结果为 JSON
def save_results_as_json(software_name, results):
    lines = results.splitlines()
    packages = []

    for line in lines:
        if line.startswith(software_name + " "):  # 只保留名称完全匹配的结果
            parts = line.split()
            name = parts[0]
            version_description = parts[1]  # 假设版本和描述的第一个词为版本
            packages.append({"name": name, "description": version_description})

    # 保存到 JSON 文件
    file_name = f"{software_name}.json"
    with open(file_name, "w", encoding="utf-8") as json_file:
        json.dump(packages, json_file, ensure_ascii=False, indent=4)
    
    messagebox.showinfo("保存成功", f"搜索结果已保存为 {file_name}")

# 读取 JSON 文件并创建版本选择下拉菜单
def load_versions(software_name):
    file_name = f"{software_name}.json"
    if not os.path.exists(file_name):
        messagebox.showerror("错误", f"未找到 {file_name} 文件！")
        return
    
    with open(file_name, "r", encoding="utf-8") as json_file:
        packages = json.load(json_file)
    
    # 清空下拉菜单和按钮
    version_dropdown['values'] = [pkg['description'] for pkg in packages]
    version_dropdown.set("选择版本")
    
    # 创建安装按钮
    install_button.pack(pady=5)

# 安装选定版本
def install_software(software_name):
    selected_version = version_dropdown.get()
    if selected_version == "选择版本":
        messagebox.showerror("错误", "请先选择一个版本！")
        return
    
    install_command = ["choco", "install", software_name, "--version", selected_version, "-y"]
    try:
        subprocess.run(install_command, check=True)
        messagebox.showinfo("安装成功", f"{software_name} {selected_version} 安装成功！")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("安装失败", f"{software_name} 安装失败：\n{e.stderr.decode()}")

# 一键安装 Chocolatey
def install_chocolatey():
    try:
        install_command = [
            'powershell', '-Command', 
            'Set-ExecutionPolicy Bypass -Scope Process -Force; '
            '[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12; '
            'iex ((New-Object System.Net.WebClient).DownloadString("https://chocolatey.org/install.ps1"))'
        ]
        subprocess.run(install_command, check=True)
        messagebox.showinfo("安装成功", "Chocolatey 安装成功！")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("安装失败", f"Chocolatey 安装失败：\n{e.stderr.decode()}")

# 退出应用程序
def exit_app():
    root.quit()

# 创建主窗口
root = tk.Tk()
root.title("Chocolatey 搜索工具")

# 设置固定窗口大小
root.geometry("400x600")
root.resizable(False, False)  # 禁止调整大小

# 提示信息
info_label = tk.Label(root, text="需要提前安装 Chocolatey", font=("Arial", 10))
info_label.pack(pady=5)

# 一键安装按钮
install_choco_button = tk.Button(root, text="一键安装 Chocolatey", command=install_chocolatey)
install_choco_button.pack(pady=5)

# 创建回显区域
output_text = scrolledtext.ScrolledText(root, width=50, height=15)
output_text.pack(pady=10)

# 创建版本选择下拉菜单
version_dropdown = ttk.Combobox(root, values=[], state="readonly")
version_dropdown.pack(pady=5)

# 创建安装按钮
install_button = tk.Button(root, text="安装", command=lambda: install_software(current_software))
install_button.pack(pady=5)
install_button.pack_forget()  # 初始时隐藏安装按钮

# 软件与按钮的映射
software_list = {
    "MySQL": "mysql",
    "Git": "git",
    "Node.js": "nodejs",
    "Java": "openjdk"  # 使用 OpenJDK 替代 Java
}

# 当前选择的软件名称
current_software = ""

# 创建按钮容器
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# 创建搜索按钮
def create_search_button(software_name, display_name):
    def search_and_load():
        global current_software
        current_software = software_name
        search_software(software_name)
        load_versions(software_name)

    button = tk.Button(button_frame, text=f" {display_name}", command=search_and_load)
    button.pack(side=tk.LEFT, padx=5, pady=5)

# 动态创建搜索按钮
for display_name, software_name in software_list.items():
    create_search_button(software_name, display_name)

# 创建退出按钮
exit_button = tk.Button(root, text="退出", command=exit_app)
exit_button.pack(pady=10)

# 运行主循环
root.mainloop()

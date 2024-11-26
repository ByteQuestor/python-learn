import tkinter as tk
from tkinter import scrolledtext, messagebox
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

# 创建主窗口
root = tk.Tk()
root.title("Chocolatey 搜索工具")

# 设置固定窗口大小
root.geometry("400x400")
root.resizable(False, False)  # 禁止调整大小

# 创建回显区域
output_text = scrolledtext.ScrolledText(root, width=50, height=15)
output_text.pack(pady=10)

# 创建搜索按钮
search_mysql_button = tk.Button(root, text="搜索 MySQL", command=lambda: search_software("mysql"))
search_mysql_button.pack(pady=5)

search_git_button = tk.Button(root, text="搜索 Git", command=lambda: search_software("git"))
search_git_button.pack(pady=5)

# 运行主循环
root.mainloop()

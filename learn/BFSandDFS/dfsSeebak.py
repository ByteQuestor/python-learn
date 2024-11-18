import matplotlib.pyplot as plt
import networkx as nx
from time import sleep

step = 0  # 记录尝试的步数
graph = nx.DiGraph()  # 有向图
positions = {}  # 保存每个节点的绘图位置
active_node = None  # 当前活跃节点

fig, ax = plt.subplots(figsize=(10, 6))
plt.ion()  # 开启交互模式
ax.axis("off")  # 不显示坐标轴

mode = "auto"  # 模式：'auto' 为自动，'manual' 为手动


def draw_graph(active_node=None):
    """绘制递归树图，突出显示当前活跃节点"""
    ax.clear()
    ax.axis("off")

    # 设置节点颜色，高亮当前活跃节点
    node_colors = [
        "orange" if node == active_node else "lightblue" for node in graph.nodes
    ]
    nx.draw(
        graph,
        pos=positions,
        with_labels=True,
        node_color=node_colors,
        edge_color="gray",
        node_size=2000,
        font_size=10,
        ax=ax,
    )
    plt.pause(0.5)


def dfs_crack_password(password="000", depth=0, parent_node=None):
    global step, active_node
    step += 1

    node_label = f"{password} (Step {step})"
    graph.add_node(node_label)  # 添加当前节点
    positions[node_label] = (depth, -step)  # 为节点设置位置

    if parent_node:
        graph.add_edge(parent_node, node_label)  # 添加边

    # 更新活跃节点
    active_node = node_label
    draw_graph(active_node)  # 动态绘制图形

    print(f"第{step}步：正在尝试密码 {password}")

    # 手动模式
    if mode == "manual":
        input("按回车键继续下一步...")

    if password == "999":
        print(f"密码破解成功，正确密码是: {password}")
        return password

    if depth == 3:  # 三位数密码，深度达到3说明已经处理完所有位数
        return None

    for i in range(10):
        new_password = password[:depth] + str(i) + password[depth + 1:]
        result = dfs_crack_password(new_password, depth + 1, node_label)  # 递归调用
        if result:
            return result


# 选择模式
while True:
    user_input = input("请选择运行模式（1: 自动, 2: 手动，默认: 自动）：").strip()
    if user_input == "2":
        mode = "manual"
        break
    elif user_input == "1" or user_input == "":
        mode = "auto"
        break
    else:
        print("无效输入，请输入 1 或 2 或直接回车！")

correct_password = dfs_crack_password()

plt.ioff()  # 关闭交互模式
plt.show()  # 显示最终图形

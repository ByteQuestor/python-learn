import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.widgets import Button
import matplotlib.colors as mcolors

step = 0  # 记录尝试的步数
graph = nx.DiGraph()  # 有向图

fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.2)  # 调整图形位置，为按钮留出空间
plt.ion()  # 开启交互模式
ax.axis("off")  # 不显示坐标轴

mode = "auto"  # 模式：'auto' 为自动，'manual' 为手动
next_step = False  # 控制手动模式是否进行下一步

# 颜色映射
color_map = list(mcolors.TABLEAU_COLORS.values())


def get_node_color(node):
    """根据节点的深度返回颜色"""
    depth = int(node.split("(Step")[0].count(" "))  # 通过名称计算深度
    return color_map[depth % len(color_map)]


def draw_graph(current_node=None):
    """重新绘制递归树，仅显示现存节点"""
    ax.clear()  # 清空绘图区
    ax.axis("off")  # 不显示坐标轴

    if graph.nodes:
        # 动态重新布局
        positions = nx.shell_layout(graph)
        # 设置节点颜色
        node_colors = [
            "red" if node == current_node else get_node_color(node) for node in graph
        ]
        nx.draw(
            graph,
            pos=positions,
            with_labels=True,
            node_color=node_colors,
            edge_color="black",
            node_size=2000,
            font_size=10,
            ax=ax,
        )
    plt.pause(1)  # 暂停以显示动态效果


def remove_subtree(node):
    """递归删除指定节点的所有子节点"""
    # 获取所有子节点
    children = list(graph.successors(node))
    for child in children:
        remove_subtree(child)  # 递归删除子节点
    # 删除当前节点
    if node in graph:
        graph.remove_node(node)


def dfs_crack_password(password="000", depth=0, parent=None):
    global step, next_step
    step += 1

    # 添加当前节点
    node_label = f"{password} (Step {step})"
    graph.add_node(node_label)

    if parent:
        graph.add_edge(parent, node_label)  # 添加边

    draw_graph(current_node=node_label)  # 绘制当前图形，当前节点高亮

    print(f"第{step}步：正在尝试密码 {password}")

    # 手动模式暂停，等待按钮触发
    if mode == "manual":
        next_step = False
        while not next_step:
            plt.pause(0.1)  # 等待按钮点击

    if password == "999":
        print(f"密码破解成功，正确密码是: {password}")
        return password

    if depth == 3:  # 三位数密码，深度达到3说明已经处理完所有位数
        return None

    # 递归处理
    for i in range(10):
        new_password = password[:depth] + str(i) + password[depth + 1:]
        result = dfs_crack_password(new_password, depth + 1, node_label)
        if result:
            return result

    # 回退时移除当前节点及其子树
    remove_subtree(node_label)
    draw_graph()  # 更新图形
    return None


def on_next(event):
    """按钮事件：允许下一步"""
    global next_step
    next_step = True


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

if mode == "manual":
    # 创建按钮
    ax_next = plt.axes([0.4, 0.05, 0.2, 0.075])  # 按钮位置 [left, bottom, width, height]
    btn_next = Button(ax_next, "next")
    btn_next.on_clicked(on_next)  # 绑定按钮点击事件

correct_password = dfs_crack_password()

plt.ioff()  # 关闭交互模式
plt.show()  # 显示最终图形

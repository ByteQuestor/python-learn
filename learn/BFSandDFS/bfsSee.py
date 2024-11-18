import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

def bfs_crack_password_animation():
    password_graph = nx.DiGraph()
    queue = ["000"]
    visited = set()
    step_data = []

    while queue:
        password = queue.pop(0)
        visited.add(password)

        # 限制每帧的节点数
        local_neighbors = []

        for i in range(len(password)):
            for j in range(10):
                new_digit = int(password[i]) + j
                if new_digit > 9:
                    new_digit -= 10

                new_password = password[:i] + str(new_digit) + password[i + 1:]
                if new_password not in visited and new_password not in queue:
                    queue.append(new_password)
                    password_graph.add_edge(password, new_password)
                    local_neighbors.append(new_password)

        # 保存当前帧数据，限制只绘制相关节点和边
        step_data.append({
            "current": password,
            "neighbors": local_neighbors,
            "visited": list(visited),
            "graph": password_graph.copy()
        })

        if password == "999":
            break

    return step_data


def update(frame):
    """更新每一帧的绘图内容"""
    data = step_data[frame]
    graph = data["graph"]
    current = data["current"]
    neighbors = data["neighbors"]
    visited = data["visited"]

    ax.clear()
    pos = nx.spring_layout(graph, seed=42)

    # 绘制已访问的节点
    nx.draw_networkx_nodes(graph, pos, nodelist=visited, node_color="red", label="Visited", alpha=0.5, ax=ax)

    # 绘制当前节点
    nx.draw_networkx_nodes(graph, pos, nodelist=[current], node_color="yellow", label="Current", ax=ax)

    # 绘制当前节点的邻居
    nx.draw_networkx_nodes(graph, pos, nodelist=neighbors, node_color="green", label="Neighbors", ax=ax)

    # 绘制与当前节点相关的边
    edges = [(current, neighbor) for neighbor in neighbors]
    nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color="blue", ax=ax)

    # 绘制标签
    nx.draw_networkx_labels(graph, pos, font_size=8, ax=ax)

    # 更新标题
    ax.set_title(f"Step {frame + 1}: Current = {current}", fontsize=14)

    # 显示图例
    ax.legend(scatterpoints=1, loc="upper left", fontsize=10)


def toggle_animation(event):
    """暂停或恢复动画"""
    global ani_running
    if ani_running:
        ani.event_source.stop()
        ani_running = False
    else:
        ani.event_source.start()
        ani_running = True


def next_step(event):
    """手动模式：点击按钮显示下一帧"""
    global manual_frame
    if not ani_running:  # 确保动画暂停
        if manual_frame < len(step_data) - 1:
            manual_frame += 1
            update(manual_frame)
            fig.canvas.draw_idle()  # 强制刷新画布


# 获取 BFS 数据
step_data = bfs_crack_password_animation()

# 初始化绘图
fig, ax = plt.subplots(figsize=(10, 8))
ani_running = True  # 动画运行状态
manual_frame = 0    # 当前帧索引

# 初始化动画
ani = FuncAnimation(fig, update, frames=len(step_data), interval=1000, repeat=False)

# 添加暂停/恢复按钮
ax_pause = plt.axes([0.7, 0.02, 0.1, 0.04])  # 按钮位置 [左, 下, 宽, 高]
btn_pause = Button(ax_pause, "Pause/Resume")
btn_pause.on_clicked(toggle_animation)

# 添加下一步按钮
ax_next = plt.axes([0.82, 0.02, 0.1, 0.04])
btn_next = Button(ax_next, "Next Step")
btn_next.on_clicked(next_step)

plt.show()

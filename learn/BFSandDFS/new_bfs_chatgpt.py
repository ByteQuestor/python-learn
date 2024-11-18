from collections import deque


def bfs_crack_password(start: str, target: str):
    """
    广度优先搜索破解密码
    :param start: 起始密码（字符串形式，如 "000"）
    :param target: 目标密码（字符串形式，如 "999"）
    """
    if start == target:
        print(f"起始密码就是目标密码：{target}")
        return

    queue = deque([start])
    visited = set([start])  # 记录访问过的密码
    step = 0

    while queue:
        password = queue.popleft()  # 从队列取出当前密码
        step += 1
        print(f"第{step}步：正在尝试密码 {password}")

        # 判断是否破解成功
        if password == target:
            print(f"密码破解成功，正确密码是 {password}")
            return

        # 尝试拨动密码锁的每一位
        for i in range(len(password)):
            current_digit = int(password[i])
            for delta in [-1, 1]:  # 拨动当前位 +1 或 -1
                new_digit = (current_digit + delta) % 10  # 确保 0-9 循环
                new_password = password[:i] + str(new_digit) + password[i + 1:]

                # 如果新密码未访问过，加入队列
                if new_password not in visited:
                    visited.add(new_password)
                    queue.append(new_password)

    # 如果队列为空仍未找到目标密码
    print("未能破解密码（可能目标密码不合法）")


# 测试代码
start_password = "000"
target_password = "999"  # 任意目标密码
bfs_crack_password(start_password, target_password)

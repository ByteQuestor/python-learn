from collections import deque

def bfs_crack_password(target="999"):
    queue = deque(["000"])  # 初始化队列，从"000"开始
    visited = set()          # 用来记录已访问的密码
    step = 0                 # 记录尝试的步数

    while queue:
        password = queue.popleft()  # 取出队列头部的密码
        step += 1
        print(f"第{step}步：正在尝试密码 {password}")

        # 结束条件
        if password == target:
            print(f"密码破解成功，正确密码是 {password}")
            break

        visited.add(password)

        # 对密码的每一位数字分别进行 +1 或 -1 操作
        for i in range(len(password)):
            for delta in [-1, 1]:  # 两种操作：加1 或 减1
                # 获取当前数字
                current_digit = int(password[i])

                # 计算新数字
                new_digit = (current_digit + delta) % 10

                # 生成新的密码
                new_password = password[:i] + str(new_digit) + password[i + 1:]

                # 如果新密码没有访问过，加入队列
                if new_password not in visited:
                    queue.append(new_password)

# 广度优先
bfs_crack_password()

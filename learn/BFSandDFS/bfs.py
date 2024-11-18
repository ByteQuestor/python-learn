def bfs_crack_password():
    queue = ["000"]
    visited = set()
    step = 0  # 记录尝试的步数

    while queue:
        password = queue.pop(0)
        step += 1  # 这个只是为了记录回显的
        print(f"第{step}步：正在尝试密码 {password}")
        # 结束条件
        if password == "999":
            print(f"密码破解成功，正确密码是 {password}")
            print(queue)
            break
        visited.add(password)
        for i in range(len(password)):
            for j in range(10):
                new_digit = int(password[i]) + j
                if new_digit > 9:
                    new_digit -= 10
                elif new_digit < 0:
                    new_digit += 10

                new_password = password[:i] + str(new_digit) + password[i + 1:]
                if new_password not in visited:
                    queue.append(new_password)


# 广度优先
bfs_crack_password()

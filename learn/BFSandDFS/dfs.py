step = 0  # 记录尝试的步数
visited = set()  # 用于记录已经尝试过的密码


def dfs_crack_password(password="000", depth=0):
    global step
    step += 1
    print(f"第{step}步：正在尝试密码 {password}")

    if password == "999":
        print(f"密码破解成功，正确密码是: {password}")
        return password

    if password in visited:
        return None  # 如果已经尝试过这个密码，跳过

    visited.add(password)  # 将当前密码标记为已访问

    if depth == 3:  # 三位数密码，深度达到3说明已经处理完所有位数
        return None

    for i in range(10):
        # 只修改当前位数对应的密码
        new_password = password[:depth] + str(i) + password[depth + 1:]

        # 确保不重复进入已经访问过的密码
        if new_password not in visited:
            result = dfs_crack_password(new_password, depth + 1)  # 递归调用，深入下一位数进行尝试
            if result:
                return result


correct_password = dfs_crack_password()

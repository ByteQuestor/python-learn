from flask import Flask, render_template, jsonify
import os
import json

app = Flask(__name__)

# 获取目录结构，递归遍历
def get_directory_structure(rootdir):
    structure = {}

    # 获取当前目录下的所有文件夹和文件
    try:
        dirnames = next(os.walk(rootdir))[1]  # 获取子目录
        filenames = next(os.walk(rootdir))[2]  # 获取文件
    except StopIteration:
        return structure

    structure = {
        'dirs': dirnames,
        'files': filenames
    }

    # 递归处理子目录
    for dirname in dirnames:
        # 拼接子目录路径
        subdir_path = os.path.join(rootdir, dirname)
        structure[dirname] = get_directory_structure(subdir_path)

    return structure


# 返回指定目录结构的JSON数据
@app.route('/generate_tree/<path:dir_path>')
def generate_tree(dir_path):
    root_directory = r'E:\User\wzy\Documents'  # 根目录
    target_path = os.path.join(root_directory, dir_path)  # 拼接目录路径

    print(f"Target path: {target_path}")  # 调试输出路径

    if os.path.exists(target_path) and os.path.isdir(target_path):
        structure = get_directory_structure(target_path)
        # 将结构保存到 tree.json 文件
        with open('tree.json', 'w', encoding='utf-8') as json_file:
            json.dump(structure, json_file, ensure_ascii=False, indent=4)
        print(f"Directory structure saved to tree.json")  # 调试输出
        return jsonify({"message": "tree.json has been generated."}), 200
    else:
        return jsonify({'error': 'Directory not found'}), 404


# 首页，加载根目录的文件树
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

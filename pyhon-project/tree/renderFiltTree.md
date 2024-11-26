文件树渲染 HTML 页面说明文档
该页面的目的是动态加载一个文件树（从一个 JSON 文件中获取数据），并在网页上以树形结构呈现文件夹和文件，用户可以点击文件夹进行展开和收起操作。

# 页面结构
## HTML 结构
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>文件树</title>
    <style>...</style>
</head>
<body>
    <h1>文件树</h1>
    <div id="file-tree"></div>

    <script>...</script>
</body>
</html>
<html>：页面根元素，定义页面的语言为英语（lang="en"）。
<head>：包含页面的元数据，如字符编码、视口设置、标题以及样式。
<meta charset="UTF-8">：定义字符编码为 UTF-8，确保能正确显示中文。
<meta name="viewport" content="width=device-width, initial-scale=1.0">：设置响应式视图，适应各种设备的屏幕宽度。
<title>文件树</title>：定义网页的标题，显示在浏览器标签页上。
<style>：包含页面的 CSS 样式。
<body>：页面的主体部分，显示文件树的标题和树结构容器。
<h1>：页面标题，展示为“文件树”。
<div id="file-tree"></div>：一个空的 div 容器，用于动态插入文件树内容。
<script>：包含用于渲染文件树的 JavaScript 代码。
```
## 样式说明（CSS）
页面的样式使用了 CSS 来进行美化和适配不同设备屏幕大小。

样式重置：通过设置 * { margin: 0; padding: 0; box-sizing: border-box; } 清除浏览器的默认样式，使得页面的样式更加一致。
字体和颜色：页面使用 Arial 字体，背景色设置为浅灰色 (#f4f4f9)，文本颜色为深灰色 (#333)。
文件树样式：
文件夹和文件使用不同的图标：文件夹使用 📁 图标，文件使用 📄 图标。
通过 li:hover 设置鼠标悬停时的背景色变化，使得交互更加友好。
使用 li.open > ul 来控制展开的子节点的显示和隐藏。
响应式设计：页面支持不同设备屏幕宽度的调整，最大支持 768px 和 480px 屏幕。
## JavaScript 说明
1. 加载和渲染文件树
```javascript
function loadFileTree() {
    fetch('../tree.json')  // 假设 tree.json 在根目录
        .then(response => response.json())
        .then(data => renderFileTree(data))
        .catch(error => console.error('Error loading tree.json:', error));
}
loadFileTree()：函数用于从服务器加载 tree.json 文件，文件中包含文件树的数据。
fetch('../tree.json')：从相对路径 ../tree.json 获取 JSON 数据。
.then(response => response.json())：解析返回的 JSON 数据。
.then(data => renderFileTree(data))：将获取到的文件树数据传递给 renderFileTree 函数进行渲染。
.catch(error => console.error(...))：如果请求过程中出现错误，捕获并打印错误信息。
````
2. 渲染文件树
```javascript
function renderFileTree(data) {
    const treeContainer = document.getElementById('file-tree');
    treeContainer.innerHTML = ''; // 清空之前的树

    const rootNode = document.createElement('ul');
    treeContainer.appendChild(rootNode);

    function renderNode(node, parentElement) {
        const li = document.createElement('li');
        ...
    }

    const root = {
        name: 'root',
        dirs: Object.keys(data),
        files: []
    };

    renderNode(root, rootNode);
}
renderFileTree(data)：该函数负责将加载的文件树数据渲染到页面上。
treeContainer.innerHTML = '';：首先清空已有的文件树内容，以避免重复渲染。
const rootNode = document.createElement('ul');：创建根节点的 ul 元素，用于存放文件树。
调用 renderNode 来递归渲染每个节点（文件夹或文件）。
```
3. 渲染单个节点
```javascript
function renderNode(node, parentElement) {
    const li = document.createElement('li');

    if (node.dirs.length > 0 || node.files.length > 0) {
        li.classList.add('folder');
    } else {
        li.classList.add('file');
    }

    li.textContent = node.name;

    if (node.dirs.length > 0 || node.files.length > 0) {
        const childrenContainer = document.createElement('ul');
        li.appendChild(childrenContainer);

        node.dirs.forEach(dir => {
            const dirNode = {
                name: dir,
                dirs: data[dir]?.dirs || [],
                files: data[dir]?.files || []
            };
            renderNode(dirNode, childrenContainer);
        });

        node.files.forEach(file => {
            const fileNode = {
                name: file,
                dirs: [],
                files: []
            };
            renderNode(fileNode, childrenContainer);
        });
    }

    li.addEventListener('click', function(event) {
        if (li.classList.contains('open')) {
            li.classList.remove('open');
        } else {
            li.classList.add('open');
        }
        event.stopPropagation();
    });

    parentElement.appendChild(li);
}
renderNode(node, parentElement)：该函数用于渲染每一个文件夹或文件的 li 元素。
首先创建一个 li 元素，根据节点类型（文件夹或文件）添加相应的样式类。
如果节点有子目录或文件，则创建子 ul 元素并递归渲染子节点。
添加点击事件监听器，点击时展开或收起子节点。
将渲染好的节点追加到父元素中。
```
4. 根节点
```javascript
const root = {
    name: 'root',
    dirs: Object.keys(data),
    files: []
};
```
>root 是文件树的根节点，它包含一个名为 root 的目录，dirs 存储所有子目录的名称，
> files 存储文件夹下的文件名称。
> 
此处 Object.keys(data) 用于获取 data 中所有子目录的名称。
## 数据结构
假设 tree.json 的结构如下所示：
```json
{
    "folder1": {
        "dirs": ["subfolder1", "subfolder2"],
        "files": ["file1.txt", "file2.txt"]
    },
    "folder2": {
        "dirs": [],
        "files": ["file3.txt"]
    },
    "folder3": {
        "dirs": ["subfolder3"],
        "files": []
    }
}
```
>每个文件夹（如 `folder1, folder2, folder3`）都包含两个属性：
dirs：包含子文件夹的名称数组。
files：包含文件名的数组。
# 功能说明
点击文件夹展开/收起：每个文件夹旁边都有一个 📁 图标，点击文件夹时会展开或收起其子文件夹和文件。
文件显示：
文件以 📄 图标显示，用户无法展开或收起文件。

样式适应不同设备：页面有响应式设计，支持不同屏幕大小的设备（如手机、平板）。
# 运行要求
tree.json 文件应包含与目录结构相关的数据，存放在网站根目录下。
需要支持 JavaScript 和 JSON 格式的浏览器。
本页面可通过静态网页服务器或本地开发环境加载。
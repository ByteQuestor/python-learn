# 文件树项目

此项目可以用来动态展示自己的资源

由`tree.py`输出json文件，然后由`index.html`渲染

改动说明：
父节点布局不变：

移除了 display: flex 和 align-items: center，确保文件夹和文件的父节点不会被拉伸或垂直居中，保持原有布局。
子节点的展开方式：

通过 li.open > ul 来控制子节点的展开和收起，display: block 显示子节点，display: none 隐藏子节点，确保父节点的位置不受影响。
缩进和样式：

子节点通过 margin-left: 20px 增加缩进，避免与父节点重叠。
```css
/* 文件和文件夹图标库 */
.icon {
    font-size: 20px;
    margin-right: 8px;
    display: inline-block;
    vertical-align: middle;
}

/* 文件夹图标 */
.icon-folder::before {
    content: '📁'; /* 文件夹图标 */
}

/* 文件图标 */
.icon-file::before {
    content: '📄'; /* 文件图标 */
}

/* 图片文件图标 */
.icon-image::before {
    content: '🖼'; /* 图片文件图标 */
}

/* 代码文件图标 */
.icon-code::before {
    content: '💻'; /* 代码文件图标 */
}

/* 文本文件图标 */
.icon-text-file::before {
    content: '📝'; /* 文本文件图标 */
}

/* 压缩文件图标 */
.icon-archive::before {
    content: '🗜'; /* 压缩文件图标 */
}

/* 音乐文件图标 */
.icon-music::before {
    content: '🎵'; /* 音乐文件图标 */
}

/* 视频文件图标 */
.icon-video::before {
    content: '🎥'; /* 视频文件图标 */
}

/* PDF 文件图标 */
.icon-pdf::before {
    content: '📚'; /* PDF 文件图标 */
}

/* Excel 文件图标 */
.icon-excel::before {
    content: '📊'; /* Excel 文件图标 */
}

/* Word 文件图标 */
.icon-word::before {
    content: '📑'; /* Word 文件图标 */
}

/* PPT 文件图标 */
.icon-ppt::before {
    content: '📊'; /* PowerPoint 文件图标 */
}

/* 链接文件图标 */
.icon-link::before {
    content: '🔗'; /* 链接图标 */
}

/* 文件夹打开图标 */
.icon-folder-open::before {
    content: '📂'; /* 打开状态的文件夹图标 */
}

/* 下载文件图标 */
.icon-download::before {
    content: '⬇️'; /* 下载图标 */
}

/* 上传文件图标 */
.icon-upload::before {
    content: '⬆️'; /* 上传图标 */
}
```

使用方法：
1. 引入 CSS 库：
将icon-library.css文件添加到HTML 中：
```html
<link rel="stylesheet" href="path/to/icon-library.css">
```
html
复制代码
<link rel="stylesheet" href="path/to/icon-library.css">
2. 在 HTML 中使用图标：
通过类名将图标应用到元素中。例如，显示文件夹、文件、PDF 和图片图标：

```html
复制代码
<!-- 文件夹图标 -->
<span class="icon icon-folder"></span>

<!-- 文件图标 -->
<span class="icon icon-file"></span>

<!-- PDF 文件图标 -->
<span class="icon icon-pdf"></span>

<!-- 图片文件图标 -->
<span class="icon icon-image"></span>

<!-- 代码文件图标 -->
<span class="icon icon-code"></span>

<!-- 压缩文件图标 -->
<span class="icon icon-archive"></span>

<!-- 音乐文件图标 -->
<span class="icon icon-music"></span>

<!-- 视频文件图标 -->
<span class="icon icon-video"></span>

<!-- Excel 文件图标 -->
<span class="icon icon-excel"></span>
```
图标库说明：
每个图标都有一个对应的类名，

例如:
`.icon-folder` 对应文件夹图标，
`.icon-file` 对应普通文件图标等。
可以通过 `font-size` 来调整图标的大小，默认大小为 `20px`。
每个图标前面都有 `::before` 伪元素来插入 `Unicode` 字符，这些字符表示了不同的文件类型图标。
可选的扩展：
# 更多的文件类型图标
可以参考 `Unicode Table` 或者使用更复杂的图标库， 
如 `Font Awesome` 或 `Material Icons`。

对于更复杂的图标和自定义样式，`Font Awesome` 提供了更丰富的图标集合和样式定制功能。

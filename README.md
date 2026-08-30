# HELEN — 印象旅行漫画

一个纯静态网站：真实的旅行摄影，被重新画成漫画。米色纸张、水墨、邮戳与印章红的设计语言，来自漫画作品本身。

无框架、无构建依赖，任何静态托管（GitHub Pages / Vercel / Netlify）都能直接部署。

## 目录结构

```
├── index.html          首页（主视觉 / 精选作品 / 引言）
├── work.html           作品总览（二十卷，错落网格）
├── work/*.html         20 个作品详情页（由脚本生成）
├── about.html          关于（创作理念 / 三步创作法 / 旅程年表）
├── journal.html        创作日记
├── contact.html        联系方式
├── css/style.css       全站样式（设计系统在文件顶部的 :root 变量里）
├── js/main.js          交互（加载动画 / 滚动显现 / 导航 / 光标等）
├── scripts/check_site.py 自动化站点检查（生成一致性 / 链接 / 图片尺寸）
├── assets/works/       网页用图（JPEG，由原 PNG 压缩而来）
├── assets/favicon.svg  网站图标（印章）
├── build_pages.py      作品页、sitemap、robots 生成脚本
├── sitemap.xml         搜索引擎站点地图（由脚本生成）
├── robots.txt          爬虫入口（由脚本生成）
├── _headers            Cloudflare Pages 安全头与缓存策略
└── 漫画作品/            原始 PNG 作品（不参与部署，保留原稿）
```

## 如何新增 / 修改作品

1. 把新作品图片压缩后放进 `assets/works/`（推荐命令：
   `sips -s format jpeg -s formatOptions 85 原图.png --out assets/works/新名字.jpg`）。
2. 打开 `build_pages.py`，在 `WORKS` 列表里按时间顺序插入一条记录
   （标题、地点、日期、坐标、副题、图片宽高、两段正文）。
3. 运行：

```bash
python3 build_pages.py
```

会重新生成 `work.html` 和全部 `work/*.html`（卷号、上一篇/下一篇自动排好）。
同时会更新 `sitemap.xml` 和 `robots.txt`。
首页 `index.html` 的精选卡片是手工挑选的，如需更换直接编辑即可。

## 自动化检查

```bash
python3 scripts/check_site.py
```

检查内容：

- `build_pages.py` 生成结果是否已同步到文件。
- `WORKS` 声明的图片尺寸是否和 `assets/works/*.jpg` 实际尺寸一致。
- 所有 HTML / CSS / JS 的本地引用是否存在。

## 本地预览

```bash
python3 -m http.server 8642
```

然后访问 http://localhost:8642 。

## 待办（部署前请修改）

- `contact.html` 里的邮箱 `hello@helen-diary.com` 和社交链接（目前是占位符 `#`）。
- 如需部署到 GitHub Pages 的子路径，页面内均为相对路径，无需改动。

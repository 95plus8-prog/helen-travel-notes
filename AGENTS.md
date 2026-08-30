# AGENTS.md

本项目是 HELEN 印象旅行漫画静态网站。接管开发时优先保持现有设计语言：米色纸张、水墨、邮戳、印章红、慢速动效、作品图让位于内容。

## 项目规则

- 默认用中文回复，结论优先。
- 这是纯静态站点，无 Node 构建链；不要引入框架，除非有明确需求。
- `work.html` 和 `work/*.html` 由 `build_pages.py` 生成，不能直接长期手改。
- 新增作品时先更新 `WORKS`，再运行 `python3 build_pages.py`。
- 原始 PNG 在 `漫画作品/`，不参与部署；网页用图在 `assets/works/`。
- GitHub Pages 部署在子路径，站内链接保持相对路径。
- Cloudflare Pages 是主站 canonical 候选：`https://helen-travel-notes.pages.dev/`。

## 常用命令

```bash
python3 build_pages.py
python3 scripts/check_site.py
python3 -m http.server 8642
git diff --check
```

## 验证要求

改动完成后至少运行：

```bash
python3 build_pages.py
python3 scripts/check_site.py
git diff --check
```

涉及布局或交互时，再用真实浏览器检查桌面和移动端视口。

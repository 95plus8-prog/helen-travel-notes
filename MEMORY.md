# MEMORY.md

## 项目当前认知

- 项目名：HELEN 印象旅行漫画网站。
- 仓库：`https://github.com/95plus8-prog/helen-travel-notes`。
- GitHub Pages：`https://95plus8-prog.github.io/helen-travel-notes/`。
- Cloudflare Pages：`https://helen-travel-notes.pages.dev/`。
- 类型：纯静态 HTML/CSS/JS + Python 生成脚本。
- 当前作品数：20 卷。
- 生成源：`build_pages.py` 的 `WORKS` 列表。
- 生成产物：`work.html`、`work/*.html`、`sitemap.xml`、`robots.txt`。

## 维护约定

- 先读目录、Git 状态、README、生成脚本，再改代码。
- 不直接编辑生成页作为长期修改；应改 `build_pages.py`。
- `.wrangler/` 是 Cloudflare 本地缓存，应忽略。
- 联系页邮箱和社交链接仍是占位内容，正式上线前需要用户提供真实信息。

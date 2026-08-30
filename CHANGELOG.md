# CHANGELOG.md

## 2026-08-30

- 接管项目并完成首次结构审计。
- `build_pages.py` 新增 `sitemap.xml` 与 `robots.txt` 生成。
- 新增 `scripts/check_site.py` 自动检查生成文件、内部引用和作品图片尺寸。
- 新增 Cloudflare Pages `_headers`，配置基础安全头和缓存策略。
- 更新 README 的作品数量、目录结构和验证命令。
- 新增 `AGENTS.md`、`MEMORY.md`、`TASKS.md` 作为后续维护入口。
- `.gitignore` 忽略 `.wrangler/` 本地缓存。

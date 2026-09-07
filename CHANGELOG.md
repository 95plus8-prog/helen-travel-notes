# CHANGELOG.md

## 2026-09-07

完成一次全量审计，并修掉其中两条 P0：

- `build_pages.py` 的 sitemap `<lastmod>` 由 `date.today()` 改为 `SITE_LASTMOD` 常量。
  原先每过一天重新生成的 sitemap 就和已提交版本不一致，`scripts/check_site.py` 必然报 stale。
- 全站 25 个页面加上 `<link rel="canonical">` 与 `og:url`，统一指向 Cloudflare Pages。
  解决 pages.dev 与 github.io 两个域名同时返回 200、内容完全一致的重复内容问题。
- `index.html` 的 JSON-LD `url` 由相对路径改为绝对地址。
- 修复前的完整快照：git tag `backup/pre-p0-20260907`。

## 2026-08-30

- 接管项目并完成首次结构审计。
- `build_pages.py` 新增 `sitemap.xml` 与 `robots.txt` 生成。
- 新增 `scripts/check_site.py` 自动检查生成文件、内部引用和作品图片尺寸。
- 新增 Cloudflare Pages `_headers`，配置基础安全头和缓存策略。
- 更新 README 的作品数量、目录结构和验证命令。
- 新增 `AGENTS.md`、`MEMORY.md`、`TASKS.md` 作为后续维护入口。
- `.gitignore` 忽略 `.wrangler/` 本地缓存。

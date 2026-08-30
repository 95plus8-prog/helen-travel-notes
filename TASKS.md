# TASKS.md

## 最高优先级

- [ ] 替换 `contact.html` 的邮箱和社交链接占位符。
- [ ] 决定主 canonical 域名：Cloudflare Pages 或 GitHub Pages。
- [ ] 真实浏览器检查首页、作品页、移动端菜单和图片加载表现。

## 下一步开发

- [ ] 给首页精选作品改成可从 `WORKS` 配置生成，减少手工同步。
- [ ] 为 `about.html` / `journal.html` 的内容建立数据源或生成脚本。
- [x] 增加 `_headers`，给 Cloudflare Pages 配置基础安全与缓存头。
- [ ] 增加 Open Graph 绝对图片 URL，改善社交分享卡片。
- [ ] 添加 404 页面。

## 已完成

- [x] 站点生成流程扩展到 `sitemap.xml` 和 `robots.txt`。
- [x] 新增 `scripts/check_site.py`，检查生成一致性、内部引用和图片尺寸。
- [x] 更新 README，使作品数量和自动化流程与当前项目一致。

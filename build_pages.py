# -*- coding: utf-8 -*-
"""HELEN 印象旅行漫画 — 作品页生成脚本。
数据集中在 WORKS 里；运行后重新生成 work.html 与 work/*.html。
新增作品：把图片放进 assets/works/，在 WORKS 里加一条，重跑 python3 build_pages.py。
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

CN_NUM = ["一","二","三","四","五","六","七","八","九","十",
          "十一","十二","十三","十四","十五","十六","十七","十八","十九","二十"]

# slug, 标题, 地点(展示), 国家/城市短标签, 日期(展示), 坐标, 副题(一句), 尺寸(w,h), 正文两段, 备注图(可选: (文件,说明))
WORKS = [
    dict(slug="amsterdam", title="阿姆斯特丹", place="荷兰 · 阿姆斯特丹", tag="荷兰", date="2023.05",
         coords="52.3676° N, 4.9041° E", sub="在水之上，与时光相遇。", w=1024, h=1536,
         p1="那天沿着运河一直走，山形墙的老房子一栋挨着一栋，倒影在水面轻轻晃。我靠在铁栏杆上拍了张照，风把头发吹乱了也没管。",
         p2="回来重画这张照片时，我把房子画成了淡淡的素描，只给那件薄荷绿的毛衣留了颜色——因为记忆里，那天的阿姆斯特丹就是这样：城市是背景，心情才是主角。"),
    dict(slug="montmartre", title="遇见巴黎", place="法国 · 巴黎 · 蒙马特", tag="法国", date="2024.05",
         coords="48.8867° N, 2.3431° E", sub="把浪漫装进记忆里。", w=941, h=1672,
         p1="爬上蒙马特高地的时候，圣心堂白色的穹顶忽然出现在台阶尽头。照片里我提着帆布袋站在石板路上，鞋底还沾着面包店门口的面粉。",
         p2="画的时候，我让教堂慢慢淡成铅笔的痕迹，只留下那件鹅黄色的开衫。巴黎的浪漫不在明信片里，在你恰好路过的那一刻。"),
    dict(slug="paris-street", title="巴黎街角", place="法国 · 巴黎", tag="法国", date="2024.05",
         coords="48.8584° N, 2.2945° E", sub="Collect moments, not things.", w=864, h=1536,
         p1="过马路时回头，埃菲尔铁塔正好卡在两排奥斯曼公寓中间。绿灯还剩三秒，我举起手机按下快门——这是那趟旅行里最匆忙、也最喜欢的一张照片。",
         p2="重画它的时候，我在页边加上了当天的清单：好天气、City Walk、铁塔、咖啡。像日记一样，把一个普通的街角，变成只属于我的一页。"),
    dict(slug="sunny-day", title="把晴天带在身上", place="法国 · 巴黎 · 圣心堂", tag="法国", date="2024.05",
         coords="48.8867° N, 2.3431° E", sub="把晴天，带在身上。", w=971, h=1619,
         p1="原本的照片是阴天：灰色的圣心堂，灰色的台阶，灰色的鸽子。只有我肩上的橘色托特包，倔强地亮着。",
         p2="所以这一张我画成了拼贴——把拱门里的天空剪掉，补上一块最饱和的蓝。照片记录天气，画可以修改天气。晴天是自己带的。"),
    dict(slug="zaandam", title="風車之國", place="荷兰 · 赞丹", tag="荷兰", date="2024.05",
         coords="52.450° N, 4.820° E", sub="在风里，遇见生活的温柔。", w=941, h=1672,
         p1="赞丹的风很大，风车的影子从水面一直铺到脚边。我坐在木栈道上休息，朋友随手帮我拍了一张。",
         p2="画里我把风车画成了旧钢笔画的样子，像从一封多年前的航空信里掉出来的。红色的冲锋衣是那天唯一的暖色，也是记忆里最清楚的部分。"),
    dict(slug="lijiang", title="時光留白", place="中国 · 云南 · 丽江", tag="中国", date="2024.05.18",
         coords="26°52′ N, 100°13′ E", sub="把时间留在古城的每一个转角。", w=941, h=1672,
         p1="丽江古城的下午，客栈的木牌匾在风里轻响，红灯笼挂在檐角。我拎着刚买的花布袋，笑得比阳光还开。",
         p2="这一张几乎不用改动构图——古城本来就长得像一幅画。我只是把喧闹的游客都留在了画外，让时光留白。"),
    dict(slug="jiangnan", title="江南印记", place="中国 · 江南水乡", tag="中国", date="2024.07",
         coords="30.7386° N, 120.6371° E", sub="风停在这里，记忆却继续向前。", w=941, h=1672,
         p1="石桥的台阶被岁月磨得发亮，檐角挂着「江南人家」的木牌。我穿着波点长裙站在桥头回头看镜头，那天热得像蒸笼，照片里却看不出来。",
         p2="画里的水乡是灰色的素描，只有人是彩色的。有些地方会留在心里很久很久——大概就是这个意思。"),
    dict(slug="old-street", title="留下的風景", place="中国 · 西南老街", tag="中国", date="2024.07.24",
         coords="27°59′ N, 102°42′ E", sub="留下的風景，是時間的樣子。", w=941, h=1672,
         p1="那条老街快要拆了。木楼歪着，招牌斑驳，卖绣品的阿婆说这些花包再不买就没有了。我买了一个最花的，背着它拍了这张照片。",
         p2="Some places stay with you long after you leave. 画完这一张我才明白：照片留住的是街，画留住的是舍不得。"),
    dict(slug="giethoorn", title="羊角村", place="荷兰 · 羊角村", tag="荷兰", date="2025.04",
         coords="52.7412° N, 6.0527° E", sub="慢下来，让时光在水面上轻轻流淌。", w=1024, h=1536,
         p1="四月的羊角村，河道比街道多。我们租了一条小红船，慢慢开过茅草屋顶和小木桥，快门按下时我正回头喊朋友看岸边的鸭子。",
         p2="重画的时候，我把整个村子画成了水彩晕开的样子，只有小船是红的。在水乡的静谧里，遇见生活最温柔的样子。"),
    dict(slug="fujiyoshida", title="把晴天收进记忆", place="日本 · 山梨 · 富士吉田", tag="日本", date="2025.04.06",
         coords="35.498° N, 138.727° E", sub="在风里旅行。", w=1023, h=1537,
         p1="本町商店街的电线杆和灯笼一路排过去，街的尽头就是富士山——雪顶白得不太真实。我裹紧围巾往前走，相机就挂在胸前，随时准备按下去。",
         p2="画里我把商店街淡成了钢笔速写，富士山淡成了一层铅灰，只有人是彩色的。旅途会结束，但记忆会留下。"),
    dict(slug="barcelona-guell", title="遇见巴塞罗那", place="西班牙 · 巴塞罗那 · 奎尔公园", tag="西班牙", date="2025.05",
         coords="41.3851° N, 2.1734° E", sub="在温柔的时光里。", w=1024, h=1536,
         p1="奎尔公园的马赛克长椅在太阳下闪闪发光，高迪的糖果屋就在身后。我坐在长椅上，手搭着彩色的瓷砖，请路人帮忙拍了这张。",
         p2="画里我让糖果屋淡成了图纸上的铅笔稿——高迪的建筑本来就像没画完的梦。Sunny day，2025 年 5 月，巴塞罗那。"),
    dict(slug="casa-batllo", title="巴特罗之家", place="西班牙 · 巴塞罗那", tag="西班牙", date="2025.05",
         coords="41.3917° N, 2.1650° E", sub="一栋会呼吸的房子，和一辆等红灯的出租车。", w=971, h=1619,
         p1="在格拉西亚大道的路口，我举着相机等巴特罗之家前面的人群散开。人群一直没散，倒是一辆黄色出租车停进了取景框——反而成了整张照片的点睛之笔。",
         p2="画成版画风格之后，骷髅阳台和龙脊屋顶都变成了黑白的肌理，只有出租车还是黄色。有时候，意外才是构图之神。"),
    dict(slug="still-passing", title="Still Passing", place="西班牙 · 巴塞罗那", tag="西班牙", date="2025.05",
         coords="41.3917° N, 2.1650° E", sub="城市在动，房子在等。", w=1619, h=971,
         p1="同一个路口的另一张照片：车流拖出长长的虚影，巴特罗之家亮着几扇橘黄色的窗，在暮色里一动不动。",
         p2="STILL，PASSING——静止的和经过的。旅行大概就是在这两个词之间：我们都是经过的人，而风景替我们留下来。"),
    dict(slug="sagrada", title="未完成的抵达", place="西班牙 · 巴塞罗那 · 圣家堂", tag="西班牙", date="2025.05",
         coords="41.4036° N, 2.1744° E", sub="未完成，也是一种抵达。", w=971, h=1619,
         p1="站在圣家堂脚下的那个傍晚，塔尖上还架着橘色的塔吊。一百四十年了，它还没完工，可没有人觉得它不完整。",
         p2="照片里我只是个小小的背影。画的时候我把自己也画成了淡淡的墨色——在未完成的伟大面前，谁不是路过的一笔。"),
    dict(slug="jinshan", title="金山塔影", place="中国 · 镇江 · 金山寺", tag="中国", date="2025.05.31",
         coords="32.1894° N, 119.4253° E", sub="把时光留在印象深处。", w=941, h=1672,
         p1="金山寺的塔在树影里一层层往上收，石栏杆被香火熏了几百年。我靠着栏杆站了一会儿，风里全是香和初夏的味道。",
         p2="这张照片本来平平无奇，画成水墨之后，塔忽然有了「塔影」——旅人记，记的从来不是景点，是那一刻的自己。"),
    dict(slug="tokyo", title="東京", place="日本 · 东京 · 新宿", tag="日本", date="2025.06",
         coords="35.6938° N, 139.7036° E", sub="有些風景，只能遇見一次。", w=941, h=1672,
         p1="歌舞伎町的白天，巨大的广告牌一层叠着一层。我穿着红色的冲锋衣走过路口，朋友在天桥上按下快门——照片里的我小得几乎找不到。",
         p2="画里我把整栋楼画成了褪色的印刷品，像旧杂志的封面。遇見・未來——有些风景只能遇见一次，所以要画下来。"),
    dict(slug="arrival", title="抵达之后", place="日本 · 东京", tag="日本", date="2025.06",
         coords="35.6895° N, 139.6917° E", sub="抵达之后，城市仍比我更快。", w=971, h=1619,
         p1="从机场进城的那个傍晚，高楼在雨里往后倒退。我拎着帆布袋站在路口，忽然觉得自己像一滴慢下来的雨。",
         p2="这是整个系列里最安静的一张。没有地标，没有攻略——只有抵达之后，那种城市仍比我更快的、微小的失重感。"),
    dict(slug="kiyomizu", title="清水寺", place="日本 · 京都", tag="日本", date="2025.06",
         coords="34.9949° N, 135.7850° E", sub="檐上的人间。", w=1619, h=971,
         p1="清水的舞台上永远挤满了人，可只要把镜头抬高一点，就只剩下飞檐、三重塔，和排成一线的小小人影。",
         p2="画成浮世绘一样的横卷之后，人群变成了檐下的墨点。京都教会我的事：热闹和清净，往往只隔一个抬头。"),
]

NAV = '''  <a href="#main" class="skip-link">跳至内容</a>

  <div class="loader" data-loader aria-hidden="true">
    <div class="loader-seal">印</div>
    <div class="loader-mark">HELEN</div>
    <div class="loader-track"><div class="loader-progress" data-loader-progress></div></div>
  </div>

  <div class="scroll-progress" data-scroll-progress></div>

  <nav class="nav" data-nav aria-label="主导航">
    <a href="{root}index.html" class="nav-mark"><span class="seal-dot">印</span>HELEN</a>
    <button class="nav-toggle" data-nav-toggle aria-expanded="false" aria-controls="nav-links">菜单</button>
    <ul class="nav-links" data-nav-links id="nav-links">
      <li><a href="{root}work.html"{active_work}>作品</a></li>
      <li><a href="{root}about.html"{active_about}>关于</a></li>
      <li><a href="{root}journal.html"{active_journal}>日记</a></li>
      <li><a href="{root}contact.html"{active_contact}>联系</a></li>
    </ul>
  </nav>
'''

FOOTER = '''  <footer class="footer">
    <div class="container">
      <p class="footer-line reveal">看过的风景，画下来才算数。</p>
      <div class="footer-meta reveal reveal-1">
        <span>&copy; 2026 HELEN · 印象旅行漫画</span>
        <a href="{root}work.html" class="link-underline">作品</a>
        <a href="{root}about.html" class="link-underline">关于</a>
        <a href="{root}journal.html" class="link-underline">日记</a>
        <a href="{root}contact.html" class="link-underline">联系</a>
      </div>
    </div>
  </footer>

  <script src="{root}js/main.js"></script>
</body>
</html>
'''

HEAD = '''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="{ogtype}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{ogimage}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<meta name="theme-color" content="#F5EFE2">
<link rel="stylesheet" href="{root}css/style.css">
</head>
<body>
'''


def nav(root, active=""):
    keys = {k: "" for k in ["work", "about", "journal", "contact"]}
    if active in keys:
        keys[active] = ' class="is-active"'
    return NAV.format(root=root,
                      active_work=keys["work"], active_about=keys["about"],
                      active_journal=keys["journal"], active_contact=keys["contact"])


def detail_page(i, w):
    prev_w = WORKS[(i - 1) % len(WORKS)]
    next_w = WORKS[(i + 1) % len(WORKS)]
    vol = "卷" + CN_NUM[i]
    head = HEAD.format(title=f"{w['title']} — HELEN 印象旅行漫画",
                       desc=w["sub"], ogtype="article",
                       ogimage=f"../assets/works/{w['slug']}.jpg", root="../")
    variant_html = ""
    if w.get("variant"):
        vf, vc = w["variant"]
        variant_html = f'''
      <figure class="detail-spread reveal">
        <div class="work-card-frame" data-no="VARIANT">
          <div class="frame-clip">
            <img class="img-reveal" loading="lazy" decoding="async" src="../assets/works/{vf}" alt="《{w['title']}》的另一个版本">
          </div>
        </div>
        <figcaption class="detail-spread-caption type-meta">{vc}</figcaption>
      </figure>'''

    return head + nav("../", "work") + f'''
  <main id="main">
    <header class="detail-hero-content">
      <div class="container">
        <span class="detail-vol reveal">{vol} · TRAVEL NOTES</span>
        <h1 class="type-display reveal reveal-1">{w['title']}</h1>
        <p class="detail-sub reveal reveal-2">{w['sub']}</p>
      </div>
    </header>

    <section class="detail-hero reveal">
      <div class="work-card-frame" data-no="NO.{i+1:03d}">
        <div class="frame-clip">
          <img loading="eager" decoding="async" width="{w['w']}" height="{w['h']}"
               src="../assets/works/{w['slug']}.jpg" alt="漫画《{w['title']}》：{w['sub']}">
        </div>
      </div>
    </section>

    <div class="detail-meta-row reveal">
      <div><span class="type-meta">日期</span><span class="type-h3">{w['date']}</span></div>
      <div><span class="type-meta">地点</span><span class="type-h3">{w['place']}</span></div>
      <div><span class="type-meta">坐标</span><span class="type-h3" style="font-family:var(--mono);font-size:.95rem;">{w['coords']}</span></div>
      <div><span class="type-meta">卷号</span><span class="type-h3">{vol}</span></div>
    </div>

    <article class="detail-body">
      <div class="container prose">
        <p class="type-body reveal">{w['p1']}</p>
        <p class="type-body reveal">{w['p2']}</p>
      </div>
      <div class="container">{variant_html}
      </div>
    </article>

    <nav class="container detail-nav" aria-label="更多作品">
      <a href="{prev_w['slug']}.html" class="link-underline" data-cursor-hover>
        <span class="type-meta dir">← 上一篇</span>
        <span class="type-h3">{prev_w['title']}</span>
      </a>
      <a href="{next_w['slug']}.html" class="link-underline to-right" data-cursor-hover>
        <span class="type-meta dir">下一篇 →</span>
        <span class="type-h3">{next_w['title']}</span>
      </a>
    </nav>
  </main>

''' + FOOTER.format(root="../")


def gallery_item(i, w, cls, delay):
    vol = "卷" + CN_NUM[i]
    d = f" reveal-{delay}" if delay else ""
    return f'''
          <figure class="gallery-item {cls} reveal{d}">
            <a href="work/{w['slug']}.html" class="work-card" data-cursor-hover>
              <div class="work-card-frame" data-no="NO.{i+1:03d}">
                <div class="frame-clip">
                  <img class="img-reveal" loading="lazy" decoding="async" width="{w['w']}" height="{w['h']}"
                       src="assets/works/{w['slug']}.jpg" alt="漫画《{w['title']}》：{w['sub']}">
                </div>
              </div>
              <figcaption class="work-card-meta">
                <span class="work-card-title">{w['title']}</span>
                <span class="work-card-tags">{vol} · {w['tag']} · {w['date'][:4]}</span>
              </figcaption>
            </a>
          </figure>'''


def work_page():
    # 错落网格节奏；横幅图用 g-wide
    pattern = ["g-lg", "g-sm g-offset", "g-md", "g-xl g-offset", "g-md", "g-lg g-offset", "g-sm"]
    items, pi = [], 0
    for i, w in enumerate(WORKS):
        if w["w"] > w["h"]:
            cls = "g-wide"
        else:
            cls = pattern[pi % len(pattern)]
            pi += 1
        items.append(gallery_item(i, w, cls, i % 3))
    head = HEAD.format(title="作品 — HELEN 印象旅行漫画",
                       desc="十八段真实的旅程，事后画成漫画：荷兰、法国、西班牙、日本，以及中国的古城与老街。",
                       ogtype="website", ogimage="assets/works/giethoorn.jpg", root="")
    return head + nav("", "work") + f'''
  <main id="main">
    <header class="section-tight" style="padding-top: calc(var(--sp-9) + var(--sp-4));">
      <div class="container">
        <p class="type-eyebrow reveal">TRAVEL NOTES · 全部作品</p>
        <h1 class="type-display mt-3 reveal reveal-1" style="max-width:900px;">十八段旅程，<br>先拍下，再画一遍。</h1>
        <p class="type-body mt-5 reveal reveal-2" style="max-width:var(--body-w);">
          每一幅漫画都始于一张真实的旅行照片——那天、那个地方、真实发生过的一刻。
          回来之后，我把它们重新画了一遍，留住相机来不及说的部分。
        </p>
      </div>
    </header>

    <section class="section">
      <div class="container">
        <div class="gallery-grid">{"".join(items)}
        </div>
      </div>
    </section>
  </main>

''' + FOOTER.format(root="")


def main():
    os.makedirs(os.path.join(ROOT, "work"), exist_ok=True)
    for i, w in enumerate(WORKS):
        path = os.path.join(ROOT, "work", w["slug"] + ".html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(detail_page(i, w))
    with open(os.path.join(ROOT, "work.html"), "w", encoding="utf-8") as f:
        f.write(work_page())
    print(f"generated {len(WORKS)} detail pages + work.html")


if __name__ == "__main__":
    main()

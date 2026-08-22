/* HELEN — 印象旅行漫画
   共用交互：无框架、无构建。所有动效都保持安静、缓慢、不打扰。 */

(function () {
  'use strict';

  var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var isFinePointer = window.matchMedia('(pointer: fine)').matches;

  /* ---------------- 加载动画 ---------------- */
  function initLoader() {
    var loader = document.querySelector('[data-loader]');
    if (!loader) return;
    var bar = loader.querySelector('[data-loader-progress]');
    document.documentElement.style.overflow = 'hidden';

    function finish() {
      if (bar) bar.style.width = '100%';
      window.setTimeout(function () {
        loader.classList.add('is-hidden');
        document.documentElement.style.overflow = '';
      }, prefersReducedMotion ? 0 : 450);
      window.setTimeout(function () {
        if (loader.parentNode) loader.parentNode.removeChild(loader);
      }, prefersReducedMotion ? 50 : 1500);
    }

    if (bar) window.requestAnimationFrame(function () { bar.style.width = '72%'; });

    if (document.readyState === 'complete') {
      window.setTimeout(finish, 260);
    } else {
      window.addEventListener('load', function () { window.setTimeout(finish, 180); });
      window.setTimeout(finish, 1800); // 兜底
    }
  }

  /* ---------------- 导航：滚动变实 + 移动端菜单 ---------------- */
  function initNav() {
    var nav = document.querySelector('[data-nav]');
    if (!nav) return;

    function onScroll() {
      nav.classList.toggle('is-solid', window.scrollY > 24);
    }
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });

    var toggle = document.querySelector('[data-nav-toggle]');
    var links = document.querySelector('[data-nav-links]');
    if (toggle && links) {
      toggle.addEventListener('click', function () {
        var open = links.classList.toggle('is-open');
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        toggle.textContent = open ? '关闭' : '菜单';
        document.documentElement.style.overflow = open ? 'hidden' : '';
      });
      links.querySelectorAll('a').forEach(function (a) {
        a.addEventListener('click', function () {
          links.classList.remove('is-open');
          toggle.setAttribute('aria-expanded', 'false');
          toggle.textContent = '菜单';
          document.documentElement.style.overflow = '';
        });
      });
    }
  }

  /* ---------------- 阅读进度条 ---------------- */
  function initScrollProgress() {
    var bar = document.querySelector('[data-scroll-progress]');
    if (!bar) return;
    function onScroll() {
      var h = document.documentElement;
      var height = h.scrollHeight - h.clientHeight;
      bar.style.transform = 'scaleX(' + (height > 0 ? h.scrollTop / height : 0) + ')';
    }
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------------- 滚动显现 ---------------- */
  function initReveal() {
    var items = document.querySelectorAll('.reveal');
    if (!items.length) return;
    if (prefersReducedMotion || !('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('is-visible'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    items.forEach(function (el) { io.observe(el); });
  }

  /* ---------------- 图片由虚到实 ---------------- */
  function initImageReveal() {
    document.querySelectorAll('img.img-reveal').forEach(function (img) {
      if (img.complete && img.naturalWidth > 0) {
        img.classList.add('is-loaded');
      } else {
        img.addEventListener('load', function () { img.classList.add('is-loaded'); }, { once: true });
      }
    });
  }

  /* ---------------- 自定义光标（印章红点） ---------------- */
  function initCursor() {
    if (!isFinePointer || prefersReducedMotion) return;
    document.body.classList.add('has-custom-cursor');

    var dot = document.createElement('div');
    dot.className = 'cursor-dot';
    var ring = document.createElement('div');
    ring.className = 'cursor-ring';
    document.body.appendChild(dot);
    document.body.appendChild(ring);

    var mouse = { x: innerWidth / 2, y: innerHeight / 2 };
    var ringPos = { x: mouse.x, y: mouse.y };

    window.addEventListener('mousemove', function (e) {
      mouse.x = e.clientX;
      mouse.y = e.clientY;
      dot.style.transform = 'translate(' + mouse.x + 'px,' + mouse.y + 'px) translate(-50%,-50%)';
    });

    (function raf() {
      ringPos.x += (mouse.x - ringPos.x) * 0.16;
      ringPos.y += (mouse.y - ringPos.y) * 0.16;
      ring.style.transform = 'translate(' + ringPos.x + 'px,' + ringPos.y + 'px) translate(-50%,-50%)';
      window.requestAnimationFrame(raf);
    })();

    document.querySelectorAll('a, button, [data-cursor-hover]').forEach(function (el) {
      el.addEventListener('mouseenter', function () { ring.classList.add('is-active'); });
      el.addEventListener('mouseleave', function () { ring.classList.remove('is-active'); });
    });

    document.addEventListener('mouseleave', function () { dot.style.opacity = ring.style.opacity = '0'; });
    document.addEventListener('mouseenter', function () { dot.style.opacity = ring.style.opacity = '1'; });
  }

  /* ---------------- 磁吸按钮 ---------------- */
  function initMagnetic() {
    if (!isFinePointer || prefersReducedMotion) return;
    document.querySelectorAll('.magnetic').forEach(function (el) {
      var strength = 16;
      el.addEventListener('mousemove', function (e) {
        var r = el.getBoundingClientRect();
        var x = e.clientX - r.left - r.width / 2;
        var y = e.clientY - r.top - r.height / 2;
        el.style.transform = 'translate(' + (x / r.width) * strength + 'px,' + (y / r.height) * strength + 'px)';
      });
      el.addEventListener('mouseleave', function () { el.style.transform = 'translate(0,0)'; });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initLoader();
    initNav();
    initScrollProgress();
    initReveal();
    initImageReveal();
    initCursor();
    initMagnetic();
  });
})();

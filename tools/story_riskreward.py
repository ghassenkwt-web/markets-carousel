# Story-format carousel (one topic, deep dive). Reuses design system from build.py.
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
_src = (HERE / "build.py").read_text(encoding="utf-8").split("slides = []")[0]
exec(_src)  # gives: css, foot, L, TOTAL, ROOT, OUT, sync_playwright

SRC = "المصادر: " + '<span class="ltr" dir="ltr">Seeking Alpha · CNBC · NPR</span>'

def stat(label, value, sub, cls="gold"):
    return f"""
<div class="card" style="padding:28px 40px;margin-top:20px">
  <div style="display:flex;justify-content:space-between;align-items:baseline"><div style="font-size:38px;font-weight:900">{label}</div><div class="{cls}" style="font-size:64px;font-weight:900">{L(value)}</div></div>
  <div style="font-size:29px;color:#9FB0CB;line-height:1.5;margin-top:6px">{sub}</div>
</div>"""

def step(day, title, val, cls, last=False):
    return f"""
<div style="display:flex;gap:30px;align-items:stretch;margin-top:0;position:relative">
  <div style="display:flex;flex-direction:column;align-items:center;min-width:34px">
    <div style="width:34px;height:34px;border-radius:50%;background:{'#FF5A67' if cls=='red' else '#F4B740' if cls=='gold' else '#2ED3A0'};border:6px solid #0B1220;box-shadow:0 0 0 3px #26324D"></div>
    {'' if last else '<div style="flex:1;width:4px;background:#26324D;margin-top:6px"></div>'}
  </div>
  <div class="card" style="flex:1;padding:22px 34px;margin-bottom:22px;display:flex;justify-content:space-between;align-items:center">
    <div><div class="muted" style="font-size:26px">{day}</div><div style="font-size:36px;font-weight:900;line-height:1.3">{title}</div></div>
    <div class="{cls}" style="font-size:52px;font-weight:900">{L(val)}</div>
  </div>
</div>"""

def point(n, t, b):
    return f"""
<div class="card" style="padding:30px 40px;margin-top:22px;display:flex;gap:30px;align-items:flex-start">
  <div style="min-width:78px;height:78px;border-radius:22px;background:rgba(244,183,64,.14);border:2px solid rgba(244,183,64,.4);color:#F4B740;font-size:48px;font-weight:900;display:flex;align-items:center;justify-content:center">{n}</div>
  <div><div style="font-size:40px;font-weight:900;line-height:1.3">{t}</div><div style="font-size:30px;color:#9FB0CB;line-height:1.55;margin-top:8px">{b}</div></div>
</div>"""

def rule(n, t, b):
    return f"""
<div style="display:flex;gap:28px;align-items:flex-start;margin-top:40px">
  <div style="min-width:72px;height:72px;border-radius:50%;background:#F4B740;color:#0B1220;font-size:44px;font-weight:900;display:flex;align-items:center;justify-content:center">{n}</div>
  <div><div style="font-size:40px;font-weight:900">{t}</div><div style="font-size:30px;color:#9FB0CB;line-height:1.5;margin-top:4px">{b}</div></div>
</div>"""

def f(n, src=SRC):
    return foot(n, src)




S = []
E="محتوى تعليمي"
def opt(l,t): return f'<div class="card" style="padding:26px 40px;margin-top:20px;display:flex;gap:28px;align-items:center"><div style="min-width:76px;height:76px;border-radius:50%;background:#F4B740;color:#0B1220;font-size:46px;font-weight:900;display:flex;align-items:center;justify-content:center">{l}</div><div style="font-size:42px;font-weight:900">{t}</div></div>'
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">درس التداول</span><span>الأحد 22 نوفمبر 2026</span></div>
 <div style="margin-top:130px;position:relative">
  <div style="font-size:50px;color:#B7C3DA;font-weight:700">يمكنك أن تخسر</div>
  <div style="direction:rtl;text-align:right;font-size:190px;font-weight:900;line-height:1.1"><span class="red">6</span><span style="color:#8FA0BC;font-size:80px"> من </span><span>10</span></div>
  <h1 style="font-size:84px;margin-top:10px">من صفقاتك <span class="gold">وتبقى رابحاً</span></h1>
  <p style="font-size:40px;color:#B7C3DA;margin-top:34px;line-height:1.55;font-weight:400">السر في معادلة واحدة بسيطة.</p>
 </div>
 <div style="position:absolute;left:84px;bottom:130px;font-size:36px;color:#8FA0BC;font-weight:700">اسحب للمزيد ←</div>
 {f(1, E)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">المفهوم</span><span>المخاطرة إلى العائد</span></div>
 <h2 style="margin-top:60px">ما هي نسبة<br><em>المخاطرة إلى العائد؟</em></h2>
 <div class="card" style="padding:40px;margin-top:36px">
  <div style="font-size:38px;font-weight:900;line-height:1.6">هي مقارنة ما <span class="red">تخاطر بخسارته</span> بما <span class="green">تتوقع ربحه</span> في الصفقة الواحدة.</div>
 </div>
 <div class="card" style="padding:34px 40px;margin-top:26px">
  <div class="muted" style="font-size:28px">مثال</div>
  <div style="font-size:36px;font-weight:900;line-height:1.6;margin-top:6px">تخاطر بـ {L("100")} لتربح {L("200")} ← النسبة <span class="gold">{L("1:2")}</span></div>
 </div>
 {f(2, E)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">مثال حسابي</span><span>افتراضي للتوضيح</span></div>
 <h2 style="margin-top:50px">10 صفقات<br><em>بنسبة {L("1:2")}</em></h2>
 <div style="position:relative;margin-top:14px">
  {stat("4 صفقات رابحة", "+800", "4 × 200 = 800", "green")}
  {stat("6 صفقات خاسرة", "−600", "6 × 100 = 600", "red")}
  {stat("الصافي", "+200", "رغم أن الخاسرة أكثر من الرابحة.", "gold")}
 </div>
 {f(3, E)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">نسبة النجاح</span><span>الحد الأدنى للتعادل</span></div>
 <h2 style="margin-top:50px">كم صفقة رابحة<br><em>تحتاج؟</em></h2>
 <div style="position:relative;margin-top:16px">
  {stat("نسبة 1:1", "50%", "تحتاج رابحة واحدة من كل صفقتين.", "red")}
  {stat("نسبة 1:2", "33.3%", "تحتاج رابحة واحدة من كل ثلاث.", "gold")}
  {stat("نسبة 1:3", "25%", "تحتاج رابحة واحدة من كل أربع.", "green")}
 </div>
 <p style="font-size:28px;color:#8FA0BC;margin-top:30px">قبل احتساب العمولات والانزلاق السعري.</p>
 {f(4, E)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">التطبيق</span><span>3 خطوات</span></div>
 <h2 style="margin-top:50px">كيف تطبّقها<br><em>قبل الدخول؟</em></h2>
 <div style="position:relative;margin-top:16px">
  {point("1","حدّد وقف الخسارة أولاً","اعرف أقصى مبلغ أنت مستعد لخسارته.")}
  {point("2","حدّد هدف الربح","على مستوى واقعي يدعمه تحليلك.")}
  {point("3","احسب النسبة","إذا كانت أقل من حدك الأدنى فتجاوز الصفقة.")}
 </div>
 {f(5, E)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">تنبيه</span><span>لا تكتفِ بالنسبة</span></div>
 <h2 style="margin-top:80px">النسبة الجيدة<br><em>لا تضمن الربح</em></h2>
 <div class="card" style="padding:36px 40px;margin-top:40px;font-size:36px;line-height:1.7;color:#B7C3DA">الهدف البعيد جداً قد لا يتحقق، فتنخفض نسبة نجاحك. اختر أهدافاً <span class="gold">واقعية</span>، وراعِ العمولات والانزلاق، والتزم بحجم صفقة ثابت ومحسوب.</div>
 {f(6, E)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">ما رأيك؟</span><span>الأحد 22 نوفمبر</span></div>
 <h1 style="font-size:80px;margin-top:60px">ما الحد الأدنى<br><span class="gold">لنسبتك؟</span></h1>
 <div style="margin-top:20px">{opt("أ", L("1:1"))}{opt("ب", L("1:2"))}{opt("ج", "1:3 أو أكثر".replace("1:3", L("1:3")))}</div>
 <p style="font-size:36px;color:#F4B740;margin-top:30px;font-weight:900">اكتب حرفك في التعليقات 👇</p>
 <p style="font-size:23px;color:#8FA0BC;margin-top:18px;line-height:1.6">⚠ المحتوى تعليمي وليس توصية استثمارية. الأمثلة افتراضية للتوضيح فقط. التداول ينطوي على مخاطر وقد تخسر جزءاً من رأس مالك أو كله.</p>
 {f(7, E)}
</section>""")

html = f"<!doctype html><html lang='ar' dir='rtl'><head><meta charset='utf-8'><style>{css}</style></head><body>{''.join(S)}</body></html>"
(ROOT / "story.html").write_text(html, encoding="utf-8")
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto(f"file://{ROOT}/story.html")
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(500)
    for i, el in enumerate(pg.query_selector_all(".slide"), 1):
        el.screenshot(path=str(OUT / f"slide-{i}.png"))
    b.close()
print("done")

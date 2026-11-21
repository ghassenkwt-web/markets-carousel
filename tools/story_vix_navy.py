# Story-format carousel (one topic, deep dive). Reuses design system from build.py.
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
_src = (HERE / "build.py").read_text(encoding="utf-8").split("slides = []")[0]
exec(_src)  # gives: css, foot, L, TOTAL, ROOT, OUT, sync_playwright

SRC = "المصادر: " + '<span class="ltr" dir="ltr">Schwab · CNBC · NPR</span>'

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
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">مؤشر الخوف</span><span>الأحد ٢٢ نوفمبر ٢٠٢٦</span></div>
 <div style="margin-top:130px;position:relative">
  <div style="font-size:48px;color:#B7C3DA;font-weight:700">قفز في أسبوع واحد من</div>
  <div style="direction:ltr;text-align:right;font-size:200px;font-weight:900;line-height:1.1"><span style="color:#8FA0BC">20</span> <span class="gold">→ 37+</span></div>
  <h1 style="font-size:104px;margin-top:10px">{L("VIX")} <span class="gold">يدق الجرس</span></h1>
  <p style="font-size:40px;color:#B7C3DA;margin-top:34px;line-height:1.55;font-weight:400">ماذا يعني هذا الرقم؟ ولماذا يهمك؟</p>
 </div>
 <div style="position:absolute;left:84px;bottom:130px;font-size:36px;color:#8FA0BC;font-weight:700">اسحب للمزيد ←</div>
 {f(1)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">المفهوم</span><span>ما هو؟</span></div>
 <h2 style="margin-top:60px">ما هو <em>{L("VIX")}؟</em></h2>
 <div class="card" style="padding:40px;margin-top:40px">
  <div style="font-size:42px;font-weight:900;line-height:1.5">يُعرف بـ«<span class="gold">مؤشر الخوف</span>».</div>
  <div style="font-size:34px;color:#B7C3DA;line-height:1.7;margin-top:14px">يقيس مدى التقلب الذي يتوقعه المستثمرون في مؤشر {L("S&amp;P 500")} خلال الـ٣٠ يوماً القادمة.</div>
 </div>
 <div class="card" style="padding:34px 40px;margin-top:26px;font-size:38px;font-weight:900;line-height:1.5">كلما ارتفع الرقم، <span class="gold">زاد القلق</span> في السوق.</div>
 {f(2, "محتوى تعليمي")}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">أسبوع الخوف</span><span>حتى الجمعة ٢٠ نوفمبر</span></div>
 <h2 style="margin-top:50px">ماذا حدث<br><em>هذا الأسبوع؟</em></h2>
 <div style="position:relative;margin-top:14px">
  {stat("مؤشر VIX", "37+", "من نحو 20 يوم الاثنين.", "gold")}
  {stat("S&amp;P 500 أسبوعياً", "−8.6%", "أسوأ أسبوع منذ أبريل 2025.", "red")}
  {stat("جلسة الجمعة", "−3.7%", "سابع خسارة متتالية للمؤشر.", "red")}
 </div>
 {f(3)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">كيف تقرؤه؟</span><span>قاعدة تقريبية</span></div>
 <h2 style="margin-top:50px">مستويات<br><em>الخوف</em></h2>
 <div style="position:relative;margin-top:16px">
  {stat("هدوء نسبي", "تحت 20", "السوق غير متوتر عادةً.", "green")}
  {stat("قلق", "20–30", "تقلب أعلى وأخبار مقلقة.", "gold")}
  {stat("خوف مرتفع", "فوق 30", "تحركات حادة في الاتجاهين.", "red")}
 </div>
 <p style="font-size:28px;color:#8FA0BC;margin-top:30px">أرقام استرشادية للتعلم، وليست حدوداً ثابتة.</p>
 {f(4, "محتوى تعليمي")}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">ماذا تفعل؟</span><span>وقت الذعر</span></div>
 <h2 style="margin-top:50px">٣ تصرفات<br><em>أذكى</em></h2>
 <div style="position:relative;margin-top:16px">
  {point("١","قلّل حجم الصفقة","التقلب العالي يعني حركات أكبر ضدك.")}
  {point("٢","التزم بخطتك","لا تغيّر قواعدك بسبب عناوين الأخبار.")}
  {point("٣","لا تبع بدافع الذعر","القرار تحت الضغط غالباً الأسوأ.")}
 </div>
 {f(5, "محتوى تعليمي")}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">تنبيه</span><span>لا تفهمه خطأ</span></div>
 <h2 style="margin-top:90px">VIX المرتفع<br><em>ليس إشارة<br>شراء أو بيع</em></h2>
 <div class="card" style="padding:36px 40px;margin-top:40px;font-size:36px;line-height:1.6;color:#B7C3DA">هو مقياس للقلق الحالي فقط، ولا يضمن ارتداداً ولا هبوطاً أعمق.</div>
 {f(6, "محتوى تعليمي")}
</section>""")
def opt(l,t): return f'<div class="card" style="padding:26px 40px;margin-top:20px;display:flex;gap:28px;align-items:center"><div style="min-width:76px;height:76px;border-radius:50%;background:#F4B740;color:#0B1220;font-size:46px;font-weight:900;display:flex;align-items:center;justify-content:center">{l}</div><div style="font-size:42px;font-weight:900">{t}</div></div>'
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">وش رأيك؟</span><span>الأحد ٢٢ نوفمبر</span></div>
 <h1 style="font-size:88px;margin-top:60px">VIX فوق ٣٧…<br><span class="gold">وش تسوي؟</span></h1>
 <div style="margin-top:20px">{opt("أ","أنتظر وأراقب")}{opt("ب","أقلّل حجم صفقاتي")}{opt("ج","أبحث عن فرصة")}</div>
 <p style="font-size:36px;color:#F4B740;margin-top:30px;font-weight:900">اكتب حرفك في التعليقات 👇</p>
 <p style="font-size:23px;color:#8FA0BC;margin-top:18px;line-height:1.6">⚠ المحتوى تعليمي وليس توصية استثمارية. التداول ينطوي على مخاطر وقد تخسر جزءاً من رأس مالك أو كله. الأرقام حتى إغلاق الجمعة ٢٠ نوفمبر.</p>
 {f(7)}
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

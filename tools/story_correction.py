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
def opt(l,t): return f'<div class="card" style="padding:26px 40px;margin-top:20px;display:flex;gap:28px;align-items:center"><div style="min-width:76px;height:76px;border-radius:50%;background:#F4B740;color:#0B1220;font-size:46px;font-weight:900;display:flex;align-items:center;justify-content:center">{l}</div><div style="font-size:42px;font-weight:900">{t}</div></div>'
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">درس التداول</span><span>الأحد 22 نوفمبر 2026</span></div>
 <div style="margin-top:120px;position:relative">
  <div style="font-size:48px;color:#B7C3DA;font-weight:700">S&amp;P 500 دون قمته القياسية بنحو</div>
  <div style="direction:ltr;text-align:right;font-size:230px;font-weight:900;line-height:1.1" class="red">−11.6%</div>
  <h1 style="font-size:88px;margin-top:10px">تصحيح أم <span class="gold">سوق هابطة؟</span></h1>
  <p style="font-size:40px;color:#B7C3DA;margin-top:34px;line-height:1.55;font-weight:400">الفرق بينهما أهم مما تظن.</p>
 </div>
 <div style="position:absolute;left:84px;bottom:130px;font-size:36px;color:#8FA0BC;font-weight:700">اسحب للمزيد ←</div>
 {f(1)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">التعريف الأول</span><span>التصحيح</span></div>
 <h2 style="margin-top:60px">ما هو <em>التصحيح؟</em></h2>
 <div class="card" style="padding:40px;margin-top:40px">
  <div style="font-size:42px;font-weight:900;line-height:1.5">هبوط بنسبة <span class="gold">{L("10%")}</span> فأكثر</div>
  <div style="font-size:34px;color:#B7C3DA;line-height:1.7;margin-top:14px">عن أعلى مستوى قياسي حديث للمؤشر أو السهم.</div>
 </div>
 <div class="card" style="padding:34px 40px;margin-top:26px;font-size:36px;font-weight:900;line-height:1.6">غالباً ما يكون <span class="gold">أقصر عمراً</span> من السوق الهابطة.</div>
 {f(2, "محتوى تعليمي")}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">التعريف الثاني</span><span>السوق الهابطة</span></div>
 <h2 style="margin-top:60px">وما هي <em>السوق الهابطة؟</em></h2>
 <div class="card" style="padding:40px;margin-top:40px">
  <div style="font-size:42px;font-weight:900;line-height:1.5">هبوط بنسبة <span class="red">{L("20%")}</span> فأكثر</div>
  <div style="font-size:34px;color:#B7C3DA;line-height:1.7;margin-top:14px">عن أعلى مستوى قياسي، وتصاحبه عادةً نظرة متشائمة للاقتصاد.</div>
 </div>
 {f(3, "محتوى تعليمي")}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">أين نحن؟</span><span>حتى إغلاق الجمعة 20 نوفمبر</span></div>
 <h2 style="margin-top:50px">موقع السوق<br><em>الآن</em></h2>
 <div style="position:relative;margin-top:14px">
  {stat("دون القمة القياسية", "−11.6%", "القمة بتاريخ 6 أكتوبر.", "red")}
  {stat("إغلاق S&amp;P 500", "6,910.39", f"بانخفاض {L('3.70%')} في جلسة الجمعة.", "gold")}
  {stat("خسائر متتالية", "7", "جلسات متتالية من التراجع.", "red")}
 </div>
 {f(4)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">الخريطة</span><span>مناطق الهبوط</span></div>
 <h2 style="margin-top:50px">أين نقع<br><em>على الخريطة؟</em></h2>
 <div style="position:relative;margin-top:16px">
  {stat("تقلب عادي", "0–10%", "هبوط لا يُصنَّف تصحيحاً.", "green")}
  {stat("تصحيح", "10–20%", "المنطقة الحالية للمؤشر.", "gold")}
  {stat("سوق هابطة", "20%+", "تحتاج هبوطاً إضافياً للوصول إليها.", "red")}
 </div>
 <p style="font-size:28px;color:#8FA0BC;margin-top:30px">التصنيف وصفٌ للأرقام فقط، ولا يتنبأ بما سيحدث لاحقاً.</p>
 {f(5, "محتوى تعليمي")}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">الخلاصة</span><span>3 دروس</span></div>
 <h2 style="margin-top:50px">كيف تتعامل<br><em>مع التصحيح؟</em></h2>
 <div style="position:relative;margin-top:16px">
  {point("1","لا تبنِ قرارك على التسمية","التصحيح أو السوق الهابطة وصفٌ للنسبة وليس إشارة تداول.")}
  {point("2","التزم بخطة مكتوبة","حدّد مسبقاً حجم المخاطرة ونقطة الخروج.")}
  {point("3","احذر القرار العاطفي","الذعر والاندفاع أكثر ما يكلّف المتداول.")}
 </div>
 {f(6, "محتوى تعليمي")}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">ما رأيك؟</span><span>الأحد 22 نوفمبر</span></div>
 <h1 style="font-size:84px;margin-top:60px">تصحيح عابر<br><span class="gold">أم سوق هابطة؟</span></h1>
 <div style="margin-top:20px">{opt("أ","تصحيح عابر")}{opt("ب","بداية سوق هابطة")}{opt("ج","من المبكر الحكم")}</div>
 <p style="font-size:36px;color:#F4B740;margin-top:30px;font-weight:900">اكتب حرفك في التعليقات 👇</p>
 <p style="font-size:23px;color:#8FA0BC;margin-top:18px;line-height:1.6">⚠ المحتوى تعليمي وليس توصية استثمارية. التداول ينطوي على مخاطر وقد تخسر جزءاً من رأس مالك أو كله. الأرقام حتى إغلاق الجمعة 20 نوفمبر.</p>
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

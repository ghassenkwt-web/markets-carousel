# Story-format carousel (one topic, deep dive). Reuses design system from build.py.
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
_src = (HERE / "build.py").read_text(encoding="utf-8").split("slides = []")[0]
exec(_src)  # gives: css, foot, L, TOTAL, ROOT, OUT, sync_playwright

SRC = "حساب رياضي بحت · محتوى تعليمي"

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
def row(loss, gain, cls):
    return f"""<div class="card" style="padding:26px 40px;margin-top:18px;display:flex;justify-content:space-between;align-items:center">
 <div><div class="muted" style="font-size:26px">إذا خسرت</div><div class="red" style="font-size:58px;font-weight:900">{L(loss)}</div></div>
 <div style="font-size:44px;color:#8FA0BC">←</div>
 <div style="text-align:left"><div class="muted" style="font-size:26px">تحتاج ربحاً</div><div class="{cls}" style="font-size:58px;font-weight:900">{L(gain)}</div></div>
</div>"""
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">درس التداول</span><span>رياضيات الخسارة</span></div>
 <div style="margin-top:120px;position:relative">
  <div style="font-size:48px;color:#B7C3DA;font-weight:700">خسارة حسابك بنسبة</div>
  <div style="direction:ltr;text-align:right;font-size:230px;font-weight:900;line-height:1.1" class="red">50%</div>
  <h1 style="font-size:84px;margin-top:10px">تحتاج ربحاً بنسبة <span class="gold">{L("100%")}</span> للعودة!</h1>
  <p style="font-size:40px;color:#B7C3DA;margin-top:34px;line-height:1.55;font-weight:400">لماذا لا تتساوى الخسارة والربح؟</p>
 </div>
 <div style="position:absolute;left:84px;bottom:130px;font-size:36px;color:#8FA0BC;font-weight:700">اسحب للمزيد ←</div>
 {f(1)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">مثال</span><span>حساب بقيمة 1000 دولار</span></div>
 <h2 style="margin-top:60px">لنبدأ <em>بمثال بسيط</em></h2>
 {step("البداية","رصيد الحساب","1,000$","gold")}
 {step(f"بعد خسارة {L('50%')}","الرصيد يصبح","500$","red")}
 {step(f"للعودة إلى {L('1,000$')}","تحتاج أن يتضاعف الرصيد","+100%","green", True)}
 <p style="font-size:30px;color:#B7C3DA;margin-top:20px;line-height:1.6">الربح بنسبة {L("50%")} على {L("500$")} يعطيك {L("750$")} فقط، وليس {L("1,000$")}.</p>
 {f(2)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">الجدول</span><span>كلما زادت الخسارة…</span></div>
 <h2 style="margin-top:40px">كم تحتاج <em>للتعويض؟</em></h2>
 <div style="position:relative;margin-top:10px">
  {row("10%","11.1%","gold")}
  {row("25%","33.3%","gold")}
  {row("50%","100%","red")}
  {row("75%","300%","red")}
 </div>
 {f(3)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">السبب</span><span>القاعدة المتغيرة</span></div>
 <h2 style="margin-top:60px">لماذا يحدث <em>هذا؟</em></h2>
 <div class="card" style="padding:40px;margin-top:40px">
  <div style="font-size:40px;font-weight:900;line-height:1.55">بعد الخسارة تصبح <span class="gold">القاعدة</span> التي تحسب عليها الربح أصغر.</div>
  <div style="font-size:34px;color:#B7C3DA;line-height:1.7;margin-top:14px">نسبة الربح تُحسب على الرصيد الجديد الأقل، لا على الرصيد الأصلي.</div>
 </div>
 <div class="card" style="padding:34px 40px;margin-top:26px;direction:ltr;text-align:center;font-size:44px;font-weight:900">الربح المطلوب = الخسارة ÷ (1 − الخسارة)</div>
 {f(4)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">مفاجأة</span><span>خسارة ثم ربح بالنسبة نفسها</span></div>
 <h2 style="margin-top:50px">خسرت {L("10%")} ثم ربحت {L("10%")}<br><em>هل عدت للبداية؟</em></h2>
 <div style="position:relative;margin-top:16px">
  {stat("الرصيد الأول", "1,000$", "نقطة البداية.", "gold")}
  {stat(f"بعد خسارة {L('10%')}", "900$", f"خسرت {L('100$')}.", "red")}
  {stat(f"بعد ربح {L('10%')}", "990$", "ما زلت دون رصيدك الأول.", "gold")}
 </div>
 {f(5)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">الخلاصة</span><span>3 دروس</span></div>
 <h2 style="margin-top:50px">كيف تحمي<br><em>رأس مالك؟</em></h2>
 <div style="position:relative;margin-top:16px">
  {point("1","حماية رأس المال أولاً","تجنّب الخسارة الكبيرة أسهل من تعويضها.")}
  {point("2","حدّد المخاطرة في كل صفقة","نسبة صغيرة من الحساب تبقيك في اللعبة.")}
  {point("3","استخدم وقف الخسارة","خطة خروج واضحة قبل الدخول وليس بعده.")}
 </div>
 {f(6)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">اختبر نفسك</span><span>سؤال سريع</span></div>
 <h1 style="font-size:76px;margin-top:50px">خسرت {L("50%")} من حسابك.<br><span class="gold">كم تحتاج من الربح للعودة؟</span></h1>
 <div style="margin-top:20px">{opt("أ",L("50%"))}{opt("ب",L("75%"))}{opt("ج",L("100%"))}</div>
 <p style="font-size:36px;color:#F4B740;margin-top:30px;font-weight:900">اكتب حرفك في التعليقات 👇</p>
 <p style="font-size:23px;color:#8FA0BC;margin-top:18px;line-height:1.6">⚠ المحتوى تعليمي وليس توصية استثمارية. التداول ينطوي على مخاطر وقد تخسر جزءاً من رأس مالك أو كله.</p>
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

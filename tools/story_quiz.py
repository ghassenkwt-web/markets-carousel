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
E="اختبار تعليمي"
def q(n,t,b):
    return f"""<div class="card" style="padding:34px 40px;margin-top:26px;display:flex;gap:28px;align-items:flex-start">
  <div style="min-width:84px;height:84px;border-radius:24px;background:rgba(244,183,64,.14);border:2px solid rgba(244,183,64,.45);color:#F4B740;font-size:52px;font-weight:900;display:flex;align-items:center;justify-content:center">{n}</div>
  <div><div style="font-size:42px;font-weight:900;line-height:1.4">{t}</div><div style="font-size:30px;color:#9FB0CB;line-height:1.5;margin-top:8px">{b}</div></div></div>"""
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">اختبار</span><span>الأحد 22 نوفمبر 2026</span></div>
 <div style="margin-top:150px">
  <div style="font-size:48px;color:#B7C3DA;font-weight:700">اختبر نفسك بصدق</div>
  <h1 style="font-size:124px;margin-top:14px">هل أنت <span class="gold">متداول</span><br>أم <span class="red">مقامر؟</span></h1>
  <p style="font-size:40px;color:#B7C3DA;margin-top:44px;line-height:1.6;font-weight:400">6 أسئلة، وأجب بـ«نعم» أو «لا».<br>ثم اكتب نتيجتك في التعليقات.</p>
 </div>
 <div style="position:absolute;left:84px;bottom:130px;font-size:36px;color:#8FA0BC;font-weight:700">ابدأ الاختبار ←</div>
 {f(1, E)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">الأسئلة</span><span>{L("1–2")}</span></div>
 <h2 style="margin-top:60px">أجب بـ <em>نعم أو لا</em></h2>
 <div style="position:relative;margin-top:10px">
  {q("1","هل لديك خطة مكتوبة قبل كل صفقة؟","سعر الدخول والخروج وحجم الصفقة.")}
  {q("2","هل تحدّد وقف الخسارة قبل الدخول؟","وليس بعد أن يتحرك السعر ضدك.")}
 </div>
 {f(2, E)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">الأسئلة</span><span>{L("3–4")}</span></div>
 <h2 style="margin-top:60px">هل <em>تعرف</em><br>ما تخاطر به؟</h2>
 <div style="position:relative;margin-top:10px">
  {q("3","هل تعرف أقصى مبلغ قد تخسره في الصفقة؟","قبل أن تضغط زر الشراء.")}
  {q("4","هل قراراتك من تحليلك أنت؟","لا من نصيحة صديق أو ضجة وسائل التواصل.")}
 </div>
 {f(3, E)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">الأسئلة</span><span>{L("5–6")}</span></div>
 <h2 style="margin-top:60px">السؤالان<br><em>الأخيران</em></h2>
 <div style="position:relative;margin-top:10px">
  {q("5","هل تلتزم بحجمك بعد الخسارة؟","دون زيادته لتعويض ما خسرته بسرعة.")}
  {q("6","هل تسجّل صفقاتك وتراجعها؟","لتتعلم من الأخطاء والنجاحات.")}
 </div>
 <p style="font-size:34px;color:#F4B740;margin-top:40px;font-weight:900">احسب عدد إجاباتك بـ «نعم»</p>
 {f(4, E)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">النتيجة</span><span>عدد «نعم»</span></div>
 <h2 style="margin-top:50px">ماذا تقول<br><em>نتيجتك؟</em></h2>
 <div style="position:relative;margin-top:14px">
  {stat("متداول منضبط", "5–6", "تعمل بخطة وتدير مخاطرك.", "green")}
  {stat("في الطريق", "3–4", "أساس جيد ويحتاج مزيداً من الانضباط.", "gold")}
  {stat("أقرب للمقامرة", "0–2", "راجع قواعدك قبل أي صفقة جديدة.", "red")}
 </div>
 <p style="font-size:26px;color:#8FA0BC;margin-top:26px">اختبار تقريبي للتعلّم والتأمل، وليس تقييماً مالياً.</p>
 {f(5, E)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">التحسين</span><span>خطوات عملية</span></div>
 <h2 style="margin-top:50px">كيف ترفع<br><em>نتيجتك؟</em></h2>
 <div style="position:relative;margin-top:16px">
  {point("1","اكتب خطتك","صفحة واحدة تلخّص قواعد الدخول والخروج.")}
  {point("2","حدّد المخاطرة مسبقاً","نسبة ثابتة صغيرة من رأس المال في كل صفقة.")}
  {point("3","سجّل وراجع","دفتر صفقات تراجعه أسبوعياً.")}
 </div>
 {f(6, E)}
</section>""")
S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">دورك الآن</span><span>الأحد 22 نوفمبر</span></div>
 <h1 style="font-size:96px;margin-top:100px">كم حصلت<br>في <span class="gold">الاختبار؟</span></h1>
 <p style="font-size:44px;color:#EAF0FA;margin-top:50px;line-height:1.6;font-weight:700">اكتب نتيجتك في التعليقات 👇<br>وأرسل الاختبار لصديقك المتداول.</p>
 <div class="card" style="position:absolute;right:84px;left:84px;bottom:170px;padding:30px 40px">
  <div style="font-size:26px;color:#8FA0BC;line-height:1.7">⚠ المحتوى تعليمي وليس توصية استثمارية. الاختبار للتأمل الذاتي فقط. التداول ينطوي على مخاطر وقد تخسر جزءاً من رأس مالك أو كله.</div>
 </div>
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

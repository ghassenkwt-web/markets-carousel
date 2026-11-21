# Story-format carousel (one topic, deep dive). Reuses design system from build.py.
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
_src = (HERE / "build.py").read_text(encoding="utf-8").split("slides = []")[0]
exec(_src)  # gives: css, foot, L, TOTAL, ROOT, OUT, sync_playwright

SRC = "المصادر: " + '<span class="ltr" dir="ltr">CNBC · Semafor · Motley Fool · Fitch</span>'

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
 <div class="top"><span class="pill">قصة الأسبوع</span><span>الأحد ٢٢ نوفمبر ٢٠٢٦</span></div>
 <div style="margin-top:150px;position:relative">
  <div style="font-size:42px;color:#FF5A67;font-weight:900;margin-bottom:26px">● إنفيديا</div>
  <h1 style="font-size:112px">أرباح قياسية<br>وسهم <span class="red">يهوي {L("14%")}</span></h1>
  <p style="font-size:44px;color:#B7C3DA;margin-top:48px;line-height:1.55;font-weight:400">كيف ينهار سهم بعد أفضل نتائجه؟<br>القصة ليست في الأرباح.</p>
 </div>
 <div class="card" style="position:absolute;right:84px;left:84px;bottom:170px;padding:34px 44px;display:flex;justify-content:space-between;align-items:center">
  <div><div class="muted" style="font-size:28px">إيرادات الربع الثالث</div><div style="font-size:84px;font-weight:900" class="gold">{L("$115.8B")}</div></div>
  <div style="font-size:36px;color:#8FA0BC;font-weight:700">اسحب للمزيد ←</div>
 </div>
 {f(1)}
</section>""")

S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">النتائج</span><span>الثلاثاء ١٧ نوفمبر</span></div>
 <h2 style="margin-top:50px">الأرقام كانت<br><em>ممتازة</em></h2>
 <div style="position:relative;margin-top:14px">
  {stat("إيرادات الربع", "$115.8B", f"أعلى من توقعات المحللين بأكثر من {L('$6B')}.", "green")}
  {stat("توقعات الربع القادم", "≈ $130B", "رفعت الشركة توقعاتها للربع المقبل.", "green")}
  {stat("رد فعل السهم", "−14%", "هبط يوم الجمعة ٢٠ نوفمبر رغم ذلك.", "red")}
 </div>
 {f(2)}
</section>""")

S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">الخط الزمني</span><span>أسبوع الصدمات</span></div>
 <h2 style="margin-top:36px">ثم بدأ<br><em>الهبوط</em></h2>
 <div style="position:relative;margin-top:22px">
  {step("قبل أسبوع", "استقالة الرئيس التنفيذي جنسن هوانغ", "", "gold")}
  {step("الثلاثاء ١٧ نوفمبر", "نتائج أفضل من التوقعات", "", "green")}
  {step("الأربعاء ١٨ نوفمبر", "السهم يتراجع رغم النتائج", "−2.9%", "red")}
  {step("الخميس ١٩ نوفمبر", "استمرار البيع", "−3.3%", "red")}
  {step("الجمعة ٢٠ نوفمبر", "أسوأ جلسات السلسلة", "−14%", "red", True)}
 </div>
 {f(3)}
</section>""")

S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">السبب الأول</span><span>من يدفع الفاتورة؟</span></div>
 <h2 style="margin-top:50px">المشكلة<br><em>ليست في المبيعات</em></h2>
 <p class="note" style="margin-top:22px;font-size:34px;color:#B7C3DA">السوق لا يشكّ في الطلب، بل في قدرة العملاء على الدفع.</p>
 <div style="position:relative;margin-top:6px">
  {stat("إنفاق 4 عمالقة تقنية", "$740B+", "إنفاق رأسمالي معلن هذا العام على مراكز البيانات والرقائق.", "gold")}
  {stat("ديون مرتبطة بالذكاء الاصطناعي", "≈ $466B", f"إصدارات هذا العام حسب تقديرات {L('Morgan Stanley')}.", "red")}
  {stat("إنفاق 2027 المتوقع", "$1T+", f"قد يتجاوز إنفاق الخمسة الكبار تريليون دولار العام القادم حسب {L('Fitch')}.", "gold")}
 </div>
 {f(4)}
</section>""")

S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">السبب الثاني</span><span>الثقة والقيادة</span></div>
 <h2 style="margin-top:50px">وعامل<br><em>عدم اليقين</em></h2>
 <div style="position:relative;margin-top:16px">
  {point("١","رحيل الرئيس التنفيذي","استقال جنسن هوانغ قبل أسبوع من النتائج، وأكد رئيس المجلس أنه لن يعود.")}
  {point("٢","تقارير عن تحقيق محاسبي",f"تحدثت تقارير يوم الجمعة عن تحقيق من هيئة {L('SEC')}، وما زالت التفاصيل غير مؤكدة.")}
  {point("٣","ضغط على القطاع كله","الهبوط جرّ معه شركات الحوسبة السحابية الناشئة وقطاع الرقائق.")}
 </div>
 {f(5)}
</section>""")

S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">درس التداول</span><span>مفهوم اليوم</span></div>
 <h2 style="margin-top:50px">لماذا لا تكفي<br><em>الأرباح الجيدة؟</em></h2>
 <div class="card" style="padding:34px 40px;margin-top:30px;position:relative">
  <div style="font-size:35px;line-height:1.6">السعر يتحرك بالفرق بين <b class="gold">النتائج والتوقعات</b>، لا بالنتائج وحدها.<br><span class="muted" style="font-size:30px">وإذا كانت التوقعات عالية، قد لا يكفي الجيد.</span></div>
 </div>
 <div style="position:relative">
  {rule("١","اسأل: ما المتوقع؟","قارن النتيجة بتوقعات السوق قبل أن تحكم عليها.")}
  {rule("٢","انظر لمن يموّل النمو","قوة الشركة تعتمد على قدرة عملائها على الدفع.")}
  {rule("٣","لا تحكم من جلسة واحدة","تحرّك يوم واحد لا يغيّر القصة كلها.")}
 </div>
 {f(6, "محتوى تعليمي")}
</section>""")

S.append(f"""
<section class="slide">
 <div class="top"><span class="pill">وش رأيك؟</span><span>الأحد ٢٢ نوفمبر</span></div>
 <h1 style="font-size:100px;margin-top:150px">هبوط إنفيديا:<br><span class="gold">تحذير أم فرصة؟</span></h1>
 <p style="font-size:44px;color:#B7C3DA;margin-top:48px;line-height:1.6;font-weight:400">اكتب رأيك في التعليقات،<br>وتابعنا لقصة جديدة كل صباح.</p>
 <div class="card" style="position:absolute;right:84px;left:84px;bottom:170px;padding:30px 40px">
  <div style="font-size:28px;color:#8FA0BC;line-height:1.7">⚠ المحتوى تعليمي ولا يُعد توصية استثمارية، ولا نوصي بشراء أو بيع أي سهم. التداول ينطوي على مخاطر وقد تخسر جزءاً من رأس مالك أو كله. الأرقام حتى إغلاق الجمعة ٢٠ نوفمبر.</div>
 </div>
 {f(7, "قصة اليوم")}
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

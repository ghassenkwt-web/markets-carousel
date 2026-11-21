import sys, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "out"; OUT.mkdir(exist_ok=True)
TOTAL = 7

def L(t):  # force LTR run for numbers / latin
    return f'<span class="ltr" dir="ltr">{t}</span>'

css = """
@font-face{font-family:Cairo;font-weight:400;src:url(fonts/cairo-arabic-400-normal.woff2);unicode-range:U+0600-06FF,U+0750-077F,U+FB50-FDFF,U+FE70-FEFF}
@font-face{font-family:Cairo;font-weight:700;src:url(fonts/cairo-arabic-700-normal.woff2);unicode-range:U+0600-06FF,U+0750-077F,U+FB50-FDFF,U+FE70-FEFF}
@font-face{font-family:Cairo;font-weight:900;src:url(fonts/cairo-arabic-900-normal.woff2);unicode-range:U+0600-06FF,U+0750-077F,U+FB50-FDFF,U+FE70-FEFF}
@font-face{font-family:Cairo;font-weight:400;src:url(fonts/cairo-latin-400-normal.woff2);unicode-range:U+0000-00FF,U+2000-206F,U+20AC,U+2212}
@font-face{font-family:Cairo;font-weight:700;src:url(fonts/cairo-latin-700-normal.woff2);unicode-range:U+0000-00FF,U+2000-206F,U+20AC,U+2212}
@font-face{font-family:Cairo;font-weight:900;src:url(fonts/cairo-latin-900-normal.woff2);unicode-range:U+0000-00FF,U+2000-206F,U+20AC,U+2212}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#000;font-family:Cairo,sans-serif;direction:rtl}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;color:#EAF0FA;
  background:radial-gradient(1200px 800px at 85% -10%,#1A2C52 0%,#0B1220 55%,#080D18 100%);padding:90px 84px 110px}
.slide::before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px);background-size:100% 54px;pointer-events:none}
.ltr{direction:ltr;unicode-bidi:isolate;display:inline-block}
.top{display:flex;justify-content:space-between;align-items:center;font-size:30px;color:#8FA0BC;font-weight:700;position:relative}
.top .pill{background:rgba(244,183,64,.12);color:#F4B740;border:2px solid rgba(244,183,64,.35);padding:6px 24px;border-radius:40px;font-size:28px}
h1{font-weight:900;line-height:1.25;position:relative}
h2{font-weight:900;font-size:74px;line-height:1.2;margin-top:64px;position:relative}
h2 em{font-style:normal;color:#F4B740}
.muted{color:#8FA0BC}
.red{color:#FF5A67}.green{color:#2ED3A0}.gold{color:#F4B740}
.foot{position:absolute;bottom:52px;left:84px;right:84px;display:flex;justify-content:space-between;align-items:center;font-size:27px;color:#6D7E9C;font-weight:700}
.dots{display:flex;gap:10px;direction:ltr}
.dots i{width:14px;height:14px;border-radius:50%;background:#26324D;display:block}
.dots i.on{background:#F4B740;width:38px;border-radius:8px}
.card{background:linear-gradient(180deg,#141E34,#101830);border:2px solid #1F2C4A;border-radius:30px;position:relative}
.note{font-size:30px;color:#8FA0BC;line-height:1.6;position:relative}
"""

def foot(n, src="المصادر: " + '<span class="ltr" dir="ltr">Reuters · CNBC · CoinDesk · Trading Economics</span>'):
    dots = "".join(f'<i class="{"on" if i+1==n else ""}"></i>' for i in range(TOTAL))
    return f'<div class="foot"><span>{src}</span><div class="dots">{dots}</div></div>'

slides = []

# 1 cover
slides.append(f"""
<section class="slide">
 <div class="top"><span class="pill">ملخص الأسواق اليومي</span><span>الأحد ٢٢ نوفمبر ٢٠٢٦</span></div>
 <div style="margin-top:170px;position:relative">
  <div style="font-size:42px;color:#FF5A67;font-weight:900;margin-bottom:26px">● أسبوع أحمر</div>
  <h1 style="font-size:118px">أسوأ أسبوع<br>لوول ستريت<br><span class="gold">منذ أبريل ٢٠٢٥</span></h1>
  <p style="font-size:44px;color:#B7C3DA;margin-top:48px;line-height:1.55;font-weight:400">S&amp;P 500 يدخل مرحلة التصحيح،<br>والذهب والبيتكوين ينزفون معه</p>
 </div>
 <div class="card" style="position:absolute;right:84px;left:84px;bottom:170px;padding:34px 44px;display:flex;justify-content:space-between;align-items:center">
  <div><div class="muted" style="font-size:28px">S&amp;P 500 خلال الأسبوع</div><div style="font-size:84px;font-weight:900" class="red">{L("−8.6%")}</div></div>
  <div style="font-size:36px;color:#8FA0BC;font-weight:700">اسحب للمزيد ←</div>
 </div>
 {foot(1)}
</section>""")

# 2 indices
def row(name, close, day, week):
    return f"""
<div class="card" style="padding:18px 40px;display:grid;grid-template-columns:1.25fr 1fr 1fr;align-items:center;gap:16px;margin-top:16px">
  <div><div style="font-size:42px;font-weight:900">{name}</div><div class="muted" style="font-size:30px">{L(close)}</div></div>
  <div style="text-align:center"><div class="muted" style="font-size:24px">يوم الجمعة</div><div class="red" style="font-size:50px;font-weight:900">{L(day)}</div></div>
  <div style="text-align:center"><div class="muted" style="font-size:24px">الأسبوع</div><div class="red" style="font-size:50px;font-weight:900">{L(week)}</div></div>
</div>"""
slides.append(f"""
<section class="slide">
 <div class="top"><span class="pill">الأسهم الأمريكية</span><span>إغلاق الجمعة ٢٠ نوفمبر</span></div>
 <h2 style="margin-top:44px">كل المؤشرات<br><em>في المنطقة الحمراء</em></h2>
 <div style="margin-top:20px;position:relative">
  {row("ناسداك","22,618","−5.28%","−10.0%")}
  {row("S&amp;P 500","6,910","−3.70%","−8.6%")}
  {row("داو جونز","48,147","−1.93%","−8.0%")}
  {row("راسل 2000","2,582","−2.76%","−7.5%")}
 </div>
 <p class="note" style="margin-top:28px">الـ S&amp;P 500 خسر <b class="gold">٧ جلسات متتالية</b>، ومؤشر الخوف {L("VIX")} قفز {L("26%")} إلى {L("35.9")}.</p>
 {foot(2)}
</section>""")

# 3 why
def reason(n, title, body):
    return f"""
<div class="card" style="padding:34px 40px;margin-top:24px;display:flex;gap:34px;align-items:flex-start">
  <div style="min-width:84px;height:84px;border-radius:24px;background:rgba(244,183,64,.14);border:2px solid rgba(244,183,64,.4);color:#F4B740;font-size:52px;font-weight:900;display:flex;align-items:center;justify-content:center">{n}</div>
  <div><div style="font-size:44px;font-weight:900;line-height:1.3">{title}</div><div style="font-size:31px;color:#9FB0CB;line-height:1.55;margin-top:10px">{body}</div></div>
</div>"""
slides.append(f"""
<section class="slide">
 <div class="top"><span class="pill">ليش نزل السوق؟</span><span>٣ أسباب رئيسية</span></div>
 <h2 style="margin-top:50px">وراء الهبوط<br><em>ثلاث ضغوط</em></h2>
 <div style="position:relative;margin-top:16px">
  {reason("١","بيع عنيف في أسهم الذكاء الاصطناعي",f"إنفيديا خسرت نحو {L('14%')} يوم الجمعة، وقطاع الرقائق هبط أكثر من {L('10%')}، وناسداك صار سالباً منذ بداية 2026.")}
  {reason("٢","مخاوف من رفع الفائدة",f"بيانات تضخم قوية هذا الشهر، والأسواق تسعّر احتمال رفع في ديسمبر، وعائد السندات لـ 10 سنوات قرابة {L('5%')}.")}
  {reason("٣","دولار قوي",f"مؤشر الدولار قرب {L('103.9')}، أعلى مستوى هذا العام، وهذا يضغط على الأصول الأخرى.")}
 </div>
 {foot(3)}
</section>""")

# 4 gold/oil/dollar
def tile(label, val, sub, cls):
    return f"""
<div class="card" style="padding:24px 40px;margin-top:18px">
  <div style="display:flex;justify-content:space-between;align-items:baseline"><div style="font-size:40px;font-weight:900">{label}</div><div class="{cls}" style="font-size:66px;font-weight:900">{L(val)}</div></div>
  <div style="font-size:30px;color:#9FB0CB;line-height:1.55;margin-top:8px">{sub}</div>
</div>"""
slides.append(f"""
<section class="slide">
 <div class="top"><span class="pill">الذهب · النفط · الدولار</span><span>إغلاق الجمعة</span></div>
 <h2 style="margin-top:40px">حتى الملاذ الآمن<br><em>لم يسلم</em></h2>
 <div style="position:relative;margin-top:16px">
  {tile("الذهب","$3,533",f"هبط نحو {L('4%')} في يوم، وأقل إغلاق منذ 12 شهراً، و9 جلسات هبوط متتالية. أقل بنحو {L('35%')} من قمة يناير.","red")}
  {tile("نفط برنت","$92.7",f"انخفض قرابة {L('15%')} خلال شهر، لكن اضطراب الشحن في مضيق هرمز يبقيه مرتفعاً.","gold")}
  {tile("مؤشر الدولار","103.9","أعلى مستوى هذا العام، ويضغط على الذهب والعملات الرقمية.","green")}
 </div>
 {foot(4)}
</section>""")

# 5 crypto
def coin(name, price, sub, cls="red"):
    return f"""
<div class="card" style="padding:36px 44px;margin-top:24px">
  <div style="display:flex;justify-content:space-between;align-items:baseline"><div style="font-size:46px;font-weight:900">{name}</div><div class="gold" style="font-size:70px;font-weight:900">{L(price)}</div></div>
  <div style="font-size:31px;color:#9FB0CB;line-height:1.55;margin-top:10px">{sub}</div>
</div>"""
slides.append(f"""
<section class="slide">
 <div class="top"><span class="pill">العملات الرقمية</span><span>السبت ٢١ نوفمبر</span></div>
 <h2 style="margin-top:50px">البيتكوين:<br><em>ثاني أسوأ نوفمبر</em></h2>
 <div style="position:relative;margin-top:16px">
  {coin("بيتكوين","≈ $60,000",f"نزل تحت {L('$57,000')} (الأدنى منذ سبتمبر 2024) ثم ارتد فوق {L('$60,000')}. خسارة نوفمبر نحو {L('25%')}.")}
  {coin("إيثريوم","≈ $1,700",f"خسارة نوفمبر نحو {L('27%')}، وثاني أسوأ نوفمبر في تاريخه.")}
 </div>
 <p class="note" style="margin-top:40px">القيمة السوقية للعملات الرقمية قرابة {L("$2")} تريليون، والتذبذب لا يزال عالياً.</p>
 {foot(5)}
</section>""")

# 6 lesson
def rule(n, t, b):
    return f"""
<div style="display:flex;gap:28px;align-items:flex-start;margin-top:44px">
  <div style="min-width:72px;height:72px;border-radius:50%;background:#F4B740;color:#0B1220;font-size:44px;font-weight:900;display:flex;align-items:center;justify-content:center">{n}</div>
  <div><div style="font-size:40px;font-weight:900">{t}</div><div style="font-size:30px;color:#9FB0CB;line-height:1.5;margin-top:4px">{b}</div></div>
</div>"""
slides.append(f"""
<section class="slide">
 <div class="top"><span class="pill">درس التداول</span><span>مفهوم اليوم</span></div>
 <h2 style="margin-top:50px">ما هو<br><em>التصحيح؟</em><div style="font-size:46px;color:#8FA0BC;font-weight:700;margin-top:6px">{L("Correction")}</div></h2>
 <div class="card" style="padding:34px 40px;margin-top:34px;position:relative">
  <div style="font-size:35px;line-height:1.6">هبوط المؤشر <b class="gold">{L("10%")} أو أكثر</b> من أعلى قمة وصل لها.<br><span class="muted" style="font-size:30px">وإذا تعمّق الهبوط إلى {L("20%")} يسمّى سوقاً هابطة.</span></div>
 </div>
 <div style="position:relative">
  {rule("١","لا تلحق السكين الساقط","انتظر حتى يستقر السعر قبل الدخول.")}
  {rule("٢","صغّر حجم الصفقة",f"عندما يتجاوز مؤشر {L('VIX')} الـ {L('30')} قلّل المخاطرة.")}
  {rule("٣","حدّد وقف الخسارة قبل الدخول","اعرف أقصى خسارة تتحملها مسبقاً.")}
 </div>
 {foot(6, "محتوى تعليمي")}
</section>""")

# 7 CTA
slides.append(f"""
<section class="slide">
 <div class="top"><span class="pill">وش رأيك؟</span><span>الأحد ٢٢ نوفمبر</span></div>
 <h1 style="font-size:104px;margin-top:150px">ارتداد قريب<br>ولا <span class="gold">هبوط أعمق؟</span></h1>
 <p style="font-size:44px;color:#B7C3DA;margin-top:48px;line-height:1.6;font-weight:400">اكتب توقعك في التعليقات،<br>وتابعنا لملخص الأسواق كل صباح.</p>
 <div class="card" style="position:absolute;right:84px;left:84px;bottom:170px;padding:30px 40px">
  <div style="font-size:28px;color:#8FA0BC;line-height:1.7">⚠ المحتوى تعليمي ولا يُعد توصية استثمارية. التداول ينطوي على مخاطر وقد تخسر جزءاً من رأس مالك أو كله. الأرقام حتى إغلاق الجمعة ٢٠ نوفمبر وأسعار العملات الرقمية يوم السبت.</div>
 </div>
 {foot(7, "ملخص الأسواق اليومي")}
</section>""")

html = f"<!doctype html><html lang='ar' dir='rtl'><head><meta charset='utf-8'><style>{css}</style></head><body>{''.join(slides)}</body></html>"
(ROOT / "carousel.html").write_text(html, encoding="utf-8")

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto(f"file://{ROOT}/carousel.html")
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(500)
    for i, el in enumerate(pg.query_selector_all(".slide"), 1):
        el.screenshot(path=str(OUT / f"slide-{i}.png"))
    b.close()
print("done")

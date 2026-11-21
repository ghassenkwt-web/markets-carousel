
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE/"out"; OUT.mkdir(exist_ok=True)
FONTS = """@font-face{font-family:Cairo;font-weight:400;src:url(fonts/cairo-arabic-400-normal.woff2);unicode-range:U+0600-06FF,U+0750-077F,U+FB50-FDFF,U+FE70-FEFF}
@font-face{font-family:Cairo;font-weight:700;src:url(fonts/cairo-arabic-700-normal.woff2);unicode-range:U+0600-06FF,U+0750-077F,U+FB50-FDFF,U+FE70-FEFF}
@font-face{font-family:Cairo;font-weight:900;src:url(fonts/cairo-arabic-900-normal.woff2);unicode-range:U+0600-06FF,U+0750-077F,U+FB50-FDFF,U+FE70-FEFF}
@font-face{font-family:Cairo;font-weight:400;src:url(fonts/cairo-latin-400-normal.woff2);unicode-range:U+0000-00FF,U+2000-206F,U+20AC,U+2212}
@font-face{font-family:Cairo;font-weight:700;src:url(fonts/cairo-latin-700-normal.woff2);unicode-range:U+0000-00FF,U+2000-206F,U+20AC,U+2212}
@font-face{font-family:Cairo;font-weight:900;src:url(fonts/cairo-latin-900-normal.woff2);unicode-range:U+0000-00FF,U+2000-206F,U+20AC,U+2212}
"""
Y="#FFE600"; K="#0A0A0A"
css = FONTS + f"""
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#222;font-family:Cairo,sans-serif;direction:rtl}}
.slide{{width:1080px;height:1350px;position:relative;overflow:hidden;padding:84px;display:block}}
.dark{{background:{K};color:#fff}}
.lite{{background:{Y};color:{K}}}
.top{{display:flex;justify-content:space-between;align-items:center;font-size:30px;font-weight:700}}
.pill{{padding:10px 30px;border-radius:50px;font-size:30px;font-weight:900}}
.dark .pill{{background:{Y};color:{K}}} .lite .pill{{background:{K};color:{Y}}}
h1{{font-weight:900;line-height:1.18}}
.dark .hl{{color:{Y}}} .lite .hl{{background:{K};color:{Y};padding:0 18px;border-radius:14px;display:inline-block;line-height:1.3;margin-top:10px}}
.ft{{position:absolute;left:84px;right:84px;bottom:56px;display:flex;justify-content:space-between;align-items:center;font-size:26px;font-weight:700;opacity:.8}}
.dots{{display:flex;gap:10px;direction:ltr}} .dots i{{width:14px;height:14px;border-radius:50%;background:currentColor;opacity:.3}} .dots i.on{{width:40px;border-radius:8px;opacity:1}}
.box{{border-radius:34px;padding:26px 40px;margin-top:22px}}
.dark .box{{background:#161616;border:3px solid #2a2a2a}} .lite .box{{background:{K};color:#fff}}
.num{{min-width:84px;height:84px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:52px;font-weight:900}}
.dark .num{{background:{Y};color:{K}}} .lite .num{{background:{K};color:{Y}}}
"""
def foot(n, t):
    d="".join(f'<i class="{"on" if i==n else ""}"></i>' for i in range(1,8))
    return f'<div class="ft"><span>{t}</span><div class="dots">{d}</div></div>'
def top(tag, d="الأحد ٢٢ نوفمبر"): return f'<div class="top"><span class="pill">{tag}</span><span>{d}</span></div>'
def item(n,t,b,cls=""):
    return f'<div class="box" style="display:flex;gap:30px;align-items:center"><div class="num" style="direction:ltr;{cls}">{n}</div><div><div style="font-size:44px;font-weight:900;line-height:1.3">{t}</div><div style="font-size:31px;opacity:.75;line-height:1.5;margin-top:6px">{b}</div></div></div>'

S=[]
SRCT="المصادر: "+'<span dir="ltr" style="direction:ltr;display:inline-block">Schwab · CNBC · NPR</span>'
def stat(label,val,sub,color=""):
    return f'<div class="box" style="display:flex;justify-content:space-between;align-items:center"><div><div style="font-size:40px;font-weight:900">{label}</div><div style="font-size:28px;opacity:.7;margin-top:4px">{sub}</div></div><div style="font-size:78px;font-weight:900;direction:ltr;{color}">{val}</div></div>'
S.append(f"""<section class="slide dark">{top("مؤشر الخوف")}
<div style="font-size:56px;font-weight:900;margin-top:110px;opacity:.9">قفز في أسبوع واحد من</div>
<div style="direction:ltr;text-align:right;font-size:230px;font-weight:900;line-height:1.05;margin-top:10px"><span style="opacity:.55">20</span> <span style="color:{Y}">→ 37+</span></div>
<h1 style="font-size:96px;margin-top:20px"><span class="hl">VIX</span> يدق الجرس</h1>
<p style="font-size:38px;margin-top:34px;opacity:.8;line-height:1.5">ماذا يعني هذا الرقم؟ ولماذا يهمك؟</p>
<div style="position:absolute;left:84px;bottom:130px;font-size:38px;font-weight:900;color:{Y}">اسحب ←</div>
{foot(1,SRCT)}</section>""")
S.append(f"""<section class="slide lite">{top("المفهوم")}
<h1 style="font-size:100px;margin-top:100px">ما هو <span class="hl">VIX</span>؟</h1>
<p style="font-size:48px;font-weight:700;line-height:1.6;margin-top:50px">يُعرف بـ«مؤشر الخوف».</p>
<p style="font-size:42px;line-height:1.7;margin-top:24px;font-weight:400">يقيس مدى التقلب الذي يتوقعه المستثمرون في مؤشر S&amp;P 500 خلال الـ٣٠ يوماً القادمة.</p>
<div class="box" style="margin-top:56px;font-size:40px;font-weight:900;line-height:1.5">كلما ارتفع، زاد القلق في السوق.</div>
{foot(2,"محتوى تعليمي")}</section>""")
S.append(f"""<section class="slide dark">{top("أسبوع الخوف")}
<h1 style="font-size:88px;margin-top:50px">ماذا حدث<br><span class="hl">هذا الأسبوع؟</span></h1>
{stat("مؤشر VIX","37+","من نحو 20 يوم الاثنين",f"color:{Y}")}
{stat("S&amp;P 500 أسبوعياً","−8.6%","أسوأ أسبوع منذ أبريل 2025","color:#FF5A67")}
{stat("جلسة الجمعة","−3.7%","سابع خسارة متتالية للمؤشر","color:#FF5A67")}
{foot(3,SRCT)}</section>""")
S.append(f"""<section class="slide lite">{top("كيف تقرؤه؟")}
<h1 style="font-size:92px;margin-top:60px">قاعدة <span class="hl">تقريبية</span></h1>
{item("تحت 20","هدوء نسبي","السوق غير متوتر عادةً.")}
{item("20–30","قلق","تقلب أعلى وأخبار مقلقة.")}
{item("فوق 30","خوف مرتفع","تحركات حادة في الاتجاهين.")}
<p style="font-size:28px;margin-top:26px;opacity:.75">أرقام استرشادية للتعلم، وليست حدوداً ثابتة.</p>
{foot(4,"محتوى تعليمي")}</section>""".replace('class="num" style=""','class="num" style="min-width:190px;padding:0 20px;white-space:nowrap;border-radius:40px;font-size:38px"'))
S.append(f"""<section class="slide dark">{top("ماذا تفعل؟")}
<h1 style="font-size:88px;margin-top:60px">٣ تصرفات <span class="hl">أذكى</span><br>وقت الذعر</h1>
{item("١","قلّل حجم الصفقة","التقلب العالي يعني حركات أكبر ضدك.")}
{item("٢","التزم بخطتك","لا تغيّر قواعدك بسبب الأخبار.")}
{item("٣","لا تبع بدافع الذعر","القرار تحت الضغط غالباً الأسوأ.")}
{foot(5,"محتوى تعليمي")}</section>""")
S.append(f"""<section class="slide lite">{top("تنبيه")}
<div style="margin-top:140px;font-size:54px;font-weight:700">VIX المرتفع</div>
<h1 style="font-size:120px;margin-top:20px"><span class="hl">ليس إشارة</span></h1>
<h1 style="font-size:100px;margin-top:30px;line-height:1.3">شراء أو بيع.</h1>
<p style="font-size:40px;margin-top:50px;line-height:1.6;font-weight:400">هو مقياس للقلق الحالي فقط، ولا يضمن ارتداداً ولا هبوطاً أعمق.</p>
{foot(6,"محتوى تعليمي")}</section>""")
S.append(f"""<section class="slide dark">{top("تفاعل معنا")}
<h1 style="font-size:90px;margin-top:50px">VIX فوق ٣٧…<br><span class="hl">وش تسوي؟</span></h1>
<div class="box" style="display:flex;gap:30px;align-items:center;margin-top:36px"><div class="num">أ</div><div style="font-size:44px;font-weight:900">أنتظر وأراقب</div></div>
<div class="box" style="display:flex;gap:30px;align-items:center"><div class="num">ب</div><div style="font-size:44px;font-weight:900">أقلّل حجم صفقاتي</div></div>
<div class="box" style="display:flex;gap:30px;align-items:center"><div class="num">ج</div><div style="font-size:44px;font-weight:900">أبحث عن فرصة</div></div>
<p style="font-size:36px;margin-top:28px;color:{Y};font-weight:900">اكتب حرفك في التعليقات 👇</p>
<p style="font-size:23px;opacity:.6;margin-top:16px;line-height:1.5">⚠ المحتوى تعليمي وليس توصية استثمارية. التداول ينطوي على مخاطر وقد تخسر جزءاً من رأس مالك أو كله. الأرقام حتى إغلاق الجمعة ٢٠ نوفمبر.</p>
{foot(7,SRCT)}</section>""")
html=f"<!doctype html><html lang='ar' dir='rtl'><head><meta charset='utf-8'><style>{css}</style></head><body>{''.join(S)}</body></html>"
(HERE/"story.html").write_text(html,encoding="utf-8")
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1350})
    pg.goto(f"file://{HERE}/story.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(500)
    for i,el in enumerate(pg.query_selector_all(".slide"),1): el.screenshot(path=str(OUT/f"slide-{i}.png"))
    b.close()
print("done")

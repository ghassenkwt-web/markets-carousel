
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
    return f'<div class="box" style="display:flex;gap:30px;align-items:center"><div class="num" style="{cls}">{n}</div><div><div style="font-size:44px;font-weight:900;line-height:1.3">{t}</div><div style="font-size:31px;opacity:.75;line-height:1.5;margin-top:6px">{b}</div></div></div>'
S=[]
S.append(f"""<section class="slide dark">{top("درس التداول")}
<div style="margin-top:120px"><div style="font-size:60px;font-weight:900;color:#fff;opacity:.9">لماذا تشتري دائماً</div>
<h1 style="font-size:150px;margin-top:6px"><span class="hl">في القمة؟</span></h1>
<div style="font-family:Cairo;font-size:250px;font-weight:900;color:{Y};line-height:1;margin-top:50px;direction:ltr;text-align:right;letter-spacing:-6px">FOMO</div>
<p style="font-size:42px;margin-top:30px;opacity:.8">الفخ الذي يقع فيه الجميع.</p></div>
<div style="position:absolute;left:84px;bottom:130px;font-size:38px;font-weight:900;color:{Y}">اسحب ←</div>
{foot(1,"قصة اليوم")}</section>""")
S.append(f"""<section class="slide lite">{top("المفهوم")}
<h1 style="font-size:104px;margin-top:100px">ما هو <span class="hl">FOMO</span>؟</h1>
<p style="font-size:50px;font-weight:700;line-height:1.6;margin-top:50px">الخوف من تفويت الفرصة.</p>
<p style="font-size:42px;line-height:1.7;margin-top:30px;font-weight:400">ترى السعر يرتفع والجميع يتحدث عن أرباحه، فتشعر أن القطار سيغادر بدونك… فتشتري بدافع الخوف لا بدافع الخطة.</p>
<div class="box" style="margin-top:60px;font-size:40px;font-weight:900;line-height:1.5">القرار العاطفي أغلى من أي عمولة.</div>
{foot(2,"محتوى تعليمي")}</section>""")
S.append(f"""<section class="slide dark">{top("كيف يعمل الفخ")}
<h1 style="font-size:84px;margin-top:40px">٤ خطوات<br><span class="hl">نحو الخسارة</span></h1>
{item("١","السعر يرتفع بقوة","يلفت الانتباه ويبدأ الحديث عنه.")}
{item("٢","الجميع يتحدث عنه","تتزايد الإثارة، وتشعر أنك متأخر.")}
{item("٣","تشتري بعد الصعود","تدخل عند سعر مرتفع بلا خطة.")}
{item("٤","السعر يتراجع","تبيع بخسارة أو تعلق بالصفقة.")}
{foot(3,"محتوى تعليمي")}</section>""")
S.append(f"""<section class="slide lite">{top("قاعدة تذكّرها")}
<div style="margin-top:130px;font-size:56px;font-weight:700">حين يصبح الجميع يتحدث عن سهم أو عملة…</div>
<h1 style="font-size:120px;margin-top:40px"><span class="hl">اسأل نفسك:</span></h1>
<h1 style="font-size:96px;margin-top:30px;line-height:1.3">كم تحرّك السعر<br>قبل أن أنتبه؟</h1>
<p style="font-size:38px;margin-top:50px;line-height:1.6;font-weight:400">الانتشار الكبير قد يعني أن جزءاً كبيراً من الحركة حدث بالفعل.</p>
{foot(4,"محتوى تعليمي")}</section>""")
S.append(f"""<section class="slide dark">{top("علامات الخطر")}
<h1 style="font-size:92px;margin-top:70px">٣ علامات أنك<br><span class="hl">وقعت في الفخ</span></h1>
{item("١","تشتري بدون خطة","لا تعرف سعر الدخول ولا الخروج.")}
{item("٢","تلاحق الشمعة الخضراء","تدخل فقط لأن السعر يطير.")}
{item("٣","تزيد حجم الصفقة","لتعوّض ما فاتك بسرعة.")}
{foot(5,"محتوى تعليمي")}</section>""")
S.append(f"""<section class="slide lite">{top("الحل")}
<h1 style="font-size:92px;margin-top:60px;margin-bottom:10px">٣ قواعد<br><span class="hl">تحميك</span></h1>
{item("١","خطة قبل الدخول","حدد سعر الدخول ووقف الخسارة قبل أي شراء.")}
{item("٢","حجم صغير ومحسوب","لا تخاطر بأكثر مما تتحمل خسارته.")}
{item("٣","انتظر الفرصة التالية","السوق لا ينتهي، والفرص تتكرر.")}
{foot(6,"محتوى تعليمي")}</section>""")
S.append(f"""<section class="slide dark">{top("تفاعل معنا")}
<h1 style="font-size:92px;margin-top:50px">آخر مرة اشتريت<br>لأن <span class="hl">الكل يشتري؟</span></h1>
<div class="box" style="display:flex;gap:30px;align-items:center;margin-top:36px"><div class="num">أ</div><div style="font-size:46px;font-weight:900">نعم، وندمت</div></div>
<div class="box" style="display:flex;gap:30px;align-items:center"><div class="num">ب</div><div style="font-size:46px;font-weight:900">نعم، وربحت</div></div>
<div class="box" style="display:flex;gap:30px;align-items:center"><div class="num">ج</div><div style="font-size:46px;font-weight:900">لا، ألتزم بخطتي</div></div>
<p style="font-size:36px;margin-top:28px;color:{Y};font-weight:900">اكتب حرفك في التعليقات 👇</p>
<p style="font-size:23px;opacity:.6;margin-top:16px;line-height:1.5">⚠ المحتوى تعليمي وليس توصية استثمارية. التداول ينطوي على مخاطر وقد تخسر جزءاً من رأس مالك أو كله.</p>
{foot(7,"قصة اليوم")}</section>""")
html=f"<!doctype html><html lang='ar' dir='rtl'><head><meta charset='utf-8'><style>{css}</style></head><body>{''.join(S)}</body></html>"
(HERE/"story.html").write_text(html,encoding="utf-8")
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1350})
    pg.goto(f"file://{HERE}/story.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(500)
    for i,el in enumerate(pg.query_selector_all(".slide"),1): el.screenshot(path=str(OUT/f"slide-{i}.png"))
    b.close()
print("done")


import pathlib
HERE=pathlib.Path(__file__).resolve().parent
OUT=HERE/"out"; OUT.mkdir(exist_ok=True)
FONTS="""@font-face{font-family:Cairo;font-weight:400;src:url(fonts/cairo-arabic-400-normal.woff2);unicode-range:U+0600-06FF,U+0750-077F,U+FB50-FDFF,U+FE70-FEFF}
@font-face{font-family:Cairo;font-weight:700;src:url(fonts/cairo-arabic-700-normal.woff2);unicode-range:U+0600-06FF,U+0750-077F,U+FB50-FDFF,U+FE70-FEFF}
@font-face{font-family:Cairo;font-weight:900;src:url(fonts/cairo-arabic-900-normal.woff2);unicode-range:U+0600-06FF,U+0750-077F,U+FB50-FDFF,U+FE70-FEFF}
@font-face{font-family:Cairo;font-weight:400;src:url(fonts/cairo-latin-400-normal.woff2);unicode-range:U+0000-00FF,U+2000-206F,U+20AC,U+2212}
@font-face{font-family:Cairo;font-weight:700;src:url(fonts/cairo-latin-700-normal.woff2);unicode-range:U+0000-00FF,U+2000-206F,U+20AC,U+2212}
@font-face{font-family:Cairo;font-weight:900;src:url(fonts/cairo-latin-900-normal.woff2);unicode-range:U+0000-00FF,U+2000-206F,U+20AC,U+2212}
"""
T="#2DE2C4"; O="#FF8A3D"; TX="#F4F1FF"; MU="#B9B0D6"
css=FONTS+f"""
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#222;font-family:Cairo,sans-serif;direction:rtl;color:{TX}}}
.slide{{width:1080px;height:1350px;position:relative;overflow:hidden;padding:84px;display:block;background:radial-gradient(1000px 700px at 85% -5%,#3A1E6E 0%,#1B1033 45%,#0F0B1E 100%)}}
.top{{display:flex;justify-content:space-between;align-items:center;font-size:28px;font-weight:700;color:{MU}}}
.pill{{padding:10px 28px;border-radius:50px;font-size:28px;font-weight:900;background:rgba(45,226,196,.14);border:2px solid rgba(45,226,196,.5);color:{T}}}
h1,h2{{font-weight:900;line-height:1.2}}
h2{{font-size:84px}}
.t{{color:{T}}} .o{{color:{O}}} .mu{{color:{MU}}}
.card{{background:linear-gradient(135deg,#25173F,#1A1030);border:2px solid #3A2A5E;border-radius:34px;padding:34px 40px;margin-top:24px}}
.ft{{position:absolute;left:84px;right:84px;bottom:56px;display:flex;justify-content:space-between;align-items:center;font-size:26px;font-weight:700;color:{MU}}}
.dots{{display:flex;gap:10px;direction:ltr}} .dots i{{width:14px;height:14px;border-radius:50%;background:#43336B}} .dots i.on{{width:40px;border-radius:8px;background:{T}}}
.num{{min-width:80px;height:80px;border-radius:50%;background:{T};color:#0F0B1E;font-size:50px;font-weight:900;display:flex;align-items:center;justify-content:center}}
.bad{{border-color:#7A2F3C;background:linear-gradient(135deg,#34172A,#220F1E)}} .good{{border-color:#1F7A6A;background:linear-gradient(135deg,#123B3A,#0D2A2E)}}
"""
def foot(n,t="محتوى تعليمي"):
    d="".join(f'<i class="{"on" if i==n else ""}"></i>' for i in range(1,8))
    return f'<div class="ft"><span>{t}</span><div class="dots">{d}</div></div>'
def top(tag,r="الأحد 22 نوفمبر 2026"): return f'<div class="top"><span class="pill">{tag}</span><span>{r}</span></div>'
def why(n,t,b):
    return f'<div class="card" style="display:flex;gap:28px;align-items:flex-start"><div class="num">{n}</div><div><div style="font-size:42px;font-weight:900;line-height:1.35">{t}</div><div style="font-size:30px;color:{MU};line-height:1.55;margin-top:8px">{b}</div></div></div>'
def ba(lbl,txt,cls): 
    return f'<div class="card {cls}"><div style="font-size:28px;font-weight:900;color:{"#FF7A8A" if cls=="bad" else T}">{lbl}</div><div style="font-size:38px;font-weight:900;line-height:1.5;margin-top:8px">{txt}</div></div>'

S=[]
def fix(lbl,txt,cls): return ba(lbl,txt,cls)
S.append(f"""<section class="slide">{top("تجارة إلكترونية")}
<div style="margin-top:140px"><div style="font-size:48px;color:{MU};font-weight:700">وضع المنتج في السلة…</div>
<h1 style="font-size:124px;margin-top:10px">ثم <span class="o">غادر</span> دون شراء</h1>
<p style="font-size:42px;margin-top:46px;line-height:1.6;font-weight:400">4 أسباب شائعة، <br>وكيف تعالج كل واحد منها.</p></div>
<div style="position:absolute;left:84px;bottom:130px;font-size:36px;font-weight:900;color:{T}">اسحب ←</div>{foot(1)}</section>""")
S.append(f"""<section class="slide">{top("لماذا تهمّك؟")}
<h2 style="margin-top:80px">السلة المتروكة<br><span class="t">فرصة قريبة جداً</span></h2>
<div class="card" style="margin-top:50px;font-size:40px;line-height:1.7;font-weight:700">الزائر الذي أضاف منتجاً للسلة أبدى <span class="t">نية شراء</span> واضحة. وأي عائق صغير في الطريق قد <span class="o">يخسّرك البيع</span>.</div>
<p style="font-size:34px;color:{MU};margin-top:36px;line-height:1.6">اعرف العائق، وأزِله.</p>{foot(2)}</section>""")
S.append(f"""<section class="slide">{top("السبب الأول")}
<h2 style="margin-top:60px">تكاليف <span class="o">تظهر</span><br>في آخر خطوة</h2>
{ba("المشكلة","رسوم شحن وضرائب تفاجئ العميل عند الدفع.","bad")}
{ba("الحل","اعرض التكلفة الكاملة أو تقديرها مبكراً في صفحة المنتج والسلة.","good")}
<p style="font-size:32px;color:{MU};margin-top:30px;line-height:1.6">المفاجأة في السعر تهدم الثقة.</p>{foot(3)}</section>""")
S.append(f"""<section class="slide">{top("السبب الثاني")}
<h2 style="margin-top:60px">إجبار العميل على<br><span class="o">إنشاء حساب</span></h2>
{ba("المشكلة","لا يمكن إتمام الشراء إلا بعد التسجيل.","bad")}
{ba("الحل","أتح «الشراء كضيف» واعرض إنشاء الحساب بعد إتمام الطلب.","good")}
<p style="font-size:32px;color:{MU};margin-top:30px;line-height:1.6">قلّل الاحتكاك قدر الإمكان.</p>{foot(4)}</section>""")
S.append(f"""<section class="slide">{top("السبب الثالث")}
<h2 style="margin-top:60px">خطوات طويلة<br><span class="o">وحقول كثيرة</span></h2>
{ba("المشكلة","نموذج دفع طويل بحقول غير ضرورية.","bad")}
{ba("الحل","اطلب المعلومات الضرورية فقط، واجعل الدفع في أقل عدد ممكن من الخطوات.","good")}
<p style="font-size:32px;color:{MU};margin-top:30px;line-height:1.6">كل حقل إضافي سبب جديد للمغادرة.</p>{foot(5)}</section>""")
S.append(f"""<section class="slide">{top("السبب الرابع")}
<h2 style="margin-top:60px">غياب <span class="o">الثقة</span><br>عند الدفع</h2>
{ba("المشكلة","لا طرق دفع مألوفة، ولا سياسة إرجاع واضحة.","bad")}
{ba("الحل","وفّر طرق دفع يعتادها عملاؤك، وأظهر سياسة الإرجاع وبيانات التواصل بوضوح.","good")}
<p style="font-size:32px;color:{MU};margin-top:30px;line-height:1.6">العميل لا يدفع لمن لا يثق به.</p>{foot(6)}</section>""")
def opt(l,t): return f'<div class="card" style="display:flex;gap:24px;align-items:center;padding:24px 36px;margin-top:18px"><div class="num" style="min-width:68px;height:68px;font-size:42px">{l}</div><div style="font-size:38px;font-weight:900">{t}</div></div>'
S.append(f"""<section class="slide">{top("شاركنا رأيك")}
<h1 style="font-size:78px;margin-top:50px;line-height:1.25">أي سبب تعاني منه<br>في <span class="o">متجرك؟</span></h1>
<div style="margin-top:14px">{opt("أ","تكاليف مفاجئة")}{opt("ب","حساب إجباري")}{opt("ج","خطوات دفع طويلة")}{opt("د","ضعف الثقة")}</div>
<p style="font-size:36px;color:{T};margin-top:26px;font-weight:900">اكتب حرفك في التعليقات 👇</p>{foot(7)}</section>""")

html=f"<!doctype html><html lang='ar' dir='rtl'><head><meta charset='utf-8'><style>{css}</style></head><body>{''.join(S)}</body></html>"
(HERE/"story.html").write_text(html,encoding="utf-8")
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1350})
    pg.goto(f"file://{HERE}/story.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(500)
    for i,el in enumerate(pg.query_selector_all(".slide"),1): el.screenshot(path=str(OUT/f"slide-{i}.png"))
    b.close()
print("done")

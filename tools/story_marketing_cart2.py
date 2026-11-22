
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
css=FONTS+"""
*{box-sizing:border-box;margin:0;padding:0}
body{background:#222;font-family:Cairo,sans-serif;direction:rtl}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;padding:84px;display:block}
.cream{background:#FFF1DD;color:#1A0B3B}
.violet{background:radial-gradient(900px 700px at 100% 0%,#7A35E8 0%,#4A1BB0 45%,#2A0F66 100%);color:#fff}
.orange{background:linear-gradient(160deg,#FF8A3D,#FF5A1F);color:#1A0B3B}
.teal{background:linear-gradient(160deg,#2DE2C4,#0FB59F);color:#0E0A24}
.top{display:flex;justify-content:space-between;align-items:center;font-size:28px;font-weight:800;position:relative;z-index:3}
.pill{padding:10px 30px;border-radius:50px;font-size:28px;font-weight:900;background:#1A0B3B;color:#FFD84D}
.violet .pill{background:#FFD84D;color:#1A0B3B}
h1,h2{font-weight:900;line-height:1.12;position:relative;z-index:3}
h2{font-size:100px}
.mark{display:inline-block;padding:0 22px;border-radius:18px;background:#FFD84D;color:#1A0B3B;transform:rotate(-2deg);margin-top:8px}
.markv{display:inline-block;padding:0 22px;border-radius:18px;background:#7A35E8;color:#fff;transform:rotate(-2deg);margin-top:8px}
.bignum{position:absolute;left:-20px;top:120px;font-size:640px;font-weight:900;line-height:1;opacity:.13;z-index:1;direction:ltr}
.box{border-radius:36px;padding:34px 40px;margin-top:26px;position:relative;z-index:3;display:flex;gap:26px;align-items:flex-start}
.bad{background:rgba(26,11,59,.88);color:#fff}
.good{background:#fff;color:#1A0B3B;box-shadow:0 14px 0 rgba(26,11,59,.18)}
.cream .bad{background:#1A0B3B;color:#fff}
.lab{font-size:28px;font-weight:900;margin-bottom:6px}
.bad .lab{color:#FF8A9B}.good .lab{color:#0E9E88}
.txt{font-size:41px;font-weight:900;line-height:1.5}
.ic{min-width:74px;height:74px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:44px;font-weight:900}
.bad .ic{background:#FF4D6A;color:#fff}.good .ic{background:#2DE2C4;color:#0E0A24}
.ft{position:absolute;left:84px;right:84px;bottom:56px;display:flex;justify-content:space-between;align-items:center;font-size:26px;font-weight:800;z-index:3}
.dots{display:flex;gap:10px;direction:ltr}.dots i{width:14px;height:14px;border-radius:50%;background:currentColor;opacity:.3}.dots i.on{width:44px;border-radius:8px;opacity:1}
.big{position:absolute;z-index:2}
"""
def foot(n,t="محتوى تعليمي"):
    d="".join(f'<i class="{"on" if i==n else ""}"></i>' for i in range(1,8))
    return f'<div class="ft"><span>{t}</span><div class="dots">{d}</div></div>'
def top(tag): return f'<div class="top"><span class="pill">{tag}</span><span>الأحد 22 نوفمبر 2026</span></div>'
CART='<svg viewBox="0 0 64 64" width="{w}" height="{w}"><path d="M5 8h9l7 32h29l6-23H16" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="26" cy="52" r="5" fill="currentColor"/><circle cx="46" cy="52" r="5" fill="currentColor"/></svg>'
def icon(kind,w=190):
    p={"money":'<circle cx="32" cy="32" r="26" fill="none" stroke="currentColor" stroke-width="5"/><text x="32" y="44" text-anchor="middle" font-size="34" font-weight="900" fill="currentColor" font-family="Cairo">$</text>',
       "user":'<circle cx="32" cy="22" r="11" fill="none" stroke="currentColor" stroke-width="5"/><path d="M10 56c2-14 12-20 22-20s20 6 22 20" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round"/>',
       "steps":'<rect x="8" y="10" width="48" height="10" rx="5" fill="currentColor"/><rect x="8" y="27" width="48" height="10" rx="5" fill="currentColor"/><rect x="8" y="44" width="48" height="10" rx="5" fill="currentColor"/>',
       "shield":'<path d="M32 5l22 8v17c0 14-9 24-22 29C19 54 10 44 10 30V13z" fill="none" stroke="currentColor" stroke-width="5" stroke-linejoin="round"/><path d="M21 32l8 8 14-16" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'}[kind]
    return f'<svg viewBox="0 0 64 64" width="{w}" height="{w}">{p}</svg>'
def reason(theme,n,tag,head,ik,prob,sol,note):
    return f"""<section class="slide {theme}">{top(tag)}
<div class="bignum">{n}</div>
<div class="big" style="left:70px;top:200px;opacity:.9">{icon(ik,170)}</div>
<h2 style="margin-top:70px">{head}</h2>
<div class="box bad" style="margin-top:50px"><div class="ic">✕</div><div><div class="lab">المشكلة</div><div class="txt">{prob}</div></div></div>
<div class="box good"><div class="ic">✓</div><div><div class="lab">الحل</div><div class="txt">{sol}</div></div></div>
<p style="font-size:34px;font-weight:800;margin-top:34px;position:relative;z-index:3;opacity:.85">{note}</p>
{foot(n+2)}</section>"""
S=[]
S.append(f"""<section class="slide orange">{top("تجارة إلكترونية")}
<div class="big" style="left:40px;bottom:150px;opacity:.95;color:#1A0B3B">{CART.format(w=560)}</div>
<div style="margin-top:110px;position:relative;z-index:3">
<h1 style="font-size:138px">زبونك<br>ترك <span class="mark" style="background:#1A0B3B;color:#FFD84D">السلة؟</span></h1>
<p style="font-size:46px;margin-top:40px;font-weight:800;line-height:1.5">4 أسباب شائعة<br>وكيف تعالجها</p></div>
<div class="big" style="right:84px;bottom:130px;font-size:38px;font-weight:900;color:#1A0B3B">اسحب ←</div>{foot(1)}</section>""")
S.append(f"""<section class="slide violet">{top("لماذا تهمّك؟")}
<div class="big" style="left:-40px;top:380px;opacity:.14;color:#fff">{CART.format(w=640)}</div>
<h2 style="margin-top:90px">السلة المتروكة<br>هي بيع <span class="mark">كاد يتم</span></h2>
<div class="box" style="background:#fff;color:#1A0B3B;margin-top:60px;display:block;font-size:42px;font-weight:900;line-height:1.6">الزائر الذي أضاف منتجاً للسلة أبدى <span style="color:#7A35E8">نية شراء</span> واضحة، وأي عائق صغير قد يخسّرك البيع.</div>
<p style="font-size:38px;font-weight:900;margin-top:36px;color:#FFD84D;position:relative;z-index:3">اعرف العائق… وأزِله.</p>{foot(2)}</section>""")
S.append(reason("cream",1,"السبب الأول",'تكاليف <span class="mark">تظهر</span><br>في آخر خطوة',"money","رسوم شحن وضرائب تفاجئ العميل عند الدفع.","اعرض التكلفة الكاملة أو تقديرها مبكراً في صفحة المنتج والسلة.","المفاجأة في السعر تهدم الثقة."))
S.append(reason("violet",2,"السبب الثاني",'إجبار العميل على <span class="mark">إنشاء حساب</span>',"user","لا يمكن إتمام الشراء إلا بعد التسجيل.","أتح «الشراء كضيف»، واعرض إنشاء الحساب بعد إتمام الطلب.","قلّل الاحتكاك قدر الإمكان."))
S.append(reason("orange",3,"السبب الثالث",'خطوات طويلة <span class="mark" style="background:#1A0B3B;color:#FFD84D">وحقول كثيرة</span>',"steps","نموذج دفع طويل بحقول غير ضرورية.","اطلب المعلومات الضرورية فقط، واجعل الدفع في أقل عدد ممكن من الخطوات.","كل حقل إضافي سبب جديد للمغادرة."))
S.append(reason("teal",4,"السبب الرابع",'غياب <span class="mark" style="background:#1A0B3B;color:#FFD84D">الثقة</span> عند الدفع',"shield","لا طرق دفع مألوفة، ولا سياسة إرجاع واضحة.","وفّر طرق دفع يعتادها عملاؤك، وأظهر سياسة الإرجاع وبيانات التواصل.","العميل لا يدفع لمن لا يثق به."))
def opt(l,t,c): return f'<div class="box" style="background:#fff;color:#1A0B3B;align-items:center;padding:22px 34px;margin-top:20px;box-shadow:0 10px 0 rgba(0,0,0,.25)"><div class="ic" style="background:{c};color:#fff;min-width:76px;height:76px">{l}</div><div style="font-size:44px;font-weight:900">{t}</div></div>'
S.append(f"""<section class="slide violet">{top("شاركنا رأيك")}
<h1 style="font-size:104px;margin-top:60px">أي سبب <span class="mark">يضرّ</span><br>متجرك؟</h1>
<div style="margin-top:16px">{opt("أ","تكاليف مفاجئة","#FF8A3D")}{opt("ب","حساب إجباري","#7A35E8")}{opt("ج","خطوات دفع طويلة","#0FB59F")}{opt("د","ضعف الثقة","#FF4D6A")}</div>
<p style="font-size:40px;color:#FFD84D;margin-top:34px;font-weight:900;position:relative;z-index:3">اكتب حرفك في التعليقات 👇</p>{foot(7)}</section>""")
html=f"<!doctype html><html lang='ar' dir='rtl'><head><meta charset='utf-8'><style>{css}</style></head><body>{''.join(S)}</body></html>"
(HERE/"story.html").write_text(html,encoding="utf-8")
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1350})
    pg.goto(f"file://{HERE}/story.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(500)
    for i,el in enumerate(pg.query_selector_all(".slide"),1): el.screenshot(path=str(OUT/f"slide-{i}.png"))
    b.close()
print("done")

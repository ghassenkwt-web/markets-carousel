import pathlib
HERE=pathlib.Path(__file__).resolve().parent
src=(HERE/"story_marketing_booking.py").read_text(encoding="utf-8").split("S=[]")[0]
g={"__file__":str(HERE/"story_marketing_booking.py")}
exec(compile(src,"booking","exec"),g)
css=g["css"];foot=g["foot"];top=g["top"];icon=g["icon"];reason=g["reason"]
FOLDER=HERE.parent/"marketing"/"2026-11-22-whatsapp-lead"; FOLDER.mkdir(parents=True,exist_ok=True)
DK='style="background:#1A0B3B;color:#FFD84D"'
DT='style="background:#1A0B3B;color:#2DE2C4"'
S=[]
CHAT='<svg viewBox="0 0 64 64" width="{w}" height="{w}"><path d="M10 10h44a5 5 0 0 1 5 5v27a5 5 0 0 1-5 5H28L14 58V47h-4a5 5 0 0 1-5-5V15a5 5 0 0 1 5-5z" fill="none" stroke="currentColor" stroke-width="5" stroke-linejoin="round"/><circle cx="21" cy="29" r="3.5" fill="currentColor"/><circle cx="32" cy="29" r="3.5" fill="currentColor"/><circle cx="43" cy="29" r="3.5" fill="currentColor"/></svg>'
S.append(f"""<section class="slide orange">{top("الخدمات")}
<div class="big" style="left:40px;bottom:150px;opacity:.95;color:#1A0B3B">{CHAT.format(w=520)}</div>
<div style="margin-top:110px;position:relative;z-index:3">
<h1 style="font-size:122px">وصلك استفسار<br>على واتساب…<br><span class="mark" {DK}>ماذا بعده؟</span></h1>
<p style="font-size:46px;margin-top:40px;font-weight:800;line-height:1.5">4 خطوات تحوّله<br>إلى عميل</p></div>
<div class="big" style="right:84px;bottom:130px;font-size:38px;font-weight:900;color:#1A0B3B">اسحب ←</div>{foot(1)}</section>""")
S.append(f"""<section class="slide violet">{top("الفكرة الأساسية")}
<h2 style="margin-top:90px">الاستفسار<br><span class="mark">ليس بيعاً</span></h2>
<div class="box" style="background:#fff;color:#1A0B3B;margin-top:60px;display:block;font-size:42px;font-weight:900;line-height:1.6">السائل مهتم، لكنه <span style="color:#7A35E8">يقارن</span> ويتردد. والرد <span style="color:#7A35E8">المنظّم</span> هو ما يصنع الفرق بينك وبين غيرك.</div>
<p style="font-size:38px;font-weight:900;margin-top:36px;color:#FFD84D;position:relative;z-index:3">اتبع هذه الخطوات الأربع.</p>{foot(2)}</section>""")
S.append(reason("cream",1,"الخطوة الأولى",'ردّ <span class="mark">بسرعة</span>',"clock","يبقى العميل ينتظر ساعات، فيتجه إلى منافس رد أسرع.","ردّ خلال دقائق، وجهّز رسالة ترحيب تلقائية لأوقات انشغالك.","السرعة أول إشارة اهتمام."))
S.append(reason("violet",2,"الخطوة الثانية",'افهم <span class="mark">حاجته</span>',"question","ترسل قائمة الأسعار فوراً دون أن تعرف ماذا يريد.","اسأل سؤالين: ما هدفك؟ وما موعدك أو ميزانيتك؟","السؤال الجيد يسبق العرض."))
S.append(reason("teal",3,"الخطوة الثالثة",f'قدّم عرضاً <span class="mark" {DK}>واضحاً</span>',"money","رسالة طويلة مبعثرة يضيع فيها المطلوب.","اعرض خياراً أو خيارين بسعر ونتيجة واضحة.","الخيارات القليلة تسهّل القرار."))
S.append(reason("cream",4,"الخطوة الرابعة",'تابع ولا <span class="mark">تختفِ</span>',"steps","ترسل العرض ثم تنتظر بصمت حتى ينساك.","تابع بعد يوم برسالة قصيرة، واعرض خطوة الحجز أو الدفع مباشرة.","المتابعة اللطيفة لا تزعج."))
def opt(l,t,c): return f'<div class="box" style="background:#fff;color:#1A0B3B;align-items:center;padding:22px 34px;margin-top:20px;box-shadow:0 10px 0 rgba(0,0,0,.25)"><div class="ic" style="background:{c};color:#fff;min-width:76px;height:76px">{l}</div><div style="font-size:44px;font-weight:900">{t}</div></div>'
S.append(f"""<section class="slide violet">{top("شاركنا رأيك")}
<h1 style="font-size:100px;margin-top:60px">أين <span class="mark">تضيع</span><br>استفساراتك؟</h1>
<div style="margin-top:16px">{opt("أ","بطء الرد","#FF8A3D")}{opt("ب","عدم فهم الحاجة","#7A35E8")}{opt("ج","عرض غير واضح","#0FB59F")}{opt("د","غياب المتابعة","#E0187A")}</div>
<p style="font-size:40px;color:#FFD84D;margin-top:34px;font-weight:900;position:relative;z-index:3">اكتب حرفك في التعليقات 👇</p>{foot(7)}</section>""")
html=f"<!doctype html><html lang='ar' dir='rtl'><head><meta charset='utf-8'><style>{css}</style></head><body>{''.join(S)}</body></html>"
(HERE/"story_wa.html").write_text(html,encoding="utf-8")
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1350})
    pg.goto(f"file://{HERE}/story_wa.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(500)
    for i,el in enumerate(pg.query_selector_all(".slide"),1): el.screenshot(path=str(FOLDER/f"slide-{i}.png"))
    b.close()
print("done")

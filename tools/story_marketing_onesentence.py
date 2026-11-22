import pathlib
HERE=pathlib.Path(__file__).resolve().parent
src=(HERE/"story_marketing_booking.py").read_text(encoding="utf-8").split("S=[]")[0]
g={"__file__":str(HERE/"story_marketing_booking.py")}
exec(compile(src,"booking","exec"),g)
css=g["css"];foot=g["foot"];top=g["top"];icon=g["icon"];reason=g["reason"]
FOLDER=HERE.parent/"marketing"/"2026-11-22-one-sentence"; FOLDER.mkdir(parents=True,exist_ok=True)
DK='style="background:#1A0B3B;color:#FFD84D"'
DT='style="background:#1A0B3B;color:#2DE2C4"'
S=[]
# 1 غلاف برتقالي (حسب قاعدة التناوب)
S.append(f"""<section class="slide orange">{top("الخدمات")}
<div class="big" style="left:40px;bottom:150px;opacity:.95;color:#1A0B3B">{icon("question",480)}</div>
<div style="margin-top:110px;position:relative;z-index:3">
<h1 style="font-size:132px">هل تشرح خدمتك<br><span class="mark" {DK}>بجملة واحدة؟</span></h1>
<p style="font-size:46px;margin-top:40px;font-weight:800;line-height:1.5">قالب من 4 عناصر<br>يفهمه أي عميل</p></div>
<div class="big" style="right:84px;bottom:130px;font-size:38px;font-weight:900;color:#1A0B3B">اسحب ←</div>{foot(1)}</section>""")
# 2 القالب
S.append(f"""<section class="slide violet">{top("القالب")}
<h2 style="margin-top:90px">الجملة الواضحة<br><span class="mark">تبيع</span></h2>
<div class="box" style="background:#fff;color:#1A0B3B;margin-top:60px;display:block;font-size:42px;font-weight:900;line-height:1.7">أساعد <span style="color:#7A35E8">[فئة محددة]</span> على <span style="color:#7A35E8">[نتيجة محددة]</span> عبر <span style="color:#7A35E8">[طريقة بسيطة]</span>.</div>
<p style="font-size:38px;font-weight:800;margin-top:40px;line-height:1.6;position:relative;z-index:3">مثال: أساعد أصحاب المتاجر الإلكترونية على زيادة مبيعاتهم عبر إعلانات مدروسة.</p>
<p style="font-size:38px;font-weight:900;margin-top:26px;color:#FFD84D;position:relative;z-index:3">جرّب القالب على خدمتك.</p>{foot(2)}</section>""")
S.append(reason("cream",1,"العنصر الأول",'حدّد <span class="mark">الفئة</span>',"user","تقول «أخدم الجميع»، فلا يشعر أحد أنك تقصده.","اذكر فئة واحدة بوضوح: أصحاب المتاجر، العيادات، المطاعم…","التحديد يجذب أكثر من العموم."))
S.append(reason("violet",2,"العنصر الثاني",'اذكر <span class="mark">النتيجة</span>',"star","تتحدث عن عملك: «أقدّم خدمات تسويقية متكاملة».","تحدّث عمّا يحصل عليه العميل: مبيعات أكثر، حجوزات أكثر، وقت أقل.","العميل يشتري النتيجة لا الخدمة."))
S.append(reason("orange",3,"العنصر الثالث",f'وضّح <span class="mark" {DK}>الطريقة</span>',"steps","نتيجة بلا طريقة تبدو وعداً فارغاً.","أضف عبارة قصيرة تشرح كيف: «عبر إعلانات مدروسة وصفحة هبوط واضحة».","الطريقة تمنح الوعد مصداقية."))
S.append(reason("teal",4,"العنصر الرابع",f'بلا <span class="mark" {DK}>مصطلحات</span>',"shield","عبارات مثل «حلول متكاملة» لا يفهمها العميل.","اكتب بكلمات يقولها عميلك في حياته اليومية.","إن لم يفهمك بسرعة، سيتجاوزك."))
def opt(l,t,c): return f'<div class="box" style="background:#fff;color:#1A0B3B;align-items:center;padding:22px 34px;margin-top:20px;box-shadow:0 10px 0 rgba(0,0,0,.25)"><div class="ic" style="background:{c};color:#fff;min-width:76px;height:76px">{l}</div><div style="font-size:44px;font-weight:900">{t}</div></div>'
S.append(f"""<section class="slide violet">{top("شاركنا رأيك")}
<h1 style="font-size:100px;margin-top:60px">أي عنصر <span class="mark">ينقص</span><br>جملتك؟</h1>
<div style="margin-top:16px">{opt("أ","الفئة المحددة","#FF8A3D")}{opt("ب","النتيجة","#7A35E8")}{opt("ج","الطريقة","#0FB59F")}{opt("د","الوضوح والبساطة","#E0187A")}</div>
<p style="font-size:40px;color:#FFD84D;margin-top:34px;font-weight:900;position:relative;z-index:3">اكتب حرفك في التعليقات 👇</p>{foot(7)}</section>""")
html=f"<!doctype html><html lang='ar' dir='rtl'><head><meta charset='utf-8'><style>{css}</style></head><body>{''.join(S)}</body></html>"
(HERE/"story_os.html").write_text(html,encoding="utf-8")
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1350})
    pg.goto(f"file://{HERE}/story_os.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(500)
    for i,el in enumerate(pg.query_selector_all(".slide"),1): el.screenshot(path=str(FOLDER/f"slide-{i}.png"))
    b.close()
print("done")

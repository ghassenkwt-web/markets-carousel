# Inflection carousel: leverage (educational, no market data). Themes rotate per slide.
import pathlib, datetime
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent
DATE = "2026-11-23"
OUT = REPO / f"{DATE}-leverage"; OUT.mkdir(exist_ok=True)
TOTAL = 7
def L(t): return f'<span class="ltr" dir="ltr">{t}</span>'
THEMES = {
 "navy":   ("#080C16", "#F5B942", "245,185,66"),
 "teal":   ("#041A18", "#2DE2C4", "45,226,196"),
 "orange": ("#1F0E05", "#FF9A4D", "255,154,77"),
 "purple": ("#12062B", "#FFD84D", "255,216,77"),
}
fonts = "".join(f"@font-face{{font-family:Cairo;font-weight:{w};src:url(fonts/cairo-{s}-{w}-normal.woff2);unicode-range:{r}}}"
  for w in (400,700,900) for s,r in (("arabic","U+0600-06FF,U+0750-077F,U+FB50-FDFF,U+FE70-FEFF"),("latin","U+0000-00FF,U+2000-206F,U+20AC,U+2212")))
css = fonts + """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#000;font-family:Cairo,sans-serif;direction:rtl}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;color:#EEF2FB;padding:150px 84px 120px;
 background:radial-gradient(1100px 700px at 50% -8%,rgba(var(--rgb),.20) 0%,transparent 60%),var(--base)}
.slide::before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(to bottom,transparent 0,transparent 53px,rgba(255,255,255,.028) 53px,rgba(255,255,255,.028) 54px);pointer-events:none}
.logo{position:absolute;left:-380px;bottom:-300px;width:1300px;height:1300px;opacity:.16;pointer-events:none}
.ltr{direction:ltr;unicode-bidi:isolate;display:inline-block}
.brand{position:absolute;top:44px;left:50%;transform:translateX(-50%);font-size:36px;font-weight:800;color:var(--acc);display:flex;align-items:flex-end;gap:5px;letter-spacing:1px}
.brand i{width:10px;height:10px;border-radius:50%;background:var(--acc);display:block;margin-bottom:9px}
.top{position:absolute;top:44px;left:84px;right:84px;display:flex;justify-content:space-between;align-items:center;font-size:27px;color:rgba(238,242,251,.5);font-weight:700}
.pill{background:rgba(var(--rgb),.13);color:var(--acc);border:1.5px solid rgba(var(--rgb),.4);padding:6px 24px;border-radius:40px;font-size:27px;font-weight:800}
h1,h2{font-weight:800;line-height:1.25;position:relative}
h2{font-size:80px}
.acc{color:var(--acc)} .red{color:#FF5A67} .green{color:#2ED8A0} .muted{color:rgba(238,242,251,.62)}
.card{background:rgba(255,255,255,.045);border:1.5px solid rgba(var(--rgb),.28);border-radius:30px;position:relative}
.foot{position:absolute;bottom:46px;left:84px;right:84px;display:flex;justify-content:space-between;align-items:center;font-size:25px;color:rgba(238,242,251,.45);font-weight:700}
.dots{display:flex;gap:10px;direction:ltr}.dots i{width:14px;height:14px;border-radius:50%;background:rgba(255,255,255,.18);display:block}
.dots i.on{background:var(--acc);width:40px;border-radius:8px}
"""
LOGO = '<svg class="logo" viewBox="0 0 120 120" fill="none" stroke="var(--acc)" stroke-linecap="round"><path d="M12 96 C 44 96, 70 30, 108 24" stroke-width="3.2"/><path d="M12 96 L108 24" stroke-width="1.6" stroke-dasharray="3 5"/><circle cx="60" cy="60" r="4.2" fill="var(--acc)" stroke="none"/></svg>'
def slide(n, theme, pill, sub, body):
    b,a,r = THEMES[theme]
    dots = "".join(f'<i class="{"on" if i==n else ""}"></i>' for i in range(1,TOTAL+1))
    return f'''<section class="slide" style="--base:{b};--acc:{a};--rgb:{r}">{LOGO}
 <div class="brand">inflection<i></i></div>
 <div class="top"><span class="pill">{pill}</span><span>{sub}</span></div>
 {body}
 <div class="foot"><span>محتوى تعليمي وليس نصيحة استثمارية</span><div class="dots">{dots}</div></div></section>'''
def card_n(n,t,b):
    return f'''<div class="card" style="padding:30px 40px;margin-top:24px;display:flex;gap:30px;align-items:flex-start">
 <div style="min-width:78px;height:78px;border-radius:22px;background:rgba(var(--rgb),.14);border:1.5px solid rgba(var(--rgb),.45);color:var(--acc);font-size:48px;font-weight:800;display:flex;align-items:center;justify-content:center">{L(n)}</div>
 <div><div style="font-size:40px;font-weight:800;line-height:1.3">{t}</div><div style="font-size:30px;line-height:1.55;margin-top:8px" class="muted">{b}</div></div></div>'''
def stat(label, val, sub, cls="acc"):
    return f'''<div class="card" style="padding:28px 40px;margin-top:22px">
 <div style="display:flex;justify-content:space-between;align-items:baseline"><div style="font-size:38px;font-weight:800">{label}</div><div class="{cls}" style="font-size:64px;font-weight:800">{L(val)}</div></div>
 <div style="font-size:29px;line-height:1.5;margin-top:6px" class="muted">{sub}</div></div>'''
def row(lev, mv):
    return f'''<div class="card" style="padding:14px 40px;margin-top:14px;display:flex;justify-content:space-between;align-items:center">
 <div><div class="muted" style="font-size:24px">الرافعة</div><div class="acc" style="font-size:50px;font-weight:800">{L(lev)}</div></div>
 <div style="font-size:44px" class="muted">←</div>
 <div style="text-align:left"><div class="muted" style="font-size:24px">حركة عكسية تمحو الحساب</div><div class="red" style="font-size:50px;font-weight:800">{L(mv)}</div></div></div>'''
def opt(l,t):
    return f'<div class="card" style="padding:26px 40px;margin-top:20px;display:flex;gap:28px;align-items:center"><div style="min-width:76px;height:76px;border-radius:50%;background:var(--acc);color:var(--base);font-size:46px;font-weight:800;display:flex;align-items:center;justify-content:center">{l}</div><div style="font-size:42px;font-weight:800">{t}</div></div>'
S=[]
S.append(slide(1,"navy","درس التداول","الرافعة المالية",f'''
 <div style="margin-top:80px;position:relative">
  <div style="font-size:48px;font-weight:700" class="muted">بسلاح رافعة {L("10x")}</div>
  <div style="direction:ltr;text-align:right;font-size:230px;font-weight:800;line-height:1.1" class="red">1%</div>
  <h1 style="font-size:82px;margin-top:6px">ضدك تعني خسارة <span class="acc">{L("10%")}</span> من حسابك</h1>
  <p style="font-size:40px;margin-top:34px;line-height:1.55;font-weight:400" class="muted">الرافعة تكبّر الربح والخسارة معاً.</p>
 </div>
 <div style="position:absolute;left:84px;bottom:130px;font-size:34px;font-weight:700" class="muted">اسحب للمزيد ←</div>'''))
S.append(slide(2,"teal","المفهوم","ما هي الرافعة؟",f'''
 <h2 style="margin-top:50px">قرض يمنحك حجم صفقة <span class="acc">أكبر</span> من رصيدك</h2>
 {stat("رصيدك",f"1,000$","المبلغ الذي تملكه فعلاً.")}
 {stat("الرافعة","10x","يقرضك الوسيط الفارق.")}
 {stat("حجم الصفقة","10,000$","تتحرك كأنك تملك هذا المبلغ كله.")}'''))
S.append(slide(3,"orange","مقارنة","الأثر على الحساب",f'''
 <h2 style="margin-top:50px">السعر تحرك <span class="acc">{L("2%")}</span> فقط</h2>
 <div class="card" style="padding:30px 40px;margin-top:30px">
  <div style="font-size:34px;font-weight:800" class="muted">بدون رافعة (حساب {L("1,000$")})</div>
  <div style="display:flex;justify-content:space-between;margin-top:10px;font-size:56px;font-weight:800"><span class="green">{L("+20$")}</span><span class="red">{L("−20$")}</span></div>
  <div style="font-size:28px" class="muted">أي {L("2%")} من الحساب</div></div>
 <div class="card" style="padding:30px 40px;margin-top:24px">
  <div style="font-size:34px;font-weight:800" class="muted">برافعة {L("10x")} (صفقة {L("10,000$")})</div>
  <div style="display:flex;justify-content:space-between;margin-top:10px;font-size:56px;font-weight:800"><span class="green">{L("+200$")}</span><span class="red">{L("−200$")}</span></div>
  <div style="font-size:28px" class="muted">أي {L("20%")} من الحساب</div></div>
 <p style="font-size:28px;margin-top:20px" class="muted">أمثلة حسابية افتراضية للتوضيح.</p>'''))
S.append(slide(4,"purple","الخطر","نقطة المحو",f'''
 <h2 style="margin-top:20px;font-size:72px">كم حركة تمحو <span class="acc">حسابك؟</span></h2>
 <div style="position:relative;margin-top:6px">
  {row("2x","50%")}{row("5x","20%")}{row("10x","10%")}{row("20x","5%")}{row("50x","2%")}
 </div>
 <p style="font-size:27px;margin-top:20px;line-height:1.5" class="muted">القاعدة: {L("100")} مقسومة على الرافعة. عملياً يغلق الوسيط الصفقة غالباً قبل ذلك.</p>'''))
S.append(slide(5,"navy","مخاطر خفية","ما لا يُقال",f'''
 <h2 style="margin-top:50px">ثلاثة <span class="acc">مخاطر</span> تتجاهلها</h2>
 {card_n("1","الإغلاق القسري","يغلق الوسيط صفقتك تلقائياً عند نقص الهامش، فتتحقق الخسارة.")}
 {card_n("2","التكاليف","فوائد التمويل والعمولات تُحسب على حجم الصفقة كاملاً.")}
 {card_n("3","الفجوات السعرية","قد يقفز السعر متجاوزاً وقف الخسارة فتكبر الخسارة عن المخطط.")}'''))
S.append(slide(6,"teal","الخلاصة","كيف تتعامل معها",f'''
 <h2 style="margin-top:50px">ثلاث قواعد <span class="acc">للبقاء</span></h2>
 {card_n("1","ابدأ برافعة منخفضة","كلما قلّت الرافعة اتسع هامش الخطأ.")}
 {card_n("2","حدّد المخاطرة بالمبلغ","اسأل: كم أخسر إن أُصيبت الصفقة؟ قبل أن تسأل: كم أربح؟")}
 {card_n("3","ضع وقف الخسارة","خطة الخروج تُكتب قبل الدخول وليس بعده.")}'''))
S.append(slide(7,"orange","اختبر نفسك","سؤال سريع",f'''
 <h1 style="font-size:70px;margin-top:50px">برافعة {L("20x")} تحرك السعر <span class="acc">{L("5%")}</span> ضدك. ماذا يحدث؟</h1>
 <div style="margin-top:16px">{opt("أ","خسارة "+L("5%")+" من الحساب")}{opt("ب","خسارة "+L("50%")+" من الحساب")}{opt("ج","خسارة "+L("100%")+" من الحساب")}</div>
 <p style="font-size:36px;margin-top:28px;font-weight:800" class="acc">اكتب حرفك في التعليقات ↓</p>
 <p style="font-size:23px;margin-top:16px;line-height:1.6" class="muted">المحتوى تعليمي وليس توصية استثمارية. التداول ينطوي على مخاطر وقد تخسر جزءاً من رأس مالك أو كله.</p>'''))
html = f"<!doctype html><html lang='ar' dir='rtl'><head><meta charset='utf-8'><style>{css}</style></head><body>{''.join(S)}</body></html>"
(HERE/"story.html").write_text(html, encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width":1080,"height":1350})
    pg.goto(f"file://{HERE}/story.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(600)
    for i, el in enumerate(pg.query_selector_all(".slide"), 1):
        el.screenshot(path=str(OUT/f"slide-{i}.png"))
    b.close()
print("done")

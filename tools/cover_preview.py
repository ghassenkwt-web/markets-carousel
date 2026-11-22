import pathlib
HERE=pathlib.Path(__file__).parent
src=(HERE/"story_marketing_booking.py").read_text(encoding="utf-8").split("S=[]")[0]
g={"__file__":str(HERE/"story_marketing_booking.py")}
exec(compile(src,"booking","exec"),g)
css=g["css"];foot=g["foot"];top=g["top"];CAL=g["CAL"]
extra="""
.yellow{background:linear-gradient(160deg,#FFE066,#FFC400);color:#1A0B3B}
.pink{background:linear-gradient(160deg,#FF5FA2,#E0187A);color:#fff}
.pink .pill{background:#FFD84D;color:#1A0B3B}
"""
# (class, mark bg, mark fg, icon color)
V=[("orange","#1A0B3B","#FFD84D","#1A0B3B"),("violet","#FFD84D","#1A0B3B","#FFD84D"),("teal","#1A0B3B","#2DE2C4","#1A0B3B"),("yellow","#FF5A1F","#1A0B3B","#1A0B3B"),("pink","#FFD84D","#1A0B3B","#fff")]
def cover(c,mb,mf,ic):
    return f"""<section class="slide {c}">{top("الخدمات")}
<div class="big" style="left:40px;bottom:150px;opacity:.95;color:{ic}">{CAL.format(w=520)}</div>
<div style="margin-top:110px;position:relative;z-index:3">
<h1 style="font-size:132px">عميلك مهتم…<br><span class="mark" style="background:{mb};color:{mf}">لكنه لم يحجز؟</span></h1>
<p style="font-size:46px;margin-top:40px;font-weight:800;line-height:1.5">4 أسباب شائعة<br>وكيف تعالجها</p></div>
<div class="big" style="right:84px;bottom:130px;font-size:38px;font-weight:900">اسحب ←</div>{foot(1)}</section>"""
html=f"<!doctype html><html lang='ar' dir='rtl'><head><meta charset='utf-8'><style>{css}{extra}</style></head><body>{''.join(cover(*v) for v in V)}</body></html>"
(HERE/"covers.html").write_text(html,encoding="utf-8")
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1350})
    pg.goto(f"file://{HERE}/covers.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(500)
    for (c,*_),el in zip(V,pg.query_selector_all(".slide")): el.screenshot(path=str(HERE/"out/covers"/f"cover-{c}.png"))
    b.close()

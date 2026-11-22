# ألوان غلاف كاروسيل التسويق (الشريحة الأولى فقط). تتبدل بالتناوب مع كل كاروسيل جديد.
# (class, mark_bg, mark_fg, icon_color)
COVERS = [
    ("orange", "#1A0B3B", "#FFD84D", "#1A0B3B"),
    ("teal",   "#1A0B3B", "#2DE2C4", "#1A0B3B"),
]
def next_cover(count_so_far):
    return COVERS[count_so_far % len(COVERS)]

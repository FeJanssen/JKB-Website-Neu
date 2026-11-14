import os

ROOT = "/Users/FJMarketing/Desktop/JKB-Website"
SKIP_DIRS = {"NEW WEB", "template LP", "Assets", "netlify", "node_modules", ".git"}

OLD = '<li class="nav-item"><a href="/integrations" class="nav-link block false">Integrations</a></li>'

NEW = ('<li class="nav-item jkb-dropdown"><a href="#" class="nav-link block false" onclick="return false">Produkte '
       '<svg style="display:inline-block;width:10px;height:10px;margin-left:2px" viewBox="0 0 10 6" fill="none"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></a>'
       '<ul class="jkb-dropdown-menu">'
       '<li><a href="/jkb-grounds.html">JKB Grounds</a></li>'
       '<li><a href="/jkb-hotels.html">JKB Hotels</a></li>'
       '<li><a href="/jkb-cloud.html">JKB Cloud</a></li>'
       '<li><a href="/jkb-office-custom.html">JKB Office Custom</a></li>'
       '</ul></li>')

STYLE = ('<style>'
         '.jkb-dropdown{position:relative}'
         '.jkb-dropdown-menu{display:none;list-style:none;margin:0;padding:8px 0;min-width:200px}'
         '@media (min-width:1024px){'
         '.jkb-dropdown-menu{position:absolute;top:100%;left:0;background:rgba(20,20,25,.95);backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.1);border-radius:16px;padding:10px;z-index:100}'
         '.jkb-dropdown:hover .jkb-dropdown-menu{display:block}'
         '.jkb-dropdown::after{content:"";position:absolute;top:100%;left:0;right:0;height:12px}'
         '}'
         '@media (max-width:1023px){.jkb-dropdown .jkb-dropdown-menu{display:block;padding-left:16px}}'
         '.jkb-dropdown-menu a{display:block;padding:8px 14px;color:inherit;text-decoration:none;border-radius:10px;white-space:nowrap;font-size:.95em}'
         '.jkb-dropdown-menu a:hover{background:rgba(255,255,255,.08)}'
         '</style>')

changed = 0
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for fn in filenames:
        if not fn.endswith(".html"):
            continue
        p = os.path.join(dirpath, fn)
        with open(p, encoding="utf-8", errors="ignore") as f:
            html = f.read()
        if OLD not in html:
            continue
        html = html.replace(OLD, NEW)
        if ".jkb-dropdown" not in html.split("</head>")[0]:
            html = html.replace("</head>", STYLE + "</head>", 1)
        with open(p, "w", encoding="utf-8") as f:
            f.write(html)
        changed += 1
        print("updated:", os.path.relpath(p, ROOT))
print("total:", changed)

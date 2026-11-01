# -*- coding: utf-8 -*-
import re

P = "/Users/FJMarketing/Desktop/JKB-Website/case-study/index.html"
s = open(P, encoding="utf-8").read()

# ---------- Kartenvorlage ----------
def card(img, badge, title, href, desc, s1v, s1l, s2v, s2l):
    return (
    '<div class="grid lg:grid-cols-2 gap-4">'
    '<div class="relative overflow-hidden rounded-2xl min-h-80 bg-light">'
    f'<img src="{img}" alt="{title}" loading="lazy" decoding="async" width="1290" height="520" class="absolute inset-0 w-full h-full object-cover">'
    '<div class="absolute inset-0 bg-linear-to-t from-dark/80 via-transparent to-transparent"></div>'
    '</div>'
    '<div class="p-8 xl:p-10 rounded-2xl bg-light border border-border">'
    f'<div class="px-4 py-1.5 bg-white max-w-min text-dark rounded-lg text-sm font-medium mb-12" style="white-space:nowrap">{badge}</div>'
    '<h3 class="text-h4 font-bold text-white mt-4 mb-3 hover:text-primary transition-colors duration-200">'
    f'<a href="{href}">{title}</a></h3>'
    f'<p class="text-text-dark text-lg">{desc}</p>'
    '<div class="flex items-center justify-between gap-8 mt-20">'
    f'<div class="flex flex-col"><div class="text-h3 font-bold font-secondary text-white">{s1v}</div><p class="text-sm text-text tracking-wide">{s1l}</p></div>'
    f'<div class="flex flex-col"><div class="text-h3 font-bold font-secondary text-white">{s2v}</div><p class="text-sm text-text tracking-wide">{s2l}</p></div>'
    '</div></div></div>')

cards = (
 card("/Assets/teaserbox_2487233097.png", "Sport &amp; Vereine",
      "JKB Grounds: Platzbuchung &amp; Mitgliederverwaltung für Vereine", "/products/jkb-grounds.html",
      "Tennis- und Sportvereine digitalisieren mit JKB Grounds ihre komplette Verwaltung – von der Online-Platzbuchung über Mitgliederdaten bis zur automatischen SEPA-Abrechnung.",
      "30%", "höhere Platzauslastung", "10+ Std.", "Zeitersparnis pro Woche") +
 card("/_astro/case-study-hero.C9oNQZML_1D457j.webp", "Künstliche Intelligenz",
      "EDITH: Die eigene Unternehmens-KI mit Wissensdatenbank &amp; ERP-Anbindung", "/contact",
      "EDITH ist unsere selbst entwickelte KI-Assistentin: Sie kennt das gesamte Unternehmenswissen, beantwortet Fragen der Mitarbeiter sofort und ist direkt an das ERP-System angebunden – Auskünfte, Auswertungen und Routineaufgaben laufen automatisch.",
      "24/7", "sofortige Antworten", "ERP", "direkt angebunden") +
 card("/_astro/case-study-hero-2.Bv6b2Jci_Z2l6ENr.webp", "Cloud &amp; IT",
      "JKB Cloud: Sichere Unternehmens-Cloud – DSGVO-konform", "/contact",
      "Mit JKB Cloud erhalten Unternehmen und Vereine eine sichere Cloud-Infrastruktur: zentrale Datenhaltung, Zugriff von überall und volle DSGVO-Konformität – ohne eigene IT-Abteilung.",
      "100%", "DSGVO-konform", "99,9%", "Verfügbarkeit") +
 card("/_astro/about_hero.CeUJLs4E_Z2toHF5.webp", "Öffentliche Verwaltung",
      "CivicPulse: Die Verwaltungsapp für Städte &amp; Gemeinden", "/contact",
      "CivicPulse verbindet Bürger und Verwaltung: Ankündigungen und Neuigkeiten direkt aufs Smartphone, digitale Anträge und ein zentrales Dokumentenmanagement – weniger Papier, kürzere Wege, zufriedenere Bürger.",
      "2-in-1", "App für Bürger &amp; Verwaltung", "100%", "digitale Dokumente")
)

m = re.search(r'(<div class="grid gap-7 lg:gap-14">).*?(</div></div></section>)', s, re.S)
assert m, "Karten-Container nicht gefunden"
s = s[:m.start()] + m.group(1) + cards + "</div></div></section>" + s[m.end():]

R = [
("Case Study - The All-In-One Growth Software", "Referenzen | JKB Software"),
("Case Studies - All-In-One Local Business Software", "Referenzen | JKB Software"),
("Real Results From Local", "Echte Projekte, echte"),
(">Businesses<", ">Ergebnisse<"),
("See how local companies across different industries are capturing more leads, automating follow-ups, and driving explosive growth without hiring extra staff.",
 "Von der Vereinsverwaltung über Unternehmens-KI bis zur Bürger-App: Ein Einblick in die Lösungen, die wir für unsere Kunden entwickelt haben."),
("Real Stories From Local", "Echte Stimmen von"),
("Business Owners", "Vereinen &amp; Betrieben"),
("We used to lose at least 3-4 jobs a week because we couldn't answer the phone while on a roof. The Missed Call Auto-Responder immediately cut that to zero. This software pays for itself a hundred times over.",
 "Früher mussten Mitglieder anrufen oder vorbeikommen, um einen Platz zu buchen. Heute läuft alles online – und die Abrechnung erledigt sich praktisch von selbst. Eine riesige Entlastung für den Vorstand."),
("Marvin McKinney", "Michael K."),
("Roofing Company Owner", "1. Vorsitzender, Tennisverein"),
("Our front desk was overwhelmed with appointment reminders and review requests. This system automated everything. Our show-up rate increased by 40% and our Google reviews doubled in two months.",
 "Die Einführung war unkompliziert und der Support hervorragend. Unsere Mitglieder haben die Online-Buchung sofort angenommen – die Auslastung unserer Plätze ist deutlich gestiegen."),
("Sarah Jenkins", "Sandra L."),
("Dental Practice Manager", "Geschäftsstellenleiterin"),
("I finally cancelled my subscription to 5 different tools. Having the Smart Inbox, calendar, and text campaigns in one dashboard saved me nearly $600 a month and made my life so much simpler.",
 "Endlich alle Tools in einem System. Wir haben mehrere Abos gekündigt, sparen jeden Monat Geld und der komplette Verwaltungsaufwand hat sich mehr als halbiert."),
("David Alaba", "Daniel B."),
("HVAC Contractor", "Anlagenbetreiber"),
]
miss=[]
for old,new in R:
    hit=False
    for v in (old, old.replace("'","&#39;"), old.replace("'","\u2019")):
        if v in s: s=s.replace(v,new); hit=True; break
    if not hit: miss.append(old[:50])

open(P,"w",encoding="utf-8").write(s)
print("Karten eingebaut. Misses:", miss if miss else "keine")

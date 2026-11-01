# -*- coding: utf-8 -*-
import re

P = "/Users/FJMarketing/Desktop/JKB-Website/pricing/index.html"
s = open(P, encoding="utf-8").read()

# --- Sektionen 1 (Pricing-Karten) und 2 (Plan-Matrix) durch Produkt-Übersicht ersetzen ---
parts = re.split(r'(?=<section)', s)
# parts[0] = Kopf bis main, danach je Sektion (letzter Teil enthält Footer)
sec_idx = [i for i, p in enumerate(parts) if p.startswith('<section')]
assert len(sec_idx) == 5, sec_idx

def card(name, desc, feats, price, cta, href, badge=""):
    f = "".join(f'<li class="flex items-start gap-x-3 mb-3"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="24" height="24" rx="6" fill="var(--color-primary)"></rect><path d="M11.18 15.69l6.52-6.86a1.1 1.1 0 0 0-1.6-1.51l-5.65 5.95-2.7-2.83a1.1 1.1 0 0 0-1.6 1.51l3.43 3.59c.2.21.46.31.72.31.26 0 .53-.1.73-.31z" fill="white"></path></svg><span class="text-sm">{x}</span></li>' for x in feats)
    b = f'<span class="absolute top-5 right-5 text-xs font-semibold px-3 py-1 rounded-full bg-primary text-white">{badge}</span>' if badge else ""
    return (f'<div class="py-10 px-7 rounded-3xl text-left relative bg-light/80 flex flex-col">{b}'
            f'<h3 class="text-h5 text-white font-semibold mb-2">{name}</h3>'
            f'<p class="text-text text-sm mb-6">{desc}</p>'
            f'<div class="text-white text-h4 font-semibold mb-6">{price}</div>'
            f'<ul class="mb-8">{f}</ul>'
            f'<a href="{href}" class="btn btn-primary w-full text-center mt-auto">{cta}</a></div>')

cards = (
 card("JKB Grounds", "Platzbuchung, Mitglieder &amp; Abrechnung für Vereine und Sportanlagen.",
      ["Online-Platz- &amp; Terminbuchung", "Mitglieder- &amp; Beitragsverwaltung", "SEPA-Lastschrift &amp; Rechnungen", "14 Tage kostenlos testen"],
      'ab <span class="text-primary">49&nbsp;€</span><span class="text-sm text-text"> / Monat</span>',
      "Preise ansehen", "/jkb-grounds-pricing.html", "Verfügbar") +
 card("JKB Hotels", "Zimmer, Gäste &amp; Rechnungen für Hotels und Pensionen – alles in einem System.",
      ["Zimmer- &amp; Buchungsverwaltung", "Gästeverwaltung &amp; Check-in", "Rechnungen &amp; Auswertungen"],
      '<span class="text-primary">Auf Anfrage</span>',
      "Jetzt informieren", "/contact", "Coming Soon") +
 card("JKB Cloud", "Sichere, DSGVO-konforme Cloud-Infrastruktur für Vereine und Unternehmen.",
      ["Sichere Cloud-Datenhaltung", "DSGVO-konform &amp; skalierbar", "Zugriff von überall"],
      '<span class="text-primary">Auf Anfrage</span>',
      "Jetzt informieren", "/contact", "Coming Soon") +
 card("JKB Office Custom", "Individualsoftware, exakt zugeschnitten auf Ihre Prozesse und Abläufe.",
      ["Maßgeschneiderte Entwicklung", "Anbindung bestehender Systeme", "Persönliche Betreuung"],
      '<span class="text-primary">Nach Aufwand</span>',
      "Projekt anfragen", "/contact")
)

new_section = ('<section class="section-box pt-0 my-0 bg-transparent" id="pricing"><div class="container">'
               '<div class="grid md:grid-cols-2 xl:grid-cols-4 gap-7">' + cards + '</div>'
               '<p class="text-center text-text text-sm mt-10">Alle Preise zzgl. MwSt. Jedes Produkt hat ein eigenes, faires Preismodell – Details erhalten Sie auf der jeweiligen Produktseite oder im persönlichen Gespräch.</p>'
               '</div></section>')

parts[sec_idx[1]] = new_section
parts[sec_idx[2]] = ""
s = "".join(parts)

# --- Hero & FAQ Texte ---
R = [
("Pricing Built For Local Business Growth", "Faire Preise – für jedes Produkt das passende Modell"),
("Start your free 14-day trial, scale as you grow. No contracts. Cancel anytime.",
 "Transparente Festpreise statt versteckter Kosten. Monatlich kündbar – und JKB Grounds testen Sie 14 Tage kostenlos."),
("Pricing - The All-In-One Growth Software", "Preise | JKB Software"),
("Quick Answers for the Smart Investors", "Häufig gestellte Fragen"),
("Find answers to common questions about our product and services.",
 "Antworten auf die wichtigsten Fragen zu unseren Preisen."),
("Is this software hard to set up?", "Gibt es eine Mindestvertragslaufzeit?"),
("Not at all. We built this platform specifically for local business owners who aren&#39;t tech experts. We provide templates and 1-on-1 support to get you running fast.",
 "Nein. Alle Abos sind monatlich kündbar. Bei individuellen Projekten vereinbaren wir den Rahmen gemeinsam im Angebot."),
("What if I already have a website?", "Was kostet die Einrichtung?"),
("You can keep your existing website! Our tools (like the Web Chat Widget and Missed Call Text-Back) easily integrate with WordPress, Wix, and Squarespace with a simple line of code.",
 "Die Standardeinrichtung inklusive Datenübernahme und Schulung ist bei unseren Produkten im Preis enthalten."),
("Can this replace my existing CRM or Mailchimp?", "Warum stehen nicht überall feste Preise?"),
("Yes. Our platform includes a full CRM, unlimited email marketing, and SMS capabilities. Most of our clients cancel 3-5 other software subscriptions when they switch to us.",
 "Unsere Produkte unterscheiden sich stark je nach Branche und Umfang. JKB Grounds hat feste Pakete – bei Hotels, Cloud und Individualprojekten erstellen wir Ihnen ein passgenaues Angebot."),
("How does the Missed Call Auto-Responder work?", "Kann ich JKB Grounds vorher testen?"),
("When a customer calls your business number and you don&#39;t answer, the system instantly texts them back (e.g., &#39;Sorry we missed your call! How can we help you?&#39;). This stops leads from calling your competitors.",
 "Ja – JKB Grounds testen Sie 14 Tage kostenlos und unverbindlich. Erst danach entscheiden Sie sich für ein Paket."),
("Are there any hidden fees?", "Gibt es versteckte Kosten?"),
("No hidden fees. You pay a simple flat monthly rate. You may just pay fractional cents directly to telecom providers for your SMS usage, exactly what it costs.",
 "Nein. Sie zahlen einen transparenten monatlichen Festpreis – ohne versteckte Gebühren."),
]
miss=[]
for old,new in R:
    for v in (old, old.replace("&#39;","'"), old.replace("&#39;","\u2019")):
        if v in s:
            s=s.replace(v,new); break
    else:
        miss.append(old[:50])

open(P,"w",encoding="utf-8").write(s)
print("Sektionen ersetzt. Text-Misses:", miss if miss else "keine")

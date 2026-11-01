# -*- coding: utf-8 -*-
P = "/Users/FJMarketing/Desktop/JKB-Website/index.html"
html = open(P, encoding="utf-8").read()

R = [
# ===== HERO: Unternehmen statt Produkt =====
("Die All-in-One Verwaltungssoftware für", "Ihr Softwarepartner für"),
("Vereine, Hotels &amp; Unternehmen</", "digitale Lösungen in jeder Branche</"),
("Schluss mit manuellem Verwaltungschaos: Buchungen, Mitglieder, Abrechnung und Kommunikation – alles automatisiert in einer Plattform.",
 "JKB Software entwickelt moderne Verwaltungs- und Buchungslösungen für Vereine, Hotellerie und Unternehmen – individuell, zuverlässig und aus einer Hand."),
("14 Tage kostenlos testen", "Unsere Produkte entdecken"),
("Demo vereinbaren", "Kontakt aufnehmen"),

# ===== PROBLEM-SEKTION =====
("Verlieren Sie wertvolle Zeit durch", "Digitalisierung scheitert oft an"),
("manuelle Verwaltung?", "den falschen Tools"),
("Zettelwirtschaft, Excel-Listen und verstreute Tools kosten Sie jede Woche Stunden. Unser System erledigt die Verwaltung automatisch.",
 "Egal ob Verein, Hotel oder Betrieb: Insellösungen, Zettelwirtschaft und veraltete Software kosten Zeit, Geld und Nerven. Wir ändern das."),

# ===== LÖSUNG: Produktportfolio =====
("Ersetzen Sie Ihre Einzeltools durch ein", "Ein Unternehmen,"),
("smartes All-in-One-System", "vier starke Lösungen"),
("Ein zentrales Dashboard für Buchungen, Mitglieder, Abrechnung und Kommunikation.",
 "Für jede Branche die passende Software – entwickelt und betreut von JKB Software."),
# Karte 1 -> JKB Grounds
("Automatisierte Buchungsverwaltung", "JKB Grounds – Vereine &amp; Sportanlagen"),
("24/7 Buchungen rund um die Uhr", "Mitglieder- &amp; Beitragsverwaltung"),
("Automatische E-Mail-Bestätigungen", "Automatische Abrechnung per SEPA"),
# Karte 2 -> JKB Hotels
("Smarte Mitgliederverwaltung", "JKB Hotels – Hotellerie &amp; Pensionen"),
("Zentrale Mitgliederdatenbank", "Zimmer- &amp; Buchungsverwaltung"),
("Beitrags- &amp; Rechnungsverwaltung", "Gästeverwaltung &amp; Check-in"),
("Notizen &amp; Buchungshistorie", "Rechnungen &amp; Auswertungen"),
# Karte 3 -> JKB Cloud
("Automatische Abrechnung", "JKB Cloud – Daten &amp; Infrastruktur"),
("SEPA-Lastschrift &amp; Rechnungen", "Sichere Cloud-Datenhaltung"),
("Automatische Zahlungserinnerungen", "DSGVO-konform &amp; skalierbar"),
("Transparente Finanzübersicht", "Zugriff von überall"),
# Karte 4 -> JKB Office Custom
("Digitale Kommunikation", "JKB Office Custom – Individualsoftware"),
("News &amp; Mitteilungen an Mitglieder", "Maßgeschneiderte Entwicklung"),
("Anfrage- &amp; Kontaktformulare", "Anbindung bestehender Systeme"),
("Automatische Benachrichtigungen", "Persönliche Betreuung"),

# ===== AUTOPILOT-SEKTION =====
("Alles, was Sie brauchen, um Ihre Verwaltung auf", "Software, die Ihnen die Arbeit abnimmt –"),
("Autopilot zu stellen<", "nicht umgekehrt<"),
("Von der ersten Buchung bis zur fertigen Abrechnung – JKB Software übernimmt.",
 "Alle unsere Produkte folgen einem Prinzip: maximale Automatisierung, minimale Einarbeitung."),

# ===== 5 DINGE -> BRANCHEN =====
("Die 5 Dinge, die jeder", "Die Branchen, in denen"),
("Verein &amp; Betrieb braucht", "wir zuhause sind"),
(">BUCHUNG<", ">SPORT &amp; VEREINE<"),
("Plätze, Räume und Termine werden online gebucht – rund um die Uhr, ohne Telefonate und Zettelwirtschaft.",
 "Mit JKB Grounds digitalisieren Tennis-, Sport- und Freizeitanlagen ihre komplette Platz- und Mitgliederverwaltung."),
(">VERWALTUNG<", ">HOTELLERIE<"),
("Alle Mitglieder- und Kundendaten zentral an einem Ort – immer aktuell und sofort auffindbar.",
 "JKB Hotels bringt Buchungen, Gästeverwaltung und Abrechnung für Hotels und Pensionen in ein System."),
(">ABRECHNUNG<", ">CLOUD &amp; IT<"),
("Beiträge und Gebühren werden automatisch berechnet und per SEPA-Lastschrift eingezogen.",
 "Mit JKB Cloud erhalten Vereine und Unternehmen eine sichere, DSGVO-konforme Infrastruktur für ihre Daten."),
(">KOMMUNIKATION<", ">BÜRO &amp; VERWALTUNG<"),
("Bestätigungen, Erinnerungen und News erreichen Ihre Mitglieder automatisch per E-Mail.",
 "JKB Office Custom digitalisiert Büro- und Verwaltungsprozesse – exakt zugeschnitten auf Ihre Abläufe."),
(">AUSWERTUNG<", ">INDIVIDUALPROJEKTE<"),
("Auslastung, Einnahmen und Entwicklung – alle wichtigen Kennzahlen auf einen Blick.",
 "Ihre Branche ist nicht dabei? Wir entwickeln individuelle Lösungen – sprechen Sie uns einfach an."),

# ===== 3 SCHRITTE =====
("In 3 Schritten zur", "In 3 Schritten zu Ihrer"),
("automatisierten Verwaltung", "digitalen Lösung"),
("1. Kostenlos testen", "1. Kennenlernen"),
("Registrieren Sie sich und testen Sie JKB Software 14 Tage unverbindlich.",
 "In einem unverbindlichen Gespräch finden wir heraus, wo Sie stehen und was Sie brauchen."),
("2. Daten verbinden", "2. Lösung finden"),
("Mitglieder importieren, Plätze und Preise anlegen – in wenigen Klicks startklar.",
 "Ob fertiges Produkt oder Individualentwicklung – wir empfehlen die Lösung, die wirklich passt."),
("3. Automatisch verwalten", "3. Durchstarten"),
("Buchungen, Abrechnung und Kommunikation laufen von allein – Sie konzentrieren sich aufs Wesentliche.",
 "Wir richten alles ein, schulen Ihr Team und bleiben auch danach Ihr persönlicher Ansprechpartner."),
("Jetzt 14 Tage kostenlos testen", "Jetzt Kontakt aufnehmen"),

# ===== TRUST =====
("und Betriebe verwalten ihre Buchungen und Mitglieder automatisch mit JKB Software.",
 ", Hotels und Betriebe vertrauen bei ihrer Digitalisierung auf JKB Software."),
("Sie haben Ihren Verein oder Betrieb nicht gegründet, um",
 "Sie haben Ihr Unternehmen nicht gegründet, um"),

# ===== CTA unten =====
("Bereit, Ihre Verwaltung auf", "Bereit für die"),
("Autopilot zu stellen?", "Digitalisierung mit JKB Software?"),
("Schluss mit verstreuten Tools und manueller Arbeit – starten Sie jetzt mit JKB Software in die digitale Verwaltung.",
 "Lassen Sie uns gemeinsam herausfinden, welche Lösung zu Ihnen passt – unverbindlich und persönlich."),
]

missed = []
for old, new in R:
    found = False
    for v in (old, old.replace("&amp;", "&")):
        if v in html:
            html = html.replace(v, new)
            found = True
            break
    if not found:
        missed.append(old[:60])

open(P, "w", encoding="utf-8").write(html)
print("ersetzt:", len(R)-len(missed), "/", len(R))
for m in missed: print("NICHT GEFUNDEN:", m)

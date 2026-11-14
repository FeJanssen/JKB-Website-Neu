# -*- coding: utf-8 -*-
P = "/Users/FJMarketing/Desktop/JKB-Website/index.html"
html = open(P, encoding="utf-8").read()

R = [
# Titel
("<title>\n      Automark\n\n    </title>", "<title>JKB Software – Digitale Verwaltung für Vereine, Hotels & Unternehmen</title>"),
# Pricing-Überschrift
("Affordable <strong>", "Faire <strong>"),
# Folgefehler aus erster Runde
("Zentrale Mitgliederdatenbank &amp; Reviews", "Mitgliederverwaltung &amp; Abrechnung"),
("Digitale Kommunikation &amp; Funnels", "SEPA-Lastschrift &amp; Rechnungen"),
("Online-Platz- &amp; Terminbuchung work?", "Wie funktioniert die automatische Abrechnung?"),
# Zitat (straight quotes + &#39;)
('"Before this system, I was losing half my leads simply because I couldn&#39;t get to my phone fast enough while on jobs. Now, the system handles the follow-up for me, and I&#39;ve seen a 300% jump in bookings."',
 '\u201eFrüher haben wir Stunden mit Platzbelegungslisten und Beitragsrechnungen verbracht. Heute läuft das alles automatisch über JKB Grounds – und wir haben endlich wieder Zeit für den Sport.\u201c'),
("We used to lose at least 3-4 jobs a week because we couldn&#39;t answer the phone while on a roof. The Missed Call Auto-Responder immediately cut that to zero. This software pays for itself a hundred times over.",
 "Früher mussten Mitglieder anrufen oder vorbeikommen, um einen Platz zu buchen. Heute läuft alles online – und die Abrechnung erledigt sich praktisch von selbst. Eine riesige Entlastung für den Vorstand."),
]

missed = []
for old, new in R:
    if old in html:
        html = html.replace(old, new)
    else:
        missed.append(old[:60])

open(P, "w", encoding="utf-8").write(html)
print("ersetzt:", len(R)-len(missed), "/", len(R))
for m in missed: print("NICHT GEFUNDEN:", m)

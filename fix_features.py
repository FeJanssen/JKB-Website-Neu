# -*- coding: utf-8 -*-
P = "/Users/FJMarketing/Desktop/JKB-Website/features/index.html"
html = open(P, encoding="utf-8").read()

R = [
# ===== META / NAV =====
("Features - The All-In-One Growth Software", "Warum JKB Software – Ihr Partner für Digitalisierung"),
(">Case Studies<", ">Referenzen<"),
(">Contact<", ">Kontakt<"),
(">Get This Template<", ">Kostenlos testen<"),

# ===== HERO =====
("Features That Turn", "Stärken, die aus Aufwand"),
(">Attention<", ">Effizienz<"),
("Into Revenue", "machen"),
("A single piece of software built to manage your entire business on autopilot. Say goodbye to scattered tools and forgotten leads.",
 "JKB Software steht für durchdachte digitale Lösungen, persönliche Betreuung und Technologie, die einfach funktioniert – branchenübergreifend und aus einer Hand."),
("Start Free Trial", "Kontakt aufnehmen"),
("Book a Demo", "Produkte entdecken"),

# ===== TRUST =====
("Trusted by", "Bereits"),
(">10,000+<", ">viele Vereine<"),
("local businesses to scale their bookings and growth automatically.",
 ", Hotels und Betriebe vertrauen bei ihrer Digitalisierung auf JKB Software."),

# ===== BLOCK 1 =====
("Automate every part of your", "Was uns als Unternehmen"),
("business with", "auszeichnet –"),
("one smart platform.", "in jeder Branche."),
("Automated Customer Follow-Up", "Alles aus einer Hand"),
("Never lose a lead again. Respond to inquiries instantly and automatically.",
 "Von der Beratung über die Entwicklung bis zum laufenden Betrieb – Sie haben einen Partner für alles."),
("Autopilot Review Generator", "Branchenübergreifende Erfahrung"),
("Automatically request and track 5-star Google reviews from happy clients.",
 "Vereine, Hotellerie, Büro und Cloud – wir kennen die Anforderungen unterschiedlichster Branchen."),
("Missed Call Auto-Responder", "Persönlicher Support"),
("Turn missed calls into booked appointments with instant automated text messages.",
 "Kein anonymes Ticketsystem: Bei uns sprechen Sie direkt mit den Menschen, die Ihre Software kennen."),
("Unified Lead Inbox", "Faire &amp; transparente Preise"),
("Manage all your SMS, email, Facebook, and Instagram messages in one single dashboard.",
 "Klare monatliche Festpreise ohne versteckte Kosten – jederzeit kündbar."),
("24/7 Appointment Scheduler", "Entwicklung aus Deutschland"),
("Let customers book directly on your calendar, completely eliminating back-and-forth emails.",
 "Unsere Lösungen werden in Deutschland entwickelt und betrieben – DSGVO-konform und zuverlässig."),

# ===== BLOCK 2 =====
("Built specifically to grow", "Gebaut für Menschen,"),
("your local business", "nicht für IT-Profis"),
("Setup in Minutes", "Schnelle Einführung"),
("Get up and running immediately with our pre-built local business templates.",
 "Wir richten alles für Sie ein und schulen Ihr Team – Sie sind in kürzester Zeit startklar."),
("Automated Intelligence", "Intelligente Automatisierung"),
("Smart workflows that automatically sort, nurture and follow up with your leads.",
 "Wiederkehrende Aufgaben laufen automatisch im Hintergrund – Sie konzentrieren sich aufs Wesentliche."),
("Secure & Reliable", "Sicher &amp; zuverlässig"),
("Your client database and payment info is protected with bank-level encryption.",
 "Ihre Daten werden verschlüsselt und DSGVO-konform in der Cloud gespeichert."),
("All Tools In One Place", "Alles an einem Ort"),
("Replace your CRM, website builder, calendar, and email marketing software.",
 "Ein System statt fünf Einzeltools – weniger Kosten, weniger Aufwand, mehr Übersicht."),

# ===== BLOCK 3 =====
("The only software you need to", "Ein Partner, mit dem Sie"),
("scale predictably", "planbar wachsen"),
("Clear ROI Tracking", "Klare Auswertungen"),
("See exactly which campaigns and ads are generating the most revenue.",
 "Behalten Sie Auslastung, Einnahmen und Entwicklung jederzeit im Blick."),
("Easy to Use", "Einfache Bedienung"),
("Designed for business owners, not IT professionals. Simple and intuitive.",
 "Entwickelt für Anwender, nicht für IT-Profis. Intuitiv und ohne Schulungsaufwand nutzbar."),
("Complete Client History", "Lückenlose Historie"),
("View every text, email, and phone call with a client in a single chronological feed.",
 "Alle Buchungen, Zahlungen und Nachrichten chronologisch an einem Ort."),
("Mobile App Access", "Von überall erreichbar"),
("Manage leads, reply to messages, and run your business from anywhere using our mobile app.",
 "Ob im Büro, auf der Anlage oder unterwegs – Sie greifen von jedem Gerät auf Ihre Daten zu."),

# ===== 5 DINGE -> Branchen =====
("The 5 things every", "Die Branchen, in denen"),
("Business Needs", "wir zuhause sind"),
(">TRAFFIC<", ">SPORT &amp; VEREINE<"),
("Drive more high-quality local leads to your business through optimized Google search and social visibility.",
 "Mit JKB Grounds digitalisieren Tennis-, Sport- und Freizeitanlagen ihre komplette Platz- und Mitgliederverwaltung."),
(">CAPTURE<", ">HOTELLERIE<"),
("Convert website visitors into real conversations using web chat widgets and fast lead capture forms.",
 "JKB Hotels bringt Buchungen, Gästeverwaltung und Abrechnung für Hotels und Pensionen in ein System."),
(">NURTURING<", ">CLOUD &amp; IT<"),
("Automatically follow up with every lead via SMS and email so no one slips through the cracks.",
 "Mit JKB Cloud erhalten Vereine und Unternehmen eine sichere, DSGVO-konforme Infrastruktur für ihre Daten."),
(">CONVERT<", ">BÜRO &amp; VERWALTUNG<"),
("Turn prospects into paying customers by making appointment booking and payments incredibly simple.",
 "JKB Office Custom digitalisiert Büro- und Verwaltungsprozesse – exakt zugeschnitten auf Ihre Abläufe."),
(">REFER<", ">INDIVIDUALPROJEKTE<"),
("Automatically request 5-star Google reviews from happy customers to drive even more organic traffic.",
 "Ihre Branche ist nicht dabei? Wir entwickeln individuelle Lösungen – sprechen Sie uns einfach an."),

# ===== USED TO BE DIFFICULT =====
("But It Used To Be", "Bisher war das"),
(">Difficult<", ">kompliziert<"),
("Social Media Platforms", "Buchungssysteme"),
("Email Marketing Tools", "E-Mail-Tools"),
("CRM Software", "Mitgliederverwaltung"),
("Ad Platforms", "Abrechnungssoftware"),
("Scheduling Tools", "Kalender-Tools"),
("Analytics Platforms", "Auswertungs-Tools"),
("Automation Tools", "Automatisierungs-Tools"),
("Project Management", "Projektverwaltung"),
("Payment Gateways", "Zahlungsanbieter"),
("Customer Support", "Support-Software"),
("/Per Month", "/pro Monat"),

# ===== FAQ =====
("Quick Answers for the Smart Investors", "Häufig gestellte Fragen"),
("Find answers to common questions about our product and services.",
 "Antworten auf die wichtigsten Fragen zu JKB Software."),
("Is this software hard to set up?", "Ist die Einrichtung kompliziert?"),
("Not at all. We built this platform specifically for local business owners who aren't tech experts. We provide templates and 1-on-1 support to get you running fast.",
 "Überhaupt nicht. Unsere Lösungen wurden für Anwender ohne IT-Kenntnisse entwickelt. Wir begleiten Sie persönlich bei der Einrichtung."),
("What if I already have a website?", "Was ist, wenn wir schon eine Website haben?"),
("You can keep your existing website! Our tools (like the Web Chat Widget and Missed Call Text-Back) easily integrate with WordPress, Wix, and Squarespace with a simple line of code.",
 "Kein Problem – Ihre bestehende Website bleibt bestehen. Unsere Systeme lassen sich einfach verlinken oder einbinden."),
("Can this replace my existing CRM or Mailchimp?", "Ersetzt JKB Software unsere bisherigen Tools?"),
("Yes. Our platform includes a full CRM, unlimited email marketing, and SMS capabilities. Most of our clients cancel 3-5 other software subscriptions when they switch to us.",
 "Ja. Unsere Plattformen bündeln Buchung, Verwaltung, Abrechnung und Kommunikation. Die meisten Kunden kündigen nach dem Wechsel mehrere andere Software-Abos."),
("How does the Missed Call Auto-Responder work?", "Für welche Branchen ist JKB Software geeignet?"),
("When a customer calls your business number and you don't answer, the system instantly texts them back (e.g., 'Sorry we missed your call! How can we help you?'). This stops leads from calling your competitors.",
 "Wir sind spezialisiert auf Vereine und Sportanlagen, Hotellerie sowie Büro- und Verwaltungsprozesse. Darüber hinaus entwickeln wir individuelle Lösungen für nahezu jede Branche."),
("Are there any hidden fees?", "Gibt es versteckte Kosten?"),
("No hidden fees. You pay a simple flat monthly rate. You may just pay fractional cents directly to telecom providers for your SMS usage, exactly what it costs.",
 "Nein. Sie zahlen einen transparenten monatlichen Festpreis – ohne versteckte Gebühren. Jederzeit kündbar."),

# ===== CTA / FOOTER =====
("Ready to put Your Local Business Growth on", "Bereit für die"),
(">Autopilot?<", ">Digitalisierung mit JKB Software?<"),
("Stop wasting thousands on scattered tools that don't convert and start enjoying streamlined, predictable growth.",
 "Lassen Sie uns gemeinsam herausfinden, welche Lösung zu Ihnen passt – unverbindlich und persönlich."),
("Start Your 14-Days Free Trial", "Jetzt Kontakt aufnehmen"),
("Empowering Marketing businesses through intelligent automation.",
 "Intelligente Verwaltungssoftware für Vereine, Hotels und Unternehmen."),
("contact@Automark.com", "info@jkb-software.com"),
("(+1) 165-320-0102", ""),
(">Primary<", ">Navigation<"),
(">Home<", ">Startseite<"),
(">About Us<", ">Über uns<"),
(">Resource<", ">Ressourcen<"),
(">Legal<", ">Rechtliches<"),
(">Privacy Policy<", ">Datenschutz<"),
(">Terms and Conditions<", ">AGB<"),
(">Themefisher<", ">JKB Software<"),
("All Rights Reserved", "Alle Rechte vorbehalten"),
]

def variants(s):
    out=[s]
    if "&amp;" in s: out.append(s.replace("&amp;","&"))
    elif "&" in s: out.append(s.replace("&","&amp;"))
    if "'" in s:
        out += [v.replace("'","&#39;") for v in list(out)]
        out += [v.replace("'","\u2019") for v in [s]]
    return out

missed=[]
for old,new in R:
    ok=False
    for v in variants(old):
        if v in html:
            html=html.replace(v,new); ok=True; break
    if not ok: missed.append(old[:60])

open(P,"w",encoding="utf-8").write(html)
print("ersetzt:", len(R)-len(missed), "/", len(R))
for m in missed: print("NICHT GEFUNDEN:", m)

# -*- coding: utf-8 -*-
import re

P = "/Users/FJMarketing/Desktop/JKB-Website/index.html"
html = open(P, encoding="utf-8").read()

R = [
# ===== HERO =====
("The All-In-One Growth Software for", "Die All-in-One Verwaltungssoftware für"),
("Local Business Owners", "Vereine, Hotels &amp; Unternehmen"),
("The complete automated system designed to capture more leads, follow up instantly, and grow your local business - all in one place.",
 "Schluss mit manuellem Verwaltungschaos: Buchungen, Mitglieder, Abrechnung und Kommunikation – alles automatisiert in einer Plattform."),
("Start Your 14-day Free Trial", "14 Tage kostenlos testen"),
("Book a Demo", "Demo vereinbaren"),

# ===== PROBLEM SECTION =====
("Are you losing real customers to the", "Verlieren Sie wertvolle Zeit durch"),
("Follow-up Gap?", "manuelle Verwaltung?"),
("Stop wasting money on marketing if you can't respond fast enough. Our system ensures every lead gets immediate attention.",
 "Zettelwirtschaft, Excel-Listen und verstreute Tools kosten Sie jede Woche Stunden. Unser System erledigt die Verwaltung automatisch."),
("Wasted Ad Spend", "Verschwendete Arbeitszeit"),
("Expensive 'Franken-stack' of tools", "Teurer Flickenteppich aus Einzeltools"),
("Scattered Customer Data", "Verstreute Mitglieder- und Kundendaten"),
("Missed Calls Costing Thousands", "Verpasste Buchungen kosten Umsatz"),
("Lost Leads to Competitors", "Verlorene Anfragen an die Konkurrenz"),
("Slow Response Times", "Langsame Reaktionszeiten"),

# ===== SOLUTION / FEATURES =====
("Replace Your Clunky Tools With A", "Ersetzen Sie Ihre Einzeltools durch ein"),
("Smart, All-In-One System", "smartes All-in-One-System"),
("Log in to a single powerful dashboard to manage everything seamlessly.",
 "Ein zentrales Dashboard für Buchungen, Mitglieder, Abrechnung und Kommunikation."),
("Automated Customer Follow-Up", "Automatisierte Buchungsverwaltung"),
("Missed Call Auto-Responder", "Online-Platz- &amp; Terminbuchung"),
("24/7 Appointment Scheduler", "24/7 Buchungen rund um die Uhr"),
("Instant SMS & Email Follow-Up", "Automatische E-Mail-Bestätigungen"),
("Smart Customer Database", "Smarte Mitgliederverwaltung"),
("Unified Lead Inbox", "Zentrale Mitgliederdatenbank"),
("Smart Pipeline Manager", "Beitrags- &amp; Rechnungsverwaltung"),
("Client Notes & History", "Notizen &amp; Buchungshistorie"),
("Autopilot Review Generator", "Automatische Abrechnung"),
("Automated Review Requests", "SEPA-Lastschrift &amp; Rechnungen"),
("Google & Facebook Integration", "Automatische Zahlungserinnerungen"),
("Reputation Tracking", "Transparente Finanzübersicht"),
("High-Converting Websites", "Digitale Kommunikation"),
("Drag-and-Drop Landing Pages", "News &amp; Mitteilungen an Mitglieder"),
("Lead Capture Forms", "Anfrage- &amp; Kontaktformulare"),
("Web Chat Widgets", "Automatische Benachrichtigungen"),

# ===== AUTOPILOT SECTION =====
("Everything You Need To Put Growth On", "Alles, was Sie brauchen, um Ihre Verwaltung auf"),
(">Autopilot<", ">Autopilot zu stellen<"),
("From capturing the very first click to securing a 5-star review, we've got you covered.",
 "Von der ersten Buchung bis zur fertigen Abrechnung – JKB Software übernimmt."),
("Automated Customer Follow-up", "Automatisierte Buchungsabläufe"),
("Visualize how teams are staffed & what resources are available across.",
 "Behalten Sie Plätze, Räume und Ressourcen jederzeit im Blick."),
("Drag & Drop Forms", "Flexible Buchungskalender"),
("Automated Text Campaigns", "Automatische Mitglieder-Kommunikation"),

# ===== 5 THINGS =====
("The 5 things every", "Die 5 Dinge, die jeder"),
("Business Needs", "Verein &amp; Betrieb braucht"),
(">TRAFFIC<", ">BUCHUNG<"),
("Drive more high-quality local leads to your business through optimized Google search and social visibility.",
 "Plätze, Räume und Termine werden online gebucht – rund um die Uhr, ohne Telefonate und Zettelwirtschaft."),
(">CAPTURE<", ">VERWALTUNG<"),
("Convert website visitors into real conversations using web chat widgets and fast lead capture forms.",
 "Alle Mitglieder- und Kundendaten zentral an einem Ort – immer aktuell und sofort auffindbar."),
(">NURTURING<", ">ABRECHNUNG<"),
("Automatically follow up with every lead via SMS and email so no one slips through the cracks.",
 "Beiträge und Gebühren werden automatisch berechnet und per SEPA-Lastschrift eingezogen."),
(">CONVERT<", ">KOMMUNIKATION<"),
("Turn prospects into paying customers by making appointment booking and payments incredibly simple.",
 "Bestätigungen, Erinnerungen und News erreichen Ihre Mitglieder automatisch per E-Mail."),
(">REFER<", ">AUSWERTUNG<"),
("Automatically request 5-star Google reviews from happy customers to drive even more organic traffic.",
 "Auslastung, Einnahmen und Entwicklung – alle wichtigen Kennzahlen auf einen Blick."),

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
("We know you didn't start your local business to become a full-time",
 "Sie haben Ihren Verein oder Betrieb nicht gegründet, um"),
(">Software Engineer<", ">Software-Administrator zu werden<"),
("\u201cBefore this system, I was losing half my leads simply because I couldn't get to my phone fast enough while on jobs. Now, the system handles the follow-up for me, and I've seen a 300% jump in bookings.\u201d",
 "\u201eFrüher haben wir Stunden mit Platzbelegungslisten und Beitragsrechnungen verbracht. Heute läuft das alles automatisch über JKB Grounds – und wir haben endlich wieder Zeit für den Sport.\u201c"),

# ===== TRUST / STATS =====
("Trusted by", "Bereits"),
(">10,000+<", ">viele Vereine<"),
("local businesses to scale their bookings and growth automatically.",
 "und Betriebe verwalten ihre Buchungen und Mitglieder automatisch mit JKB Software."),
("Lead Captured", "Buchungen digital"),
("5x Faster", "5x schneller"),
("Response Time", "Verwaltungsabläufe"),
("28hr/week", "10+ Std./Woche"),
("Hours Saved", "Zeitersparnis"),
("This all-in-one software is exactly what our local business needed. It completely eliminated our need for 4 other separate platforms and organized our entire customer pipeline.",
 "Genau die Lösung, die unser Verein gebraucht hat. Wir konnten mehrere Einzeltools abschaffen und haben jetzt alles – von der Platzbuchung bis zur Abrechnung – in einem System."),
("Ronald Richards", "Thomas R."),
("Local Services Co.", "Tennisclub-Vorstand"),

# ===== 3 STEPS =====
("Your 3-Step Path to", "In 3 Schritten zur"),
("Automated Growth", "automatisierten Verwaltung"),
("1. Start Your Trial", "1. Kostenlos testen"),
("Sign up for a free trial and experience the power of the platform for yourself. No credit card required.",
 "Registrieren Sie sich und testen Sie JKB Software 14 Tage unverbindlich."),
("2. Connect Your Business", "2. Daten verbinden"),
("Forward your calls, plug in your social accounts, and unify your inbox in a matter of clicks.",
 "Mitglieder importieren, Plätze und Preise anlegen – in wenigen Klicks startklar."),
("3. Scale on Autopilot", "3. Automatisch verwalten"),
("Watch your calendar fill up and reviews come in automatically, so you can focus on serving your customers.",
 "Buchungen, Abrechnung und Kommunikation laufen von allein – Sie konzentrieren sich aufs Wesentliche."),
("Start Your 14-Day Free Trial", "Jetzt 14 Tage kostenlos testen"),

# ===== CEO LETTER =====
("Why We Do What We Do - A Letter From", "Warum wir tun, was wir tun – ein Brief von"),
("Our CEO", "unserem Gründer"),
("Founder & CEO", "Gründer &amp; Geschäftsführer"),
("At Automark, we know you started your local business to serve your community, not to become a software engineer.",
 "Bei JKB Software wissen wir: Sie engagieren sich für Ihren Verein oder Ihr Unternehmen – nicht, um Software-Experte zu werden."),
("The problem is most modern marketing tools are too complex, scattered, and disconnected, which leaves you feeling overwhelmed and stuck in the daily admin grind.",
 "Das Problem: Die meisten Verwaltungstools sind zu komplex, verstreut und nicht miteinander verbunden. Das Ergebnis ist täglicher Verwaltungsaufwand, der Zeit und Nerven kostet."),
("We believe you shouldn't have to pay for five different subscriptions or spend your weekends sending emails just to grow your company. We understand how frustrating it is to watch hard-earned leads slip through the cracks, which is why we built a single, unified platform that puts your follow-ups, reviews, and bookings on complete autopilot.",
 "Wir finden: Sie sollten nicht fünf verschiedene Abos bezahlen oder Ihre Wochenenden mit Excel-Listen verbringen müssen. Deshalb haben wir eine einzige, zentrale Plattform gebaut, die Buchungen, Abrechnung und Kommunikation komplett automatisiert."),
("Here's how we do it:", "So funktioniert es:"),
("1. Plug In Your Business Data", "1. Daten anbinden"),
("2. Activate Our Local Workflows", "2. Abläufe aktivieren"),
("3. Watch Your Bookings Grow", "3. Verwaltung läuft automatisch"),
("Stop wasting money on scattered tools that don't talk to each other, and instead enjoy a streamlined business with consistent, predictable revenue growth.",
 "Schluss mit verstreuten Tools, die nicht miteinander sprechen – freuen Sie sich auf reibungslose Abläufe und volle Übersicht."),

# ===== INTEGRATIONS / RESOURCE =====
("Connect all your", "Verbinden Sie alle Ihre"),
(">Applications<", ">Anwendungen<"),
("Free Resource for", "Kostenloser Leitfaden für"),
("The \"Leaking Bucket\" Audit: 5 Ways You're Losing Local Leads (And How to Fix Them).",
 "Der Verwaltungs-Check: 5 Zeitfresser in Ihrer Vereins- und Betriebsverwaltung (und wie Sie sie beseitigen)."),
("Did you know that most small businesses lose up to 50% of their potential sales simply because of slow follow-up?",
 "Wussten Sie, dass die meisten Vereine und Betriebe über 10 Stunden pro Woche durch manuelle Verwaltung verlieren?"),
("Download our", "Laden Sie unsere"),
(">FREE<", ">KOSTENLOSE<"),
("Checklist to identify the \"lead leaks\" in your current business and learn how to plug them with simple software automation.",
 "Checkliste herunter und finden Sie heraus, wo Sie in Ihrer Verwaltung Zeit verlieren – und wie einfache Automatisierung hilft."),
("The Follow-Up Audit:", "Der Verwaltungs-Check:"),
("A step-by-step guide to measuring your lead response time.",
 "Schritt für Schritt analysieren, wo Ihre Zeit verloren geht."),
("Automation Quick-Wins:", "Automatisierungs-Quick-Wins:"),
("3 workflows you can set up today to start booking more local appointments.",
 "3 Abläufe, die Sie noch heute automatisieren können."),
("The Tech Stack Check:", "Der Tool-Check:"),
("Stop paying for 5 different software tools.",
 "Schluss mit 5 verschiedenen Software-Abos."),
("Get Free Checklist", "Kostenlose Checkliste anfordern"),
("Submitting...", "Wird gesendet..."),
("✅ Free Checklist requested successfully!", "✅ Checkliste erfolgreich angefordert!"),
("Something went wrong.", "Etwas ist schiefgelaufen."),

# ===== PRICING =====
(">Affordable<", ">Faire<"),
("Pricing Plans", "Preispakete"),
("Choose the plan that fits your local business and start growing automatically.",
 "Wählen Sie das Paket, das zu Ihrem Verein oder Betrieb passt – und starten Sie direkt durch."),
(">Monthly<", ">Monatlich<"),
(">Yearly<", ">Jährlich<"),
(">Essentials<", ">Starter<"),
("The core necessities for organizing your leads and capturing more business.",
 "Die Grundausstattung für digitale Buchungen und Mitgliederverwaltung."),
("Start Free Trial", "Kostenlos testen"),
("Features Included", "Enthaltene Funktionen"),
("Automatically text back missed calls.", "Online-Buchung für Plätze &amp; Termine."),
("Automated Follow-Up Campaigns", "Automatische Buchungsbestätigungen"),
("Most Popular", "Beliebtestes Paket"),
(">Growth<", ">Professional<"),
("Everything you need to put your business growth on complete autopilot.",
 "Alles, was Sie brauchen, um Ihre komplette Verwaltung zu automatisieren."),
("Unified Lead Inbox & Reviews", "Mitgliederverwaltung &amp; Abrechnung"),
("Unlimited calendars and bookings.", "Unbegrenzte Kalender und Buchungen."),
("High-Converting Websites & Funnels", "SEPA-Lastschrift &amp; Rechnungen"),
("Advanced API Integrations", "Erweiterte Schnittstellen"),
(">Scale<", ">Enterprise<"),
("Total control and advanced tools to scale multiple locations seamlessly.",
 "Volle Kontrolle und erweiterte Funktionen für mehrere Standorte und Anlagen."),
("Everything in Growth", "Alles aus Professional"),
("Unlimited Social Media Posting", "Mehrere Anlagen &amp; Standorte"),
("Schedule content across all platforms.", "Zentrale Verwaltung aller Standorte."),
("Multi-Location Support", "Individuelle Anpassungen"),
("Dedicated Account Manager", "Persönlicher Ansprechpartner"),

# ===== TESTIMONIALS =====
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

# ===== FAQ =====
("Quick Answers for the Smart Investors", "Häufig gestellte Fragen"),
("Find answers to common questions about our product and services.",
 "Antworten auf die wichtigsten Fragen zu JKB Software."),
("Is this software hard to set up?", "Ist die Einrichtung kompliziert?"),
("Not at all. We built this platform specifically for local business owners who aren't tech experts. We provide templates and 1-on-1 support to get you running fast.",
 "Überhaupt nicht. JKB Software wurde speziell für Vereine und Betriebe entwickelt, die keine Technik-Experten sind. Wir begleiten Sie persönlich bei der Einrichtung."),
("What if I already have a website?", "Was ist, wenn wir schon eine Website haben?"),
("You can keep your existing website! Our tools (like the Web Chat Widget and Missed Call Text-Back) easily integrate with WordPress, Wix, and Squarespace with a simple line of code.",
 "Kein Problem – Ihre bestehende Website bleibt bestehen. Das Buchungssystem lässt sich einfach verlinken oder einbinden."),
("Can this replace my existing CRM or Mailchimp?", "Ersetzt JKB Software unsere bisherigen Tools?"),
("Yes. Our platform includes a full CRM, unlimited email marketing, and SMS capabilities. Most of our clients cancel 3-5 other software subscriptions when they switch to us.",
 "Ja. Unsere Plattform umfasst Buchung, Mitgliederverwaltung, Abrechnung und Kommunikation. Die meisten Kunden kündigen nach dem Wechsel mehrere andere Software-Abos."),
("How does the Missed Call Auto-Responder work?", "Wie funktioniert die automatische Abrechnung?"),
("When a customer calls your business number and you don't answer, the system instantly texts them back (e.g., 'Sorry we missed your call! How can we help you?'). This stops leads from calling your competitors.",
 "Beiträge und Gebühren werden automatisch berechnet und auf Wunsch per SEPA-Lastschrift eingezogen. Rechnungen und Zahlungserinnerungen verschickt das System selbstständig."),
("Are there any hidden fees?", "Gibt es versteckte Kosten?"),
("No hidden fees. You pay a simple flat monthly rate. You may just pay fractional cents directly to telecom providers for your SMS usage, exactly what it costs.",
 "Nein. Sie zahlen einen transparenten monatlichen Festpreis – ohne versteckte Gebühren. Jederzeit kündbar."),

# ===== CTA / FOOTER =====
("Ready to put Your Local Business Growth on", "Bereit, Ihre Verwaltung auf"),
("Autopilot?", "Autopilot zu stellen?"),
("Stop wasting thousands on scattered tools that don't convert and start enjoying streamlined, predictable growth.",
 "Schluss mit verstreuten Tools und manueller Arbeit – starten Sie jetzt mit JKB Software in die digitale Verwaltung."),
("Start Your 14-Days Free Trial", "Jetzt 14 Tage kostenlos testen"),
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
(">Contact<", ">Kontakt<"),
(">Case Studies<", ">Referenzen<"),
(">Blog<", ">Blog<"),

# ===== META =====
("<title>Automark", "<title>JKB Software – Digitale Verwaltung für Vereine, Hotels &amp; Unternehmen"),
]

def variants(s):
    out = [s]
    if "&" in s and "&amp;" not in s:
        out.append(s.replace("&", "&amp;"))
    if "&amp;" in s:
        out.append(s.replace("&amp;", "&"))
    if "'" in s:
        out.extend([v.replace("'", "&#39;") for v in list(out)])
        out.extend([v.replace("'", "\u2019") for v in [s]])
    if '"' in s:
        out.extend([v.replace('"', "&quot;") for v in list(out)])
    return out

missed = []
for old, new in R:
    done = False
    for v in variants(old):
        if v in html:
            html = html.replace(v, new)
            done = True
            break
    if not done:
        missed.append(old[:70])

open(P, "w", encoding="utf-8").write(html)
print("ersetzt:", len(R) - len(missed), "/", len(R))
for m in missed:
    print("NICHT GEFUNDEN:", m)

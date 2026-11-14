#!/usr/bin/env python3
import html, re

CONNECTORS = [
("Google Drive","Dateien sofort suchen, lesen und hochladen"),
("Gmail","Antworten verfassen, Threads zusammenfassen und den Posteingang durchsuchen"),
("Google Calendar","Deinen Kalender verwalten und Meetings mühelos koordinieren"),
("Canva","Canva-Designs suchen, erstellen, befüllen und exportieren"),
("Microsoft 365","Greife direkt in Claude auf SharePoint, OneDrive, Outlook und Teams zu"),
("Notion","Verbinde deinen Notion-Workspace, um Workflows zu suchen, zu aktualisieren und toolübergreifend zu steuern."),
("Figma","Diagramme und besseren Code aus Figma-Kontext generieren"),
("Slack","Nachrichten senden, Canvases erstellen und Slack-Daten abrufen"),
("Atlassian MCP","Jira, Confluence, Bitbucket, Loom und weitere Atlassian-Apps suchen, lesen und aktualisieren – mit deinen vorhandenen Atlassian-Berechtigungen."),
("HubSpot","CRM-Kontext für jede Antwort, jeden Einblick und jede Aktion"),
("Asana","Mit Asana Aufgaben, Projekte und Ziele koordinieren"),
("Linear","Issues, Projekte und Team-Workflows in Linear verwalten"),
("monday.com","monday.com Projektmanagement & CRM für Projekte, Aufgaben, Portfolios, Boards, Workflows, Meilensteine, Abhängigkeiten, Formulare, Dashboards und mehr."),
("Intercom","Zugriff auf Intercom-Daten für bessere Kundeneinblicke"),
("Box","Box-Inhalte durchsuchen, bearbeiten und analysieren"),
("Adobe","Gestalten, kombinieren und bearbeiten mit professionellen Adobe-Tools"),
("Supabase","Datenbanken, Authentifizierung und Speicher verwalten"),
("Miro","Miro-Boards aufrufen und neue Inhalte erstellen"),
("Shopify","Deinen Shopify-Shop aufbauen, verwalten und analysieren"),
("Vercel","Projekte und Deployments analysieren, debuggen und verwalten"),
("Zoom for Claude","Zoom-Meetings durchsuchen, zusammenfassen und Aktionen ausführen"),
("Granola","Der KI-Notizblock für Meetings, jetzt in Claude. Frag nach deinen Notizen, Transkripten und Meeting-Kontext."),
("Spotify","Musik- und Podcast-Empfehlungen, ganz auf dich zugeschnitten."),
("Indeed","Auf Indeed nach Jobs suchen"),
("Gamma","Präsentationen, Dokumente, Social-Posts und Websites mit KI erstellen"),
("Wispr Flow","Deine Meetings, Notizen und Aufgaben aus Wispr Flow – jetzt nativer Kontext für Claude."),
("Salesforce – Beta","Verkaufen, betreuen und skalieren mit Salesforce."),
("Zapier","Workflows über tausende Apps hinweg per Konversation automatisieren"),
("Microsoft Learn","Durchsuche vertrauenswürdige Microsoft-Docs für deine Entwicklung"),
("PubMed","Biomedizinische Literatur über PubMed durchsuchen"),
("Airtable","Deine strukturierten Daten in Claude einbringen"),
("Lucid","Ideen entwickeln, Diagramme erstellen und Teams abstimmen"),
("vidIQ","Für YouTube, Instagram & TikTok recherchieren und erstellen"),
("ClickUp","Projektmanagement und Zusammenarbeit für Teams und KI-Agenten"),
("ElevenLabs","ElevenAgents-Sprachagenten direkt im Chat verwalten"),
("Datadog","Probleme mit Datadog-Telemetrie debuggen und beheben"),
("Docusign","Intelligentes, sicheres Vertragsmanagement von Docusign"),
("Windsor.ai","Instagram, Meta Ads, Google Ads, Google Analytics, YouTube, TikTok, LinkedIn und 350+ weitere Quellen – Reporting und Verwaltung in einem."),
("Strava","Deine Strava-Daten analysieren, zusammenfassen und erkunden"),
("Sentry","Fehler intelligent suchen, abfragen und debuggen"),
("Apollo.io","Leads über Einstellungs- und Finanzierungssignale finden, Kontakte anreichern und Outreach-Sequenzen verwalten"),
("Stripe","Tools für Zahlungsabwicklung und Finanzinfrastruktur"),
("Lovable","Lovable-Apps erstellen, iterieren, prüfen und deployen"),
("Cloudflare Developer Platform","Anwendungen mit Compute, Storage und KI entwickeln"),
("Metricool","Social-Media-Beiträge mit KI planen, analysieren und verwalten."),
("Dropbox","Dropbox-Inhalte durchsuchen, organisieren und bearbeiten"),
("Google Cloud BigQuery","BigQuery: Fortgeschrittene Analyseerkenntnisse für Agenten"),
("Consensus","Wissenschaftliche Forschung erkunden"),
("Booking.com","Hotels, Ferienwohnungen und mehr finden"),
("Todoist","Aufgaben in Todoist suchen, abschließen und verwalten"),
("HyperFrames by HeyGen","Animierte Folien und Motion Graphics mit HTML erstellen"),
("Semrush","SEO, Keyword-Recherche, Wettbewerbsanalyse, Traffic- und Marktanalysen, Backlink-Analyse und PPC"),
("Supermetrics","Analysiere und verwalte Werbekampagnen und Social Media – PPC, SEO, E-Commerce und Social-Media-Analytics"),
("WordPress.com","Sicherer KI-Zugriff zur Verwaltung deiner WordPress.com-Sites"),
("Smartsheet","Smartsheet-Daten mit Claude analysieren und verwalten"),
("ZoomInfo","Prospects finden, Accounts recherchieren, Käufer mit verifizierten B2B-Daten anreichern."),
("Firecrawl","Web-Daten suchen und extrahieren"),
("Context7","Aktuelle Dokumentation für LLMs und KI-Code-Editoren"),
("NetSuite","Claude mit NetSuite-Daten verbinden – für Analysen und Insights"),
("Trello","Mit Trello Aufgaben erledigen"),
("Postman","Gib deinen Coding-Agenten API-Kontext"),
("Clinical Trials","Auf ClinicalTrials.gov-Daten zugreifen"),
("Ahrefs","SEO- und KI-Such-Analytik"),
("Snowflake","Strukturierte und unstrukturierte Daten abrufen"),
("Intuit QuickBooks","Geschäftsfinanzen leicht gemacht"),
("Webflow","Seiten gestalten, CMS-Inhalte verwalten, Traffic analysieren und die gesamte Website launchen – alles per Prompt."),
("Plaud","Durchsuche deine Plaud-Aufnahmen und extrahiere wertvolle Erkenntnisse."),
("Expedia","Reisen planen: Flüge und Hotels mit Echtzeit-Preisen und Karten suchen"),
("Clay","Prospects finden, Accounts recherchieren, Outreach personalisieren"),
("Fireflies","Meeting-Transkripte analysieren und Erkenntnisse gewinnen"),
("Netlify","Websites auf Netlify erstellen, deployen, verwalten und absichern."),
("bioRxiv","Auf bioRxiv- und medRxiv-Preprint-Daten zugreifen"),
("Excalidraw","Interaktive handgezeichnete Diagramme in Excalidraw erstellen"),
("Make","Make-Szenarien ausführen und dein Make-Konto verwalten"),
("PitchBook Premium","PitchBook-Daten – direkt in deinem Arbeitsablauf."),
("Hugging Face","Zugriff auf den Hugging Face Hub und tausende Gradio-Apps"),
("PostHog","PostHog-Insights abfragen, analysieren und verwalten"),
("Superhuman Mail","Der beste E-Mail- und Kalender-Assistent für Gmail und Outlook."),
("Exa","Websuche + Suche in Code-Dokumentationen"),
("S&P – Deterministic Retrieval","Deterministischer Zugriff auf S&P-Global-Daten"),
("n8n","Deine n8n-Workflows aufrufen und ausführen"),
("Fathom","Deine Meeting-Notizen, Transkripte und der gesamte Kontext – jetzt Teil jedes Claude-Gesprächs"),
("Mobbin","UI- & UX-Design-Referenzen finden"),
("Interactive Brokers (IBKR)","Handeln, investieren, analysieren und globale Märkte verwalten"),
("Xero","Greife in jeder Konversation auf deine Xero-Finanzdaten zu"),
("Amplitude","Amplitude-Daten durchsuchen, abrufen und Erkenntnisse daraus gewinnen"),
("ChEMBL","Auf die ChEMBL-Datenbank zugreifen"),
("Kiwi.com","Flüge direkt in Claude suchen"),
("Calendly","Termine verwalten und Meeting-Zusammenfassungen abrufen."),
("Adobe CX Enterprise Coworker","CX-Workflows vorantreiben"),
("Wix","Erstelle eine Website oder einen Onlineshop, sichere dir eine Domain und verwalte alles auf Wix"),
("Descript","Videos per Spracheingabe importieren, bearbeiten oder erstellen"),
("Jotform","Formulare, Umfragen und Quizze erstellen & Einreichungen analysieren"),
("Ramp","Ausgaben analysieren sowie Belege, Rechnungen und Genehmigungen in Ramp verwalten"),
("Klaviyo","Berichten, strategieren und erstellen mit Live-Daten aus Klaviyo"),
("Mermaid Chart","Mermaid-Diagramme prüfen, als SVG rendern und interaktiv iterieren."),
("Wiley Scholar Gateway","Antworten mit wissenschaftlicher Forschung und Zitaten untermauern"),
("Vibe Prospecting","Unternehmens- und Kontaktdaten finden und anreichern – 150 Mio.+ Unternehmen, 800 Mio.+ Kontakte"),
("FactSet AI-Ready Data","Zugang zu institutionellen Finanzdaten und Analysen"),
("Anthropic Economic Index","Öffentliche Daten zur weltweiten Nutzung von Claude erkunden"),
("Adobe Experience Manager","Deinen Adobe Experience Manager-Content verwalten"),
("Mixpanel","Mixpanel-Daten analysieren, abfragen und verwalten"),
("Intuit Mailchimp","Marketing-Kampagnen erstellen"),
("Lusha","B2B-Kontakte und Unternehmen finden und anreichern"),
("Elicit","Wissenschaftliche Publikationen suchen und analysieren"),
("Gong","Gong MCP Server"),
("TikTok for Business","TikTok-Werbekampagnen erstellen, verwalten und analysieren"),
("Trimble SketchUp","3D-Modelle für SketchUp erstellen und iterieren"),
("lastminute.com","Flüge, Kombi-Pakete (Flug + Hotel) und Hotels weltweit suchen, vergleichen und buchen."),
("Uber","Uber-Preis- und Zeitschätzungen für alle Fahrtoptionen abrufen"),
("NPI Registry","Auf das US National Provider Identifier (NPI) Registry zugreifen"),
("Tripadvisor","Finde dein perfektes Hotel anhand von Tripadvisor-Bewertungen"),
("BioRender","BioRender-Bibliothek durchsuchen und wissenschaftliche Abbildungen direkt aus Claude erstellen."),
("ServiceNow","Unternehmens-Workflows auslösen, automatisieren und orchestrieren"),
("Alpha Vantage","Börsenmarktdaten: Aktien, Optionen, Fundamentaldaten, Earnings, News, Wechselkurse und mehr"),
("Scite","Evidenzbasierte Antworten auf Basis wissenschaftlicher Forschung"),
("Adobe Workfront","Planung, Projekte, Aufgaben und Freigaben verwalten"),
("Harvey","Rechtliche Anfragen beantworten, Vaults durchsuchen und recherchieren"),
("ZipRecruiter","Jobsuche leicht gemacht."),
("Similarweb","Echtzeit-Daten zu Web, mobilen Apps und Märkten."),
]

COLORS=["#D97757","#E08A64","#C4683F","#B85C3E","#E6997A","#A85838"]

cards=[]
for idx,(name,desc) in enumerate(CONNECTORS):
    initial=html.escape(name[0].upper())
    c=COLORS[idx%len(COLORS)]
    cards.append(
      f'<div class="conn-card"><div class="conn-icon" style="background:{c}">{initial}</div>'
      f'<div class="conn-body"><div class="conn-name">{html.escape(name)}</div>'
      f'<div class="conn-desc">{html.escape(desc)}</div></div></div>')

grid=('<div class="conn-count">1126 Konnektoren</div>\n'
      '<div class="conn-grid">\n'+"\n".join(cards)+'\n</div>\n'
      '<p class="conn-more">… und noch viele mehr – fehlende Konnektoren entwickeln wir individuell für Sie.</p>')

css='''
<style>
.conn-count{text-align:center;margin:0 0 28px;font-weight:600;color:var(--accent);font-size:1rem;letter-spacing:.02em}
.conn-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;max-width:1200px;margin:0 auto}
.conn-card{display:flex;gap:12px;align-items:flex-start;background:var(--surface-2,#fff);border:1px solid var(--border,rgba(36,24,18,.08));border-radius:14px;padding:14px 16px;box-shadow:var(--shadow-sm,0 2px 12px rgba(36,24,18,.06))}
.conn-icon{flex:0 0 38px;width:38px;height:38px;border-radius:10px;display:grid;place-items:center;color:#fff;font-weight:700;font-size:1.05rem}
.conn-name{font-weight:600;color:var(--text-1,#241812);font-size:.95rem;margin-bottom:2px}
.conn-desc{font-size:.8rem;line-height:1.45;color:var(--text-3,#8C7263)}
.conn-more{text-align:center;margin-top:30px;color:var(--text-2,#5C463A);font-size:1rem;font-weight:500}
</style>
'''

s=open("edith.html").read()
m=re.search(r'<div class="integrations-grid">.*?</div>\s*</div>\s*</section>', s, re.S)
assert m, "Grid nicht gefunden"
old=m.group(0)
new=css+grid+'\n    </div>\n  </section>'
s=s.replace(old,new)
open("edith.html","w").write(s)
print("OK:",len(CONNECTORS),"Konnektoren eingefügt")

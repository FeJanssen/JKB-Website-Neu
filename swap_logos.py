#!/usr/bin/env python3
import re

# (Name, Domain für Logo)
L=[
("Google Drive","drive.google.com"),("Gmail","gmail.com"),("Google Calendar","calendar.google.com"),
("Canva","canva.com"),("Microsoft 365","microsoft.com"),("Notion","notion.so"),("Figma","figma.com"),
("Slack","slack.com"),("Atlassian","atlassian.com"),("HubSpot","hubspot.com"),("Asana","asana.com"),
("Linear","linear.app"),("monday.com","monday.com"),("Intercom","intercom.com"),("Box","box.com"),
("Adobe","adobe.com"),("Supabase","supabase.com"),("Miro","miro.com"),("Shopify","shopify.com"),
("Vercel","vercel.com"),("Zoom","zoom.us"),("Granola","granola.ai"),("Spotify","spotify.com"),
("Indeed","indeed.com"),("Gamma","gamma.app"),("Wispr Flow","wisprflow.ai"),("Salesforce","salesforce.com"),
("Zapier","zapier.com"),("Microsoft Learn","learn.microsoft.com"),("PubMed","pubmed.ncbi.nlm.nih.gov"),
("Airtable","airtable.com"),("Lucid","lucid.co"),("vidIQ","vidiq.com"),("ClickUp","clickup.com"),
("ElevenLabs","elevenlabs.io"),("Datadog","datadoghq.com"),("Docusign","docusign.com"),
("Windsor.ai","windsor.ai"),("Strava","strava.com"),("Sentry","sentry.io"),("Apollo.io","apollo.io"),
("Stripe","stripe.com"),("Lovable","lovable.dev"),("Cloudflare","cloudflare.com"),("Metricool","metricool.com"),
("Dropbox","dropbox.com"),("Google BigQuery","cloud.google.com"),("Consensus","consensus.app"),
("Booking.com","booking.com"),("Todoist","todoist.com"),("HeyGen","heygen.com"),("Semrush","semrush.com"),
("Supermetrics","supermetrics.com"),("WordPress.com","wordpress.com"),("Smartsheet","smartsheet.com"),
("ZoomInfo","zoominfo.com"),("Firecrawl","firecrawl.dev"),("Context7","context7.com"),
("NetSuite","netsuite.com"),("Trello","trello.com"),("Postman","postman.com"),
("ClinicalTrials.gov","clinicaltrials.gov"),("Ahrefs","ahrefs.com"),("Snowflake","snowflake.com"),
("QuickBooks","quickbooks.intuit.com"),("Webflow","webflow.com"),("Plaud","plaud.ai"),
("Expedia","expedia.com"),("Clay","clay.com"),("Fireflies","fireflies.ai"),("Netlify","netlify.com"),
("bioRxiv","biorxiv.org"),("Excalidraw","excalidraw.com"),("Make","make.com"),("PitchBook","pitchbook.com"),
("Hugging Face","huggingface.co"),("PostHog","posthog.com"),("Superhuman","superhuman.com"),
("Exa","exa.ai"),("S&P Global","spglobal.com"),("n8n","n8n.io"),("Fathom","fathom.video"),
("Mobbin","mobbin.com"),("Interactive Brokers","interactivebrokers.com"),("Xero","xero.com"),
("Amplitude","amplitude.com"),("ChEMBL","ebi.ac.uk"),("Kiwi.com","kiwi.com"),("Calendly","calendly.com"),
("Wix","wix.com"),("Descript","descript.com"),("Jotform","jotform.com"),("Ramp","ramp.com"),
("Klaviyo","klaviyo.com"),("Mermaid Chart","mermaidchart.com"),("Wiley","wiley.com"),
("FactSet","factset.com"),("Anthropic","anthropic.com"),("Mixpanel","mixpanel.com"),
("Mailchimp","mailchimp.com"),("Lusha","lusha.com"),("Elicit","elicit.com"),("Gong","gong.io"),
("TikTok for Business","tiktok.com"),("SketchUp","sketchup.com"),("lastminute.com","lastminute.com"),
("Uber","uber.com"),("Tripadvisor","tripadvisor.com"),("BioRender","biorender.com"),
("ServiceNow","servicenow.com"),("Alpha Vantage","alphavantage.co"),("Scite","scite.ai"),
("Workfront","workfront.com"),("Harvey","harvey.ai"),("ZipRecruiter","ziprecruiter.com"),
("Similarweb","similarweb.com"),
]

tiles="\n".join(
  f'<div class="logo-tile" title="{n}"><img src="https://logo.clearbit.com/{d}?size=80" alt="{n}" loading="lazy" onerror="this.parentElement.style.display=\'none\'"></div>'
  for n,d in L)

new_block=f'''<style>
.conn-count{{text-align:center;margin:0 0 28px;font-weight:600;color:var(--accent);font-size:1rem;letter-spacing:.02em}}
.logo-wrap{{position:relative;max-height:340px;overflow:hidden;transition:max-height .6s ease}}
.logo-wrap.expanded{{max-height:3000px}}
.logo-wrap::after{{content:"";position:absolute;left:0;right:0;bottom:0;height:140px;background:linear-gradient(to bottom,transparent,var(--bg,#F8EEE8));pointer-events:none;transition:opacity .4s}}
.logo-wrap.expanded::after{{opacity:0}}
.logo-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(110px,1fr));gap:14px;max-width:1100px;margin:0 auto}}
.logo-tile{{background:var(--surface-2,#fff);border:1px solid var(--border,rgba(36,24,18,.08));border-radius:14px;aspect-ratio:1/1;display:grid;place-items:center;padding:20px;box-shadow:var(--shadow-sm,0 2px 12px rgba(36,24,18,.06));transition:transform .2s}}
.logo-tile:hover{{transform:translateY(-3px)}}
.logo-tile img{{max-width:100%;max-height:100%;object-fit:contain}}
.logo-more-row{{text-align:center;margin-top:26px}}
.btn-show-more{{display:inline-block;padding:13px 32px;border-radius:999px;background:var(--accent,#D97757);color:#fff;font-weight:600;border:none;cursor:pointer;font-size:.95rem;transition:background .2s}}
.btn-show-more:hover{{background:var(--accent-mid,#E08A64)}}
.conn-more{{text-align:center;margin-top:22px;color:var(--text-2,#5C463A);font-size:1rem;font-weight:500}}
</style>
<div class="conn-count">1126 Konnektoren</div>
<div class="logo-wrap" id="logo-wrap">
<div class="logo-grid">
{tiles}
</div>
</div>
<div class="logo-more-row"><button class="btn-show-more" id="logo-more-btn" type="button">Mehr anzeigen</button></div>
<p class="conn-more">… und noch viele mehr – fehlende Konnektoren entwickeln wir individuell für Sie.</p>
<script>
document.getElementById('logo-more-btn').addEventListener('click',function(){{
  var w=document.getElementById('logo-wrap');
  w.classList.toggle('expanded');
  this.textContent=w.classList.contains('expanded')?'Weniger anzeigen':'Mehr anzeigen';
}});
</script>'''

s=open("edith.html").read()
m=re.search(r'<style>\s*\.conn-count.*?</div>\s*\n?<p class="conn-more">.*?</p>', s, re.S)
assert m, "Alter Block nicht gefunden"
s=s.replace(m.group(0), new_block)
open("edith.html","w").write(s)
print("OK – Logos:",len(L))

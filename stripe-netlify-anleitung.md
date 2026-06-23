# Stripe Subscription System - Komplette Anleitung

## 🎯 System-Übersicht

Ihr System funktioniert so:
1. **Kunde wählt Abo** → Zahlt via Stripe
2. **Stripe sendet Webhook** → Netlify Function empfängt Event
3. **Verein wird angelegt** → In Ihrer Datenbank mit automatisch generierter ID
4. **Monatliche Zahlung** → Stripe zieht automatisch Geld ein

---

## � Schritt 1: Code zu GitHub/Netlify deployen

```bash
cd /Users/FJMarketing/Desktop/JKB-Website
git add .
git commit -m "Add Stripe Subscription System with Netlify Functions"
git push
```

---

## 🔧 Schritt 2: Netlify Environment Variables

Gehen Sie zu: https://app.netlify.com → Ihre Site → **Site settings** → **Environment variables**

Fügen Sie hinzu:

### Variable 1: STRIPE_SECRET_KEY
- **Key:** `STRIPE_SECRET_KEY`
- **Value:** Ihr Stripe Secret Key (beginnt mit `sk_test_...`)
- **Finden Sie hier:** https://dashboard.stripe.com/test/apikeys

### Variable 2: STRIPE_WEBHOOK_SECRET (wichtig!)
- **Key:** `STRIPE_WEBHOOK_SECRET`  
- **Value:** Wird in Schritt 3 erstellt

---

## 🪝 Schritt 3: Stripe Webhook einrichten

### 3.1 Webhook erstellen
1. Gehen Sie zu: https://dashboard.stripe.com/test/webhooks
2. Klicken Sie auf **"Endpunkt hinzufügen"**
3. **Endpunkt-URL:** `https://ihre-netlify-domain.netlify.app/.netlify/functions/stripe-webhook`
   - Ersetzen Sie `ihre-netlify-domain` mit Ihrer echten Domain!
4. **Events auswählen:**
   - ✅ `checkout.session.completed`
   - ✅ `customer.subscription.created`
   - ✅ `customer.subscription.updated`
   - ✅ `customer.subscription.deleted`
   - ✅ `invoice.payment_succeeded`
   - ✅ `invoice.payment_failed`
5. Klicken Sie **"Endpunkt hinzufügen"**

### 3.2 Webhook Secret kopieren
1. Nach dem Erstellen sehen Sie den **Signaturschlüssel** (beginnt mit `whsec_...`)
2. Kopieren Sie diesen
3. Fügen Sie ihn in Netlify als **`STRIPE_WEBHOOK_SECRET`** hinzu

---

## ✅ Schritt 4: Netlify neu deployen

Nach dem Hinzufügen der Environment Variables:
1. Gehen Sie zu **Deploys** Tab
2. Klicken Sie **Trigger deploy** → **Deploy site**

---

## 🗄️ Schritt 5: Datenbank-Integration (TODO)

Die Datei `netlify/functions/stripe-webhook.js` enthält Platzhalter-Funktionen:

### TODO: Implementieren Sie diese Funktionen

```javascript
// 1. Verein anlegen nach erfolgreicher Zahlung
async function createClubInDatabase(session) {
  // Ihre Logik hier:
  // - Verein-Name aus session.customer_details.name
  // - E-Mail aus session.customer_details.email
  // - Stripe Customer ID: session.customer
  // - Subscription ID: session.subscription
  // - Plan ermitteln aus session.line_items[0].price.id
  // - Auto-generierte ID in Datenbank
}

// 2. Verein deaktivieren bei Kündigung
async function deactivateClubInDatabase(subscription) {
  // Suchen Sie Verein mit subscription.id
  // Setzen Sie status = 'inactive'
}

// 3. Kunde benachrichtigen bei Zahlungsfehler
async function notifyCustomerPaymentFailed(invoice) {
  // E-Mail an invoice.customer_email senden
}
```

---

## 🧪 Schritt 6: Testen

### Test-Kreditkarten (Stripe Test Mode)
- **Erfolgreiche Zahlung:** `4242 4242 4242 4242`
- **Abgelehnte Zahlung:** `4000 0000 0000 0002`
- **CVV:** Beliebig (z.B. `123`)
- **Datum:** Zukunft (z.B. `12/34`)

### Test-Ablauf
1. Öffnen Sie: `https://ihre-domain.netlify.app/products/jkb-grounds.html`
2. Klicken Sie **"Jetzt starten"** bei einem Plan
3. Zahlen Sie mit Test-Karte
4. Prüfen Sie Netlify Function Logs: **Functions** → `stripe-webhook`
5. Sehen Sie das Event `checkout.session.completed`? ✅

---

## � Monatliche Zahlungen

**Automatisch:** Stripe zieht jeden Monat Geld ein!
- Bei Erfolg: Event `invoice.payment_succeeded`
- Bei Fehler: Event `invoice.payment_failed`

Sie müssen nur die Webhook-Events verarbeiten.

---

## 🔑 Wichtige Dateien

| Datei | Zweck |
|-------|-------|
| `netlify/functions/create-checkout-session.js` | Erstellt Stripe Checkout |
| `netlify/functions/stripe-webhook.js` | Empfängt Stripe Events |
| `products/jkb-grounds.html` | Frontend mit Checkout |
| `pricing.html` | Alternative Pricing-Seite |

---

## 🐛 Troubleshooting

**Problem:** Function gibt 500 Error
- ✅ Prüfen Sie: `STRIPE_SECRET_KEY` in Netlify gesetzt?
- ✅ Schauen Sie in Function Logs (Netlify Dashboard)

**Problem:** Webhook funktioniert nicht
- ✅ Prüfen Sie: `STRIPE_WEBHOOK_SECRET` korrekt?
- ✅ Webhook URL endet auf `/.netlify/functions/stripe-webhook`?
- ✅ Richtige Events ausgewählt?

**Problem:** Verein wird nicht angelegt
- ✅ Implementieren Sie `createClubInDatabase()` Funktion
- ✅ Verbinden Sie Ihre Datenbank (z.B. Supabase, PostgreSQL, etc.)

---

## 🎉 Fertig!

Ihr Subscription-System ist jetzt bereit. Sobald Sie die Datenbank-Funktionen implementiert haben, läuft alles automatisch:

1. ✅ Kunde zahlt
2. ✅ Verein wird angelegt
3. ✅ Monatliche Zahlungen laufen
4. ✅ Bei Kündigung: Verein wird deaktiviert

**Nächster Schritt:** Welche Datenbank verwenden Sie? Ich kann Ihnen helfen, die Integration zu implementieren!

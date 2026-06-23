# Stripe Checkout mit Netlify Functions - Deployment Anleitung

## 🚀 Schritt 1: Code zu GitHub pushen

```bash
cd /Users/FJMarketing/Desktop/JKB-Website
git add .
git commit -m "Add Stripe Checkout with Netlify Functions"
git push
```

## 🔧 Schritt 2: Netlify Environment Variables setzen

1. Gehen Sie zu Ihrem Netlify Dashboard: https://app.netlify.com
2. Wählen Sie Ihre Website
3. Gehen Sie zu **Site settings** → **Environment variables**
4. Fügen Sie folgende Variable hinzu:

   **Key:** `STRIPE_SECRET_KEY`
   **Value:** Ihr Stripe Secret Key (beginnt mit `sk_test_...`)

   ⚠️ **WICHTIG:** Verwenden Sie Ihren **Secret Key**, nicht den Publishable Key!
   
   Finden Sie ihn hier: https://dashboard.stripe.com/test/apikeys

## 📦 Schritt 3: Netlify neu deployen

Nachdem Sie den Environment Variable hinzugefügt haben:

1. Gehen Sie zu **Deploys** Tab
2. Klicken Sie auf **Trigger deploy** → **Deploy site**

Oder pushen Sie einfach Ihren Code zu GitHub - Netlify deployed automatisch!

## ✅ Schritt 4: Testen

1. Öffnen Sie Ihre deployed Website
2. Gehen Sie zu: `https://ihre-domain.netlify.app/products/jkb-grounds.html`
3. Klicken Sie auf "Jetzt starten" bei einem Plan
4. Sie sollten zu Stripe Checkout weitergeleitet werden

## 🔑 Stripe API Keys finden

**Test Mode Keys:**
- Publishable Key: `pk_test_...` (wird NICHT mehr benötigt)
- Secret Key: `sk_test_...` (als Environment Variable in Netlify)

Link: https://dashboard.stripe.com/test/apikeys

## 🎯 Vorteile dieser Lösung

✅ Sicherer - Secret Key ist nicht im Frontend-Code
✅ Keine Client-Only Integration nötig
✅ Funktioniert out-of-the-box mit Netlify
✅ Professioneller Standard
✅ Einfach zu warten

## 🐛 Troubleshooting

**Problem:** Function gibt Fehler zurück
- Prüfen Sie, ob `STRIPE_SECRET_KEY` in Netlify gesetzt ist
- Prüfen Sie die Function Logs in Netlify: **Functions** Tab → **create-checkout-session**

**Problem:** "Cannot find module 'stripe'"
- Netlify installiert Dependencies automatisch aus `package.json`
- Warten Sie, bis das Deployment abgeschlossen ist

## 📝 Wichtige Dateien

- `netlify/functions/create-checkout-session.js` - Netlify Function
- `package.json` - Dependencies (Stripe npm package)
- `products/jkb-grounds.html` - Frontend mit Checkout Integration

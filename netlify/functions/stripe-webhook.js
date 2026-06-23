const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

exports.handler = async (event) => {
  const sig = event.headers['stripe-signature'];
  const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;

  let stripeEvent;

  try {
    // Verify webhook signature
    stripeEvent = stripe.webhooks.constructEvent(
      event.body,
      sig,
      webhookSecret
    );
  } catch (err) {
    console.error('Webhook signature verification failed:', err.message);
    return {
      statusCode: 400,
      body: JSON.stringify({ error: `Webhook Error: ${err.message}` })
    };
  }

  // Handle the event
  switch (stripeEvent.type) {
    case 'checkout.session.completed':
      const session = stripeEvent.data.object;
      console.log('💰 Payment successful!', session.id);
      
      // TODO: Hier Verein in Datenbank anlegen
      // const customerId = session.customer;
      // const subscriptionId = session.subscription;
      // await createClubInDatabase(session);
      
      break;

    case 'customer.subscription.created':
      const subscription = stripeEvent.data.object;
      console.log('✅ Subscription created:', subscription.id);
      break;

    case 'customer.subscription.updated':
      const updatedSub = stripeEvent.data.object;
      console.log('🔄 Subscription updated:', updatedSub.id);
      break;

    case 'customer.subscription.deleted':
      const deletedSub = stripeEvent.data.object;
      console.log('❌ Subscription cancelled:', deletedSub.id);
      
      // TODO: Verein deaktivieren in Datenbank
      // await deactivateClubInDatabase(deletedSub);
      
      break;

    case 'invoice.payment_succeeded':
      const invoice = stripeEvent.data.object;
      console.log('💳 Invoice paid:', invoice.id);
      break;

    case 'invoice.payment_failed':
      const failedInvoice = stripeEvent.data.object;
      console.log('⚠️ Payment failed:', failedInvoice.id);
      
      // TODO: Kunde benachrichtigen
      // await notifyCustomerPaymentFailed(failedInvoice);
      
      break;

    default:
      console.log(`Unhandled event type: ${stripeEvent.type}`);
  }

  return {
    statusCode: 200,
    body: JSON.stringify({ received: true })
  };
};

// Placeholder Funktionen - Diese müssen Sie mit Ihrer Datenbank verbinden
async function createClubInDatabase(session) {
  // TODO: Implementieren Sie die Logik zum Anlegen eines Vereins
  // Beispiel:
  // const clubData = {
  //   name: session.customer_details.name,
  //   email: session.customer_details.email,
  //   stripe_customer_id: session.customer,
  //   stripe_subscription_id: session.subscription,
  //   plan: getPlanFromPriceId(session.line_items[0].price.id),
  //   status: 'active',
  //   created_at: new Date()
  // };
  // await database.clubs.insert(clubData);
  console.log('Creating club for customer:', session.customer);
}

async function deactivateClubInDatabase(subscription) {
  // TODO: Verein in Datenbank deaktivieren
  console.log('Deactivating club for subscription:', subscription.id);
}

async function notifyCustomerPaymentFailed(invoice) {
  // TODO: E-Mail an Kunden senden
  console.log('Notifying customer about failed payment:', invoice.customer);
}

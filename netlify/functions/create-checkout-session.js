const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

exports.handler = async (event) => {
  const headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'POST, OPTIONS'
  };

  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 200, headers, body: '' };
  }

  if (event.httpMethod !== 'POST') {
    return { 
      statusCode: 405, 
      headers, 
      body: JSON.stringify({ error: 'Method not allowed' }) 
    };
  }

  try {
    const { priceId } = JSON.parse(event.body);

    if (!priceId) {
      return {
        statusCode: 400,
        headers,
        body: JSON.stringify({ error: 'Price ID is required' })
      };
    }

    // Determine the base URL (works with Netlify, localhost, and custom domains)
    const protocol = event.headers['x-forwarded-proto'] || 'https';
    const host = event.headers['host'];
    const baseUrl = `${protocol}://${host}`;

    // Create Checkout Session
    const session = await stripe.checkout.sessions.create({
      line_items: [{
        price: priceId,
        quantity: 1,
      }],
      mode: 'subscription',
      success_url: `${baseUrl}/stripe-success.html?session_id={CHECKOUT_SESSION_ID}&price_id=${priceId}`,
      cancel_url: `${baseUrl}/products/jkb-grounds.html`,
      // Wichtig: Metadata für später (Verein-Erstellung)
      metadata: {
        integration_type: 'jkb_subscription',
        price_id: priceId
      }
    });

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({ 
        sessionId: session.id,
        url: session.url 
      })
    };
  } catch (error) {
    console.error('Error creating checkout session:', error);
    return {
      statusCode: 500,
      headers,
      body: JSON.stringify({ error: error.message })
    };
  }
};

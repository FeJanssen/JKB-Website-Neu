const { createClient } = require('@supabase/supabase-js');

exports.handler = async (event, context) => {
  // CORS headers
  const headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
  };

  // Handle preflight requests
  if (event.httpMethod === 'OPTIONS') {
    return {
      statusCode: 200,
      headers,
      body: '',
    };
  }

  // Only allow POST requests
  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      headers,
      body: JSON.stringify({ error: 'Method not allowed' }),
    };
  }

  try {
    // Parse request body
    const data = JSON.parse(event.body);
    const {
      clubName,
      street,
      houseNumber,
      postalCode,
      city,
      country,
      phone,
      email,
      sessionId,
      stripePriceId,
    } = data;

    // Validate required fields
    if (!clubName || !street || !houseNumber || !postalCode || !city || !country || !phone) {
      return {
        statusCode: 400,
        headers,
        body: JSON.stringify({ error: 'Missing required fields' }),
      };
    }

    // Initialize Supabase client
    const supabaseUrl = process.env.SUPABASE_URL;
    const supabaseServiceKey = process.env.SUPABASE_SERVICE_KEY;

    if (!supabaseUrl || !supabaseServiceKey) {
      console.error('Missing Supabase credentials');
      return {
        statusCode: 500,
        headers,
        body: JSON.stringify({ error: 'Server configuration error' }),
      };
    }

    const supabase = createClient(supabaseUrl, supabaseServiceKey);

    // 1. Create the club (Verein)
    const { data: clubData, error: clubError } = await supabase
      .from('verein')
      .insert([
        {
          name: clubName,
          street: street,
          house_number: houseNumber,
          postal_code: postalCode,
          city: city,
          country: country,
          phone: phone,
          email: email || null,
        },
      ])
      .select()
      .single();

    if (clubError) {
      console.error('Error creating club:', clubError);
      return {
        statusCode: 500,
        headers,
        body: JSON.stringify({ error: 'Failed to create club', details: clubError.message }),
      };
    }

    console.log('Club created:', clubData);

    // 2. If we have Stripe session data, get subscription info from Stripe
    let stripeCustomerId = null;
    let stripeSubscriptionId = null;
    let planId = null;

    if (sessionId) {
      // Get Stripe session details
      const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
      const session = await stripe.checkout.sessions.retrieve(sessionId);
      
      stripeCustomerId = session.customer;
      stripeSubscriptionId = session.subscription;

      // Find the subscription plan based on stripe_price_id
      if (stripePriceId) {
        const { data: planData, error: planError } = await supabase
          .from('subscription_plans')
          .select('id')
          .eq('stripe_price_id', stripePriceId)
          .eq('is_active', true)
          .single();

        if (!planError && planData) {
          planId = planData.id;
        }
      }

      // 3. Create subscription record if we have the necessary data
      if (stripeSubscriptionId && planId) {
        const subscription = await stripe.subscriptions.retrieve(stripeSubscriptionId);

        const { data: subscriptionData, error: subscriptionError } = await supabase
          .from('subscription')
          .insert([
            {
              verein_id: clubData.id,
              plan_id: planId,
              stripe_customer_id: stripeCustomerId,
              stripe_subscription_id: stripeSubscriptionId,
              status: subscription.status,
              current_period_start: new Date(subscription.current_period_start * 1000).toISOString(),
              current_period_end: new Date(subscription.current_period_end * 1000).toISOString(),
              cancel_at_period_end: subscription.cancel_at_period_end,
            },
          ])
          .select()
          .single();

        if (subscriptionError) {
          console.error('Error creating subscription:', subscriptionError);
          // Don't fail the whole request, club is already created
        } else {
          console.log('Subscription created:', subscriptionData);
        }
      }
    }

    // Success response
    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({
        success: true,
        club: {
          id: clubData.id,
          name: clubData.name,
        },
        message: 'Club successfully created',
      }),
    };

  } catch (error) {
    console.error('Error in create-club function:', error);
    return {
      statusCode: 500,
      headers,
      body: JSON.stringify({ 
        error: 'Internal server error',
        message: error.message 
      }),
    };
  }
};

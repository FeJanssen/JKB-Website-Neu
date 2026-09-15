const { createClient } = require('@supabase/supabase-js');
const bcrypt = require('bcryptjs');

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
    const { name, email, password, clubId, roleId } = data;

    // Validate required fields
    if (!name || !email || !password || !clubId || !roleId) {
      return {
        statusCode: 400,
        headers,
        body: JSON.stringify({ error: 'Alle Felder sind erforderlich' }),
      };
    }

    // Validate password length
    if (password.length < 8) {
      return {
        statusCode: 400,
        headers,
        body: JSON.stringify({ error: 'Passwort muss mindestens 8 Zeichen lang sein' }),
      };
    }

    // Validate email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      return {
        statusCode: 400,
        headers,
        body: JSON.stringify({ error: 'Ungültige E-Mail-Adresse' }),
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
        body: JSON.stringify({ error: 'Server-Konfigurationsfehler' }),
      };
    }

    const supabase = createClient(supabaseUrl, supabaseServiceKey);

    // Check if email already exists
    const { data: existingUser, error: checkError } = await supabase
      .from('nutzer')
      .select('id')
      .eq('email', email)
      .single();

    if (existingUser) {
      return {
        statusCode: 400,
        headers,
        body: JSON.stringify({ error: 'Diese E-Mail-Adresse wird bereits verwendet' }),
      };
    }

    // Hash password
    const saltRounds = 10;
    const hashedPassword = await bcrypt.hash(password, saltRounds);

    // Create admin user
    const { data: adminData, error: adminError } = await supabase
      .from('nutzer')
      .insert([
        {
          name: name,
          email: email,
          passwort: hashedPassword,
          verein_id: clubId,
          rolle_id: roleId,
          ist_bestaetigt: true,
        },
      ])
      .select()
      .single();

    if (adminError) {
      console.error('Error creating admin:', adminError);
      return {
        statusCode: 500,
        headers,
        body: JSON.stringify({ 
          error: 'Fehler beim Erstellen des Admin-Accounts', 
          details: adminError.message 
        }),
      };
    }

    console.log('Admin created successfully:', {
      id: adminData.id,
      name: adminData.name,
      email: adminData.email,
    });

    // Success response (don't send password back!)
    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({
        success: true,
        admin: {
          id: adminData.id,
          name: adminData.name,
          email: adminData.email,
        },
        message: 'Admin-Account erfolgreich erstellt',
      }),
    };

  } catch (error) {
    console.error('Error in create-admin function:', error);
    return {
      statusCode: 500,
      headers,
      body: JSON.stringify({ 
        error: 'Interner Serverfehler',
        message: error.message 
      }),
    };
  }
};

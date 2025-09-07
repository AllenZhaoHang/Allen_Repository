const { createClient } = require('@supabase/supabase-js');

const supabaseUrl = process.env.SUPABASE_URL;
const supabaseAnonKey = process.env.SUPABASE_ANON_KEY;

const supabase = createClient(supabaseUrl, supabaseAnonKey);

const authenticateUser = async (req, res, next) => {
  try {
    const authHeader = req.headers.authorization;
    console.log('Auth middleware - Authorization header:', authHeader ? 'Present' : 'Missing');
    
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      console.log('Auth middleware - No valid token provided');
      return res.status(401).json({ error: 'No token provided' });
    }

    const token = authHeader.substring(7);
    console.log('Auth middleware - Token length:', token.length);
    
    const { data: { user }, error } = await supabase.auth.getUser(token);
    
    if (error) {
      console.error('Auth middleware - Supabase error:', error);
      return res.status(401).json({ error: 'Invalid token' });
    }
    
    if (!user) {
      console.log('Auth middleware - No user found');
      return res.status(401).json({ error: 'Invalid token' });
    }

    console.log('Auth middleware - User authenticated:', user.id);
    req.user = user;
    next();
  } catch (error) {
    console.error('Auth middleware error:', error);
    res.status(500).json({ error: 'Authentication failed' });
  }
};

module.exports = { authenticateUser };

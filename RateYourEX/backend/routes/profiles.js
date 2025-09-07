const express = require('express');
const supabase = require('../utils/supabase');
const { authenticateUser } = require('../middleware/auth');

const router = express.Router();

// GET /api/profiles - List profiles with optional search
router.get('/', async (req, res) => {
  try {
    const { search, page = 1, limit = 20 } = req.query;
    const offset = (page - 1) * limit;

    let query = supabase
      .from('profiles')
      .select(`
        id,
        name,
        school,
        location,
        created_at,
        reviews:reviews(rating)
      `)
      .order('created_at', { ascending: false })
      .range(offset, offset + limit - 1);

    // Add search functionality - search by name, school, university, or company
    if (search) {
      query = query.or(`name.ilike.%${search}%,school.ilike.%${search}%`);
    }

    const { data: profiles, error } = await query;

    if (error) {
      console.error('Error fetching profiles:', error);
      return res.status(500).json({ error: 'Failed to fetch profiles' });
    }

    // Calculate average ratings
    const profilesWithRatings = profiles.map(profile => {
      const ratings = profile.reviews?.map(r => r.rating) || [];
      const averageRating = ratings.length > 0 
        ? (ratings.reduce((sum, rating) => sum + rating, 0) / ratings.length).toFixed(1)
        : 0;
      
      return {
        ...profile,
        averageRating: parseFloat(averageRating),
        reviewCount: ratings.length,
        reviews: undefined // Remove reviews array from response
      };
    });

    res.json({
      profiles: profilesWithRatings,
      pagination: {
        page: parseInt(page),
        limit: parseInt(limit),
        total: profilesWithRatings.length
      }
    });
  } catch (error) {
    console.error('Error in profiles route:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// GET /api/profiles/:id - Get profile with reviews
router.get('/:id', async (req, res) => {
  try {
    const { id } = req.params;

    // Get profile
    const { data: profile, error: profileError } = await supabase
      .from('profiles')
      .select('*')
      .eq('id', id)
      .single();

    if (profileError) {
      if (profileError.code === 'PGRST116') {
        return res.status(404).json({ error: 'Profile not found' });
      }
      console.error('Error fetching profile:', profileError);
      return res.status(500).json({ error: 'Failed to fetch profile' });
    }

    // Get reviews for this profile
    const { data: reviews, error: reviewsError } = await supabase
      .from('reviews')
      .select('id, rating, comment, created_at')
      .eq('profile_id', id)
      .order('created_at', { ascending: false });

    if (reviewsError) {
      console.error('Error fetching reviews:', reviewsError);
      return res.status(500).json({ error: 'Failed to fetch reviews' });
    }

    // Calculate average rating
    const ratings = reviews.map(r => r.rating);
    const averageRating = ratings.length > 0 
      ? (ratings.reduce((sum, rating) => sum + rating, 0) / ratings.length).toFixed(1)
      : 0;

    res.json({
      ...profile,
      averageRating: parseFloat(averageRating),
      reviewCount: reviews.length,
      reviews
    });
  } catch (error) {
    console.error('Error in profile detail route:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// POST /api/profiles - Create new profile (requires authentication)
router.post('/', authenticateUser, async (req, res) => {
  try {
    const { name, school, location } = req.body;

    if (!name || !school || !location) {
      return res.status(400).json({ 
        error: 'Name, school/university/company, and location are required' 
      });
    }

    const { data, error } = await supabase
      .from('profiles')
      .insert([
        {
          name: name.trim(),
          school: school.trim(),
          location: location.trim(),
          created_by: req.user.id
        }
      ])
      .select()
      .single();

    if (error) {
      console.error('Error creating profile:', error);
      return res.status(500).json({ error: 'Failed to create profile' });
    }

    res.status(201).json({
      message: 'Profile created successfully',
      profile: data
    });
  } catch (error) {
    console.error('Error in create profile route:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

module.exports = router;

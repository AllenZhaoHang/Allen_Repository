const express = require('express');
const supabase = require('../utils/supabase');
const { authenticateUser } = require('../middleware/auth');

const router = express.Router();

// GET /api/profiles/:id/reviews - Get reviews for a profile
router.get('/:id/reviews', async (req, res) => {
  try {
    const { id } = req.params;
    const { page = 1, limit = 20 } = req.query;
    const offset = (page - 1) * limit;

    // Check if profile exists
    const { data: profile, error: profileError } = await supabase
      .from('profiles')
      .select('id')
      .eq('id', id)
      .single();

    if (profileError) {
      if (profileError.code === 'PGRST116') {
        return res.status(404).json({ error: 'Profile not found' });
      }
      console.error('Error checking profile:', profileError);
      return res.status(500).json({ error: 'Failed to fetch profile' });
    }

    // Get reviews
    const { data: reviews, error: reviewsError } = await supabase
      .from('reviews')
      .select('id, rating, comment, created_at')
      .eq('profile_id', id)
      .order('created_at', { ascending: false })
      .range(offset, offset + limit - 1);

    if (reviewsError) {
      console.error('Error fetching reviews:', reviewsError);
      return res.status(500).json({ error: 'Failed to fetch reviews' });
    }

    res.json({
      reviews,
      pagination: {
        page: parseInt(page),
        limit: parseInt(limit),
        total: reviews.length
      }
    });
  } catch (error) {
    console.error('Error in reviews route:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// POST /api/profiles/:id/reviews - Add review to a profile (requires authentication)
router.post('/:id/reviews', authenticateUser, async (req, res) => {
  try {
    const { id } = req.params;
    const { rating, comment } = req.body;

    // Validate input
    if (!rating || rating < 1 || rating > 5) {
      return res.status(400).json({ 
        error: 'Rating must be between 1 and 5' 
      });
    }

    if (!comment || comment.trim().length === 0) {
      return res.status(400).json({ 
        error: 'Comment is required' 
      });
    }

    if (comment.trim().length > 1000) {
      return res.status(400).json({ 
        error: 'Comment must be less than 1000 characters' 
      });
    }

    // Check if profile exists
    const { data: profile, error: profileError } = await supabase
      .from('profiles')
      .select('id')
      .eq('id', id)
      .single();

    if (profileError) {
      if (profileError.code === 'PGRST116') {
        return res.status(404).json({ error: 'Profile not found' });
      }
      console.error('Error checking profile:', profileError);
      return res.status(500).json({ error: 'Failed to fetch profile' });
    }

    // Check if user has already reviewed this profile
    const { data: existingReview, error: existingError } = await supabase
      .from('reviews')
      .select('id')
      .eq('profile_id', id)
      .eq('created_by', req.user.id)
      .single();

    if (existingError && existingError.code !== 'PGRST116') {
      console.error('Error checking existing review:', existingError);
      return res.status(500).json({ error: 'Failed to check existing review' });
    }

    if (existingReview) {
      return res.status(400).json({ 
        error: 'You have already reviewed this profile' 
      });
    }

    // Create review
    const { data, error } = await supabase
      .from('reviews')
      .insert([
        {
          profile_id: id,
          rating: parseInt(rating),
          comment: comment.trim(),
          created_by: req.user.id
        }
      ])
      .select('id, rating, comment, created_at')
      .single();

    if (error) {
      console.error('Error creating review:', error);
      return res.status(500).json({ error: 'Failed to create review' });
    }

    res.status(201).json({
      message: 'Review created successfully',
      review: data
    });
  } catch (error) {
    console.error('Error in create review route:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

module.exports = router;

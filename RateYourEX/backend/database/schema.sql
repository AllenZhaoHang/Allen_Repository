-- Enable Row Level Security
ALTER DATABASE postgres SET "app.jwt_secret" TO 'your-jwt-secret';

-- Create profiles table
CREATE TABLE IF NOT EXISTS profiles (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    school VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    created_by UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create reviews table
CREATE TABLE IF NOT EXISTS reviews (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    profile_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
    rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
    comment TEXT NOT NULL,
    created_by UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_profiles_name ON profiles(name);
CREATE INDEX IF NOT EXISTS idx_profiles_school ON profiles(school);
CREATE INDEX IF NOT EXISTS idx_profiles_created_at ON profiles(created_at);
CREATE INDEX IF NOT EXISTS idx_reviews_profile_id ON reviews(profile_id);
CREATE INDEX IF NOT EXISTS idx_reviews_created_at ON reviews(created_at);
CREATE INDEX IF NOT EXISTS idx_reviews_rating ON reviews(rating);

-- Create updated_at trigger function
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create triggers for updated_at
CREATE TRIGGER update_profiles_updated_at 
    BEFORE UPDATE ON profiles 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_reviews_updated_at 
    BEFORE UPDATE ON reviews 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Enable Row Level Security
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE reviews ENABLE ROW LEVEL SECURITY;

-- Profiles policies
-- Anyone can read profiles
CREATE POLICY "Anyone can read profiles" ON profiles
    FOR SELECT USING (true);

-- Only authenticated users can create profiles
CREATE POLICY "Authenticated users can create profiles" ON profiles
    FOR INSERT WITH CHECK (auth.uid() IS NOT NULL);

-- Only the creator can update their profiles
CREATE POLICY "Users can update their own profiles" ON profiles
    FOR UPDATE USING (auth.uid() = created_by);

-- Only the creator can delete their profiles
CREATE POLICY "Users can delete their own profiles" ON profiles
    FOR DELETE USING (auth.uid() = created_by);

-- Reviews policies
-- Anyone can read reviews (but they're anonymous)
CREATE POLICY "Anyone can read reviews" ON reviews
    FOR SELECT USING (true);

-- Only authenticated users can create reviews
CREATE POLICY "Authenticated users can create reviews" ON reviews
    FOR INSERT WITH CHECK (auth.uid() IS NOT NULL);

-- Users can update their own reviews
CREATE POLICY "Users can update their own reviews" ON reviews
    FOR UPDATE USING (auth.uid() = created_by);

-- Users can delete their own reviews
CREATE POLICY "Users can delete their own reviews" ON reviews
    FOR DELETE USING (auth.uid() = created_by);

-- Create a view for profile statistics
CREATE OR REPLACE VIEW profile_stats AS
SELECT 
    p.id,
    p.name,
    p.school,
    p.location,
    p.created_at,
    COUNT(r.id) as review_count,
    COALESCE(AVG(r.rating), 0) as average_rating,
    COALESCE(MIN(r.rating), 0) as min_rating,
    COALESCE(MAX(r.rating), 0) as max_rating
FROM profiles p
LEFT JOIN reviews r ON p.id = r.profile_id
GROUP BY p.id, p.name, p.school, p.location, p.created_at;

-- Grant access to the view
GRANT SELECT ON profile_stats TO anon, authenticated;

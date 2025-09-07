-- Sample data for testing
-- Note: These are example profiles for demonstration purposes

-- Insert sample profiles
INSERT INTO profiles (name, school, location, created_by) VALUES
('Alex Johnson', 'Stanford University', 'Palo Alto, CA', (SELECT id FROM auth.users LIMIT 1)),
('Sarah Chen', 'MIT', 'Cambridge, MA', (SELECT id FROM auth.users LIMIT 1)),
('Michael Rodriguez', 'UC Berkeley', 'Berkeley, CA', (SELECT id FROM auth.users LIMIT 1)),
('Emily Davis', 'Harvard University', 'Cambridge, MA', (SELECT id FROM auth.users LIMIT 1)),
('David Kim', 'UCLA', 'Los Angeles, CA', (SELECT id FROM auth.users LIMIT 1)),
('Jessica Wang', 'NYU', 'New York, NY', (SELECT id FROM auth.users LIMIT 1)),
('Ryan Thompson', 'University of Chicago', 'Chicago, IL', (SELECT id FROM auth.users LIMIT 1)),
('Amanda Foster', 'Duke University', 'Durham, NC', (SELECT id FROM auth.users LIMIT 1));

-- Insert sample reviews (only if there are users in auth.users)
-- Note: These will only work if you have actual users in your auth.users table
INSERT INTO reviews (profile_id, rating, comment, created_by) 
SELECT 
    p.id,
    CASE (random() * 4 + 1)::int
        WHEN 1 THEN 5
        WHEN 2 THEN 4
        WHEN 3 THEN 3
        WHEN 4 THEN 2
        ELSE 1
    END,
    CASE (random() * 5 + 1)::int
        WHEN 1 THEN 'Great person, very kind and thoughtful.'
        WHEN 2 THEN 'Had some good times together, but we grew apart.'
        WHEN 3 THEN 'Nice person overall, just not compatible.'
        WHEN 4 THEN 'Very intelligent and ambitious, but communication was difficult.'
        WHEN 5 THEN 'Fun to be around, but different life goals.'
        ELSE 'Mixed experience, some good and some challenging moments.'
    END,
    (SELECT id FROM auth.users LIMIT 1)
FROM profiles p
WHERE EXISTS (SELECT 1 FROM auth.users LIMIT 1)
LIMIT 20;

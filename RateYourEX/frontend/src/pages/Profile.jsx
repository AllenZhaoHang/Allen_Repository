import { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import { ArrowLeft, GraduationCap, MapPin, Star } from 'lucide-react'
import { apiClient } from '../utils/api'
import { StarRating } from '../components/StarRating'
import { ReviewCard } from '../components/ReviewCard'
import { ReviewForm } from '../components/ReviewForm'

export const Profile = () => {
  const { id } = useParams()
  const [profile, setProfile] = useState(null)
  const [reviews, setReviews] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  const fetchProfile = async () => {
    try {
      setLoading(true)
      const data = await apiClient.getProfile(id)
      setProfile(data)
      setReviews(data.reviews || [])
      setError('')
    } catch (err) {
      setError('Failed to load profile')
      console.error('Error fetching profile:', err)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchProfile()
  }, [id])

  const handleReviewAdded = () => {
    // Refresh the profile data to get updated reviews
    fetchProfile()
  }

  if (loading) {
    return (
      <div className="flex justify-center items-center py-12">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    )
  }

  if (error || !profile) {
    return (
      <div className="text-center py-12">
        <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg max-w-md mx-auto">
          {error || 'Profile not found'}
        </div>
        <Link to="/" className="btn-primary mt-4">
          Back to Home
        </Link>
      </div>
    )
  }

  return (
    <div className="max-w-4xl mx-auto">
      {/* Back Button */}
      <Link
        to="/"
        className="inline-flex items-center space-x-2 text-gray-600 hover:text-primary-600 mb-6"
      >
        <ArrowLeft className="w-4 h-4" />
        <span>Back to profiles</span>
      </Link>

      {/* Profile Header */}
      <div className="card mb-8">
        <div className="flex items-start justify-between">
          <div className="flex-1">
            <h1 className="text-3xl font-bold text-gray-900 mb-4">
              {profile.name}
            </h1>
            
            <div className="space-y-3">
              <div className="flex items-center text-gray-600">
                <GraduationCap className="w-5 h-5 mr-3" />
                <span className="text-lg">{profile.school}</span>
              </div>
              
              <div className="flex items-center text-gray-600">
                <MapPin className="w-5 h-5 mr-3" />
                <span className="text-lg">{profile.location}</span>
              </div>
            </div>
          </div>
          
          <div className="text-right">
            <div className="flex items-center space-x-2 mb-2">
              <StarRating rating={profile.averageRating} size="lg" />
              <span className="text-2xl font-semibold text-gray-900">
                {profile.averageRating.toFixed(1)}
              </span>
            </div>
            <div className="text-gray-600">
              {profile.reviewCount} review{profile.reviewCount !== 1 ? 's' : ''}
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Reviews Section */}
        <div className="lg:col-span-2">
          <div className="mb-6">
            <h2 className="text-2xl font-semibold text-gray-900 mb-4">
              Reviews ({reviews.length})
            </h2>
          </div>
          
          {reviews.length === 0 ? (
            <div className="text-center py-12 bg-gray-50 rounded-lg">
              <Star className="w-12 h-12 text-gray-300 mx-auto mb-4" />
              <p className="text-gray-500 text-lg mb-2">No reviews yet</p>
              <p className="text-gray-400">Be the first to share your experience</p>
            </div>
          ) : (
            <div className="space-y-4">
              {reviews.map((review) => (
                <ReviewCard key={review.id} review={review} />
              ))}
            </div>
          )}
        </div>

        {/* Review Form Sidebar */}
        <div className="lg:col-span-1">
          <ReviewForm profileId={id} onReviewAdded={handleReviewAdded} />
        </div>
      </div>
    </div>
  )
}

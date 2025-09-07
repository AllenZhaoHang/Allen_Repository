import { Link } from 'react-router-dom'
import { Star, MapPin, GraduationCap } from 'lucide-react'

export const ProfileCard = ({ profile }) => {
  const renderStars = (rating) => {
    const stars = []
    const fullStars = Math.floor(rating)
    const hasHalfStar = rating % 1 !== 0

    for (let i = 0; i < fullStars; i++) {
      stars.push(
        <Star key={i} className="w-4 h-4 fill-yellow-400 text-yellow-400" />
      )
    }

    if (hasHalfStar) {
      stars.push(
        <Star key="half" className="w-4 h-4 fill-yellow-400/50 text-yellow-400" />
      )
    }

    const emptyStars = 5 - Math.ceil(rating)
    for (let i = 0; i < emptyStars; i++) {
      stars.push(
        <Star key={`empty-${i}`} className="w-4 h-4 text-gray-300" />
      )
    }

    return stars
  }

  return (
    <Link
      to={`/profile/${profile.id}`}
      className="card hover:shadow-lg transition-shadow duration-200 block"
    >
      <div className="flex items-start justify-between">
        <div className="flex-1">
          <h3 className="text-lg font-semibold text-gray-900 mb-2">
            {profile.name}
          </h3>
          
          <div className="flex items-center text-gray-600 mb-2">
            <GraduationCap className="w-4 h-4 mr-2" />
            <span className="text-sm">{profile.school}</span>
          </div>
          
          <div className="flex items-center text-gray-600 mb-3">
            <MapPin className="w-4 h-4 mr-2" />
            <span className="text-sm">{profile.location}</span>
          </div>
        </div>
      </div>

      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-1">
          {renderStars(profile.averageRating)}
          <span className="ml-2 text-sm text-gray-600">
            {profile.averageRating.toFixed(1)}
          </span>
        </div>
        
        <div className="text-sm text-gray-500">
          {profile.reviewCount} review{profile.reviewCount !== 1 ? 's' : ''}
        </div>
      </div>
    </Link>
  )
}

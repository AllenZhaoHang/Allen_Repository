import { useState } from 'react'
import { Star } from 'lucide-react'

export const StarRating = ({ rating, onRatingChange, interactive = false, size = 'md' }) => {
  const [hoverRating, setHoverRating] = useState(0)

  const sizeClasses = {
    sm: 'w-4 h-4',
    md: 'w-5 h-5',
    lg: 'w-6 h-6'
  }

  const handleClick = (newRating) => {
    if (interactive && onRatingChange) {
      onRatingChange(newRating)
    }
  }

  const handleMouseEnter = (newRating) => {
    if (interactive) {
      setHoverRating(newRating)
    }
  }

  const handleMouseLeave = () => {
    if (interactive) {
      setHoverRating(0)
    }
  }

  const displayRating = hoverRating || rating

  return (
    <div className="flex items-center space-x-1">
      {[1, 2, 3, 4, 5].map((star) => (
        <button
          key={star}
          type={interactive ? 'button' : undefined}
          onClick={() => handleClick(star)}
          onMouseEnter={() => handleMouseEnter(star)}
          onMouseLeave={handleMouseLeave}
          disabled={!interactive}
          className={`
            ${interactive ? 'cursor-pointer' : 'cursor-default'}
            ${sizeClasses[size]}
            transition-colors duration-150
          `}
        >
          <Star
            className={`
              ${sizeClasses[size]}
              ${
                star <= displayRating
                  ? 'fill-yellow-400 text-yellow-400'
                  : 'text-gray-300'
              }
            `}
          />
        </button>
      ))}
    </div>
  )
}

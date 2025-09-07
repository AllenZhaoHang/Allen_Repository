import { StarRating } from './StarRating'

export const ReviewCard = ({ review }) => {
  const formatDate = (dateString) => {
    const date = new Date(dateString)
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    })
  }

  return (
    <div className="bg-white border border-gray-200 rounded-lg p-4">
      <div className="flex items-start justify-between mb-3">
        <div className="flex items-center space-x-2">
          <div className="w-8 h-8 bg-gray-300 rounded-full flex items-center justify-center">
            <span className="text-gray-600 text-sm font-medium">A</span>
          </div>
          <div>
            <div className="text-sm font-medium text-gray-900">Anonymous</div>
            <div className="text-xs text-gray-500">{formatDate(review.created_at)}</div>
          </div>
        </div>
        <StarRating rating={review.rating} size="sm" />
      </div>
      
      {review.comment && (
        <p className="text-gray-700 text-sm leading-relaxed">
          {review.comment}
        </p>
      )}
    </div>
  )
}

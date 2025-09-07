import { useState } from 'react'
import { StarRating } from './StarRating'
import { useAuth } from '../contexts/AuthContext'

export const ReviewForm = ({ profileId, onReviewAdded }) => {
  const [rating, setRating] = useState(0)
  const [comment, setComment] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const { user } = useAuth()

  const handleSubmit = async (e) => {
    e.preventDefault()
    
    if (!user) {
      setError('You must be logged in to leave a review')
      return
    }

    if (rating === 0) {
      setError('Please select a rating')
      return
    }

    if (!comment.trim()) {
      setError('Please write a comment')
      return
    }

    setLoading(true)
    setError('')

    try {
      const { apiClient } = await import('../utils/api')
      await apiClient.createReview(profileId, rating, comment.trim())
      
      // Reset form
      setRating(0)
      setComment('')
      
      // Notify parent component
      if (onReviewAdded) {
        onReviewAdded()
      }
    } catch (err) {
      setError(err.message || 'Failed to submit review')
    } finally {
      setLoading(false)
    }
  }

  if (!user) {
    return (
      <div className="bg-gray-50 border border-gray-200 rounded-lg p-6 text-center">
        <p className="text-gray-600 mb-4">
          You need to be logged in to leave a review.
        </p>
        <a href="/login" className="btn-primary">
          Login to Review
        </a>
      </div>
    )
  }

  return (
    <div className="bg-white border border-gray-200 rounded-lg p-6">
      <h3 className="text-lg font-semibold text-gray-900 mb-4">
        Write a Review
      </h3>
      
      <form onSubmit={handleSubmit} className="space-y-4">
        {error && (
          <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg">
            {error}
          </div>
        )}
        
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Rating
          </label>
          <StarRating
            rating={rating}
            onRatingChange={setRating}
            interactive={true}
            size="lg"
          />
        </div>
        
        <div>
          <label htmlFor="comment" className="block text-sm font-medium text-gray-700 mb-2">
            Comment
          </label>
          <textarea
            id="comment"
            value={comment}
            onChange={(e) => setComment(e.target.value)}
            rows={4}
            className="input-field"
            placeholder="Share your experience..."
            maxLength={1000}
          />
          <div className="text-xs text-gray-500 mt-1">
            {comment.length}/1000 characters
          </div>
        </div>
        
        <button
          type="submit"
          disabled={loading || rating === 0 || !comment.trim()}
          className="btn-primary w-full disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {loading ? 'Submitting...' : 'Submit Review'}
        </button>
      </form>
    </div>
  )
}

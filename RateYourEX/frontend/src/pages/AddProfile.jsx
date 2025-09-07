import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { ArrowLeft, User, GraduationCap, MapPin } from 'lucide-react'
import { useAuth } from '../contexts/AuthContext'
import { apiClient } from '../utils/api'

export const AddProfile = () => {
  const [formData, setFormData] = useState({
    name: '',
    school: '',
    location: ''
  })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const { user } = useAuth()
  const navigate = useNavigate()

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: value
    }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    
    if (!user) {
      setError('You must be logged in to add a profile')
      return
    }

    if (!formData.name.trim() || !formData.school.trim() || !formData.location.trim()) {
      setError('All fields are required. For school/university/company, enter "N/A" if not applicable.')
      return
    }

    setLoading(true)
    setError('')

    try {
      const data = await apiClient.createProfile(
        formData.name.trim(),
        formData.school.trim(),
        formData.location.trim()
      )
      
      // Redirect to the new profile
      navigate(`/profile/${data.profile.id}`)
    } catch (err) {
      setError(err.message || 'Failed to create profile')
    } finally {
      setLoading(false)
    }
  }

  if (!user) {
    return (
      <div className="max-w-2xl mx-auto">
        <div className="text-center py-12">
          <div className="bg-yellow-50 border border-yellow-200 text-yellow-700 px-4 py-3 rounded-lg max-w-md mx-auto mb-6">
            You need to be logged in to add a profile.
          </div>
          <a href="/login" className="btn-primary">
            Login to Continue
          </a>
        </div>
      </div>
    )
  }

  return (
    <div className="max-w-2xl mx-auto">
      {/* Back Button */}
      <button
        onClick={() => navigate('/')}
        className="inline-flex items-center space-x-2 text-gray-600 hover:text-primary-600 mb-6"
      >
        <ArrowLeft className="w-4 h-4" />
        <span>Back to profiles</span>
      </button>

      {/* Header */}
      <div className="text-center mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-4">
          Add a New Profile
        </h1>
        <p className="text-gray-600">
          Share information about someone to help others make informed decisions. Include school, university, or company information when available.
        </p>
      </div>

      {/* Form */}
      <div className="card">
        <form onSubmit={handleSubmit} className="space-y-6">
          {error && (
            <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg">
              {error}
            </div>
          )}

          <div>
            <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-2">
              <User className="w-4 h-4 inline mr-2" />
              Full Name
            </label>
            <input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              className="input-field"
              placeholder="Enter the person's full name"
              required
            />
          </div>

          <div>
            <label htmlFor="school" className="block text-sm font-medium text-gray-700 mb-2">
              <GraduationCap className="w-4 h-4 inline mr-2" />
              School/University/Company
            </label>
            <input
              type="text"
              id="school"
              name="school"
              value={formData.school}
              onChange={handleChange}
              className="input-field"
              placeholder="Enter school, university, or company name (or N/A if not applicable)"
              required
            />
            <p className="text-xs text-gray-500 mt-1">
              If not applicable, please enter "N/A"
            </p>
          </div>

          <div>
            <label htmlFor="location" className="block text-sm font-medium text-gray-700 mb-2">
              <MapPin className="w-4 h-4 inline mr-2" />
              Location
            </label>
            <input
              type="text"
              id="location"
              name="location"
              value={formData.location}
              onChange={handleChange}
              className="input-field"
              placeholder="Enter city, state or general location"
              required
            />
          </div>

          <div className="flex space-x-4">
            <button
              type="button"
              onClick={() => navigate('/')}
              className="flex-1 btn-secondary"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={loading}
              className="flex-1 btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? 'Creating...' : 'Create Profile'}
            </button>
          </div>
        </form>
      </div>

      {/* Guidelines */}
      <div className="mt-8 bg-blue-50 border border-blue-200 rounded-lg p-6">
        <h3 className="text-lg font-semibold text-blue-900 mb-3">
          Guidelines
        </h3>
        <ul className="text-blue-800 space-y-2 text-sm">
          <li>• Only add profiles for people you have personal experience with</li>
          <li>• Be respectful and constructive in your reviews</li>
          <li>• All reviews are anonymous to protect privacy</li>
          <li>• Focus on factual experiences rather than personal opinions</li>
          <li>• For school/university/company, enter "N/A" if not applicable</li>
          <li>• Remember that this information will be public</li>
        </ul>
      </div>
    </div>
  )
}

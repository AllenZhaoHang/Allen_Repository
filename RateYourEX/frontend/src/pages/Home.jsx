import { useState, useEffect } from 'react'
import { Search, Plus } from 'lucide-react'
import { Link } from 'react-router-dom'
import { useAuth } from '../contexts/AuthContext'
import { apiClient } from '../utils/api'
import { ProfileCard } from '../components/ProfileCard'

export const Home = () => {
  const [profiles, setProfiles] = useState([])
  const [loading, setLoading] = useState(true)
  const [searchTerm, setSearchTerm] = useState('')
  const [error, setError] = useState('')
  const { user } = useAuth()

  const fetchProfiles = async (search = '') => {
    try {
      setLoading(true)
      const data = await apiClient.getProfiles(search)
      setProfiles(data.profiles)
      setError('')
    } catch (err) {
      setError('Failed to load profiles')
      console.error('Error fetching profiles:', err)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchProfiles()
  }, [])

  const handleSearch = (e) => {
    e.preventDefault()
    fetchProfiles(searchTerm)
  }

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value)
    if (e.target.value === '') {
      fetchProfiles()
    }
  }

  return (
    <div className="max-w-6xl mx-auto">
      {/* Hero Section */}
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold text-gray-900 mb-4">
          Rate Your EX
        </h1>
        <p className="text-xl text-gray-600 mb-8">
          Share your experiences and help others make informed decisions
        </p>
        
        {/* Search Bar */}
        <form onSubmit={handleSearch} className="max-w-2xl mx-auto">
          <div className="relative">
            <input
              type="text"
              value={searchTerm}
              onChange={handleSearchChange}
              placeholder="Search by name, school, university, or company..."
              className="w-full px-4 py-3 pl-12 pr-4 text-lg border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
            />
            <Search className="absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
          </div>
        </form>
      </div>

      {/* Add Profile CTA */}
      {user && (
        <div className="mb-8 text-center">
          <Link
            to="/add-profile"
            className="inline-flex items-center space-x-2 btn-primary"
          >
            <Plus className="w-5 h-5" />
            <span>Add a Profile</span>
          </Link>
        </div>
      )}

      {/* Profiles Grid */}
      {loading ? (
        <div className="flex justify-center items-center py-12">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
        </div>
      ) : error ? (
        <div className="text-center py-12">
          <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg max-w-md mx-auto">
            {error}
          </div>
        </div>
      ) : profiles.length === 0 ? (
        <div className="text-center py-12">
          <div className="text-gray-500 text-lg mb-4">
            {searchTerm ? 'No profiles found matching your search.' : 'No profiles available yet.'}
          </div>
          {user && !searchTerm && (
            <Link to="/add-profile" className="btn-primary">
              Be the first to add a profile
            </Link>
          )}
        </div>
      ) : (
        <>
          <div className="mb-6">
            <h2 className="text-2xl font-semibold text-gray-900">
              {searchTerm ? `Search Results (${profiles.length})` : 'All Profiles'}
            </h2>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {profiles.map((profile) => (
              <ProfileCard key={profile.id} profile={profile} />
            ))}
          </div>
        </>
      )}

      {/* Login Prompt */}
      {!user && (
        <div className="mt-12 text-center">
          <div className="bg-blue-50 border border-blue-200 rounded-lg p-6 max-w-2xl mx-auto">
            <h3 className="text-lg font-semibold text-blue-900 mb-2">
              Want to add a profile or leave a review?
            </h3>
            <p className="text-blue-700 mb-4">
              Sign up for a free account to start sharing your experiences.
            </p>
            <Link to="/login" className="btn-primary">
              Get Started
            </Link>
          </div>
        </div>
      )}
    </div>
  )
}

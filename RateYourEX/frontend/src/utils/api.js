const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:3001/api'

class ApiClient {
  constructor() {
    this.baseURL = API_BASE_URL
  }

  async request(endpoint, options = {}) {
    const url = `${this.baseURL}${endpoint}`
    
    // Get token from Supabase session
    let token = null
    try {
      const { supabase } = await import('./supabase')
      const { data: { session } } = await supabase.auth.getSession()
      token = session?.access_token
      console.log('API Request - Token available:', !!token)
      console.log('API Request - Endpoint:', endpoint)
    } catch (error) {
      console.warn('Could not get Supabase session:', error)
    }
    
    const config = {
      headers: {
        'Content-Type': 'application/json',
        ...(token && { Authorization: `Bearer ${token}` }),
        ...options.headers,
      },
      ...options,
    }

    try {
      console.log('Making API request to:', url)
      const response = await fetch(url, config)
      const data = await response.json()

      if (!response.ok) {
        console.error('API Error Response:', data)
        throw new Error(data.error || 'Request failed')
      }

      return data
    } catch (error) {
      console.error('API request failed:', error)
      throw error
    }
  }

  // Auth endpoints
  async register(email, password) {
    return this.request('/auth/register', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    })
  }

  async login(email, password) {
    return this.request('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    })
  }

  async logout() {
    return this.request('/auth/logout', {
      method: 'POST',
    })
  }

  async getCurrentUser() {
    return this.request('/auth/me')
  }

  // Profile endpoints
  async getProfiles(search = '', page = 1, limit = 20) {
    const params = new URLSearchParams({ page, limit })
    if (search) params.append('search', search)
    
    return this.request(`/profiles?${params}`)
  }

  async getProfile(id) {
    return this.request(`/profiles/${id}`)
  }

  async createProfile(name, school, location) {
    return this.request('/profiles', {
      method: 'POST',
      body: JSON.stringify({ name, school, location }),
    })
  }

  // Review endpoints
  async getReviews(profileId, page = 1, limit = 20) {
    const params = new URLSearchParams({ page, limit })
    return this.request(`/profiles/${profileId}/reviews?${params}`)
  }

  async createReview(profileId, rating, comment) {
    return this.request(`/profiles/${profileId}/reviews`, {
      method: 'POST',
      body: JSON.stringify({ rating, comment }),
    })
  }
}

export const apiClient = new ApiClient()

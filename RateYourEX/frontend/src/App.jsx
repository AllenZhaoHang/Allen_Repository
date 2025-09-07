import { Routes, Route } from 'react-router-dom'
import { AuthProvider } from './contexts/AuthContext'
import { Navbar } from './components/Navbar'
import { Home } from './pages/Home'
import { Profile } from './pages/Profile'
import { Login } from './pages/Login'
import { AddProfile } from './pages/AddProfile'
import { Settings } from './pages/Settings'

function App() {
  return (
    <AuthProvider>
      <div className="min-h-screen bg-gray-50">
        <Navbar />
        <main className="container mx-auto px-4 py-8">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/profile/:id" element={<Profile />} />
            <Route path="/login" element={<Login />} />
            <Route path="/add-profile" element={<AddProfile />} />
            <Route path="/settings" element={<Settings />} />
          </Routes>
        </main>
      </div>
    </AuthProvider>
  )
}

export default App

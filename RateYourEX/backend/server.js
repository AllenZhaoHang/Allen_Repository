// server.js
const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
require('dotenv').config();

const profileRoutes = require('./routes/profiles');
const reviewRoutes = require('./routes/reviews');
const authRoutes = require('./routes/auth');

const app = express();
const PORT = process.env.PORT || 3001;

// --------------------- Trust Proxy ---------------------
// 必须在 rateLimit 之前设置
// Render、Heroku 等云平台会在请求头里加 X-Forwarded-For
app.set('trust proxy', 1);

// --------------------- Security Middleware ---------------------
app.use(helmet());

// --------------------- Rate Limiting ---------------------
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100,
  message: 'Too many requests from this IP, please try again later.'
});
app.use(limiter);

// --------------------- CORS ---------------------
app.use(cors({
  origin: process.env.FRONTEND_URL || 'http://localhost:5173',
  credentials: true,
  allowedHeaders: ['Content-Type', 'Authorization'],
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
}));
app.options('*', cors());

// --------------------- Body Parsing ---------------------
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true }));

// --------------------- Routes ---------------------
app.use('/api/auth', authRoutes);
app.use('/api/profiles', profileRoutes);
app.use('/api/reviews', reviewRoutes);

app.get('/api/health', (req, res) => {
  res.json({ status: 'OK', timestamp: new Date().toISOString() });
});

// --------------------- Error Handling ---------------------
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ 
    error: 'Something went wrong!',
    message: process.env.NODE_ENV === 'development' ? err.message : 'Internal server error'
  });
});

// 404 handler
app.use('*', (req, res) => {
  res.status(404).json({ error: 'Route not found' });
});

// --------------------- Start Server ---------------------
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log(`Environment: ${process.env.NODE_ENV || 'development'}`);
});

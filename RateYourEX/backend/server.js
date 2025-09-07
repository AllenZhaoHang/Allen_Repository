// server.js
const express = require('express');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const cors = require('cors');
require('dotenv').config();

const profileRoutes = require('./routes/profiles');
const reviewRoutes = require('./routes/reviews');
const authRoutes = require('./routes/auth');

const app = express();
const PORT = process.env.PORT || 3001;

// --------------------- Trust Proxy ---------------------
// Render / Heroku 等云平台请求头里会有 X-Forwarded-For
app.set('trust proxy', 1);

// --------------------- Security Middleware ---------------------
app.use(helmet());

// --------------------- Rate Limiting ---------------------
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100,
  standardHeaders: true,
  legacyHeaders: false,
  message: 'Too many requests from this IP, please try again later.'
});
app.use(limiter);

// --------------------- CORS ---------------------
// Method 2: Development - allow all origins
app.use(cors({
  origin: '*', // allow all domains
  credentials: true,
  allowedHeaders: ['Authorization', 'Content-Type'],
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
}));

app.options('*', cors()); // support preflight requests

// --------------------- Body Parsing ---------------------
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true }));

// --------------------- Routes ---------------------
app.use('/api/auth', authRoutes);
app.use('/api/profiles', profileRoutes);
app.use('/api/reviews', reviewRoutes);

// Health check
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

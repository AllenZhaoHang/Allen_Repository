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
// Render 等平台会在请求头里加 X-Forwarded-For
app.set('trust proxy', 1);

// --------------------- Security Middleware ---------------------
app.use(helmet());

// --------------------- Rate Limiting ---------------------
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 分钟
  max: 100,
  standardHeaders: true,
  legacyHeaders: false,
  message: 'Too many requests from this IP, please try again later.'
});
app.use(limiter);

// --------------------- CORS ---------------------
// 方法一：允许多个前端域名（包括 Vercel Preview 动态 URL）
const allowedOrigins = [
  process.env.FRONTEND_URL, // 主前端 URL，例如 https://rateyourexfrontend.vercel.app
  process.env.FRONTEND_URL_ALT // 可选备用 URL
];

app.use(cors({
  origin: function(origin, callback) {
    if (!origin) return callback(null, true); // Postman/curl 等没有 origin
    if (allowedOrigins.includes(origin)) return callback(null, true);
    // 支持 Vercel Preview URL 动态域名
    if (/^https:\/\/rateyourexfrontend-.*\.vercel\.app$/.test(origin)) return callback(null, true);

    return callback(new Error('Not allowed by CORS'), false);
  },
  credentials: true,
  allowedHeaders: ['Content-Type', 'Authorization'],
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
}));

app.options('*', cors()); // 支持预检请求

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

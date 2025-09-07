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
app.set('trust proxy', 1); // 添加这一行解决 Render X-Forwarded-For 报错

// --------------------- Security Middleware ---------------------
app.use(helmet());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  message: 'Too many requests from this IP, please try again later.'
});
app.use(limiter);

// ... 后续 CORS、body parser、routes 等保持不变

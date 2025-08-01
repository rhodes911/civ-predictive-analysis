# Superset Configuration for Civ VI Analytics
# This configuration sets up Superset to work with our PostgreSQL database

import os

# Database Configuration - using environment variables
DATABASE_USER = os.environ.get('DATABASE_USER', 'civ6_user')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'civ6_password')
DATABASE_HOST = os.environ.get('DATABASE_HOST', 'postgres')
DATABASE_DB = os.environ.get('DATABASE_DB', 'civ6_analytics')

SQLALCHEMY_DATABASE_URI = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:5432/{DATABASE_DB}'

# Security Configuration
SECRET_KEY = os.environ.get('SUPERSET_SECRET_KEY', 'this_is_a_very_long_jwt_secret_key_for_civ6_local_development_definitely_more_than_32_bytes_long_12345')

# Disable JWT for local development
WTF_CSRF_ENABLED = False
JWT_SECRET_KEY = SECRET_KEY

# Feature Flags
FEATURE_FLAGS = {
    'DASHBOARD_NATIVE_FILTERS': True,
    'DASHBOARD_CROSS_FILTERS': True,
    'GLOBAL_ASYNC_QUERIES': False,  # Disable async queries for local development
}

# Cache Configuration (Redis not needed for local setup)
CACHE_CONFIG = {
    'CACHE_TYPE': 'SimpleCache',
    'CACHE_DEFAULT_TIMEOUT': 300
}

# Email Configuration (disabled for local setup)
SMTP_HOST = None
SMTP_STARTTLS = False
SMTP_SSL = False

# CSV Export
CSV_EXPORT = {
    'encoding': 'utf-8',
}

# Webdriver Configuration (for screenshots/alerts - optional)
WEBDRIVER_TYPE = None

# Logging
import logging
LOG_LEVEL = logging.INFO

# Authentication
AUTH_TYPE = 1  # Database authentication
AUTH_ROLE_ADMIN = 'Admin'
AUTH_ROLE_PUBLIC = 'Public'

# Allow embedding (for potential iframe usage)
HTTP_HEADERS = {'X-Frame-Options': 'ALLOWALL'}

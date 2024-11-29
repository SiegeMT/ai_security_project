"""
Constants module for the AI Security Platform.
Values that should not be configurable at runtime.
"""
from enum import Enum
from typing import Dict, Set

class LogLevel(str, Enum):
    """Valid logging levels."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class Environment(str, Enum):
    """Valid deployment environments."""
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"

# Security Constants
REQUIRED_PERMISSIONS: Set[str] = {
    "read_logs",
    "write_logs",
    "manage_users",
    "view_dashboard",
    "manage_system"
}

AUTH_HEADER: str = "X-Security-Token"
TOKEN_EXPIRY: int = 86400  # 24 hours in seconds

# API Rate Limits (requests per minute)
RATE_LIMITS: Dict[str, int] = {
    "default": 60,
    "log_ingestion": 1000,
    "query": 120,
    "user_management": 30
}

# Database Constants
MAX_CONNECTIONS: int = 100
CONNECTION_TIMEOUT: int = 30  # seconds
MAX_VECTOR_DIMENSION: int = 2048

# AI Model Constants
MODEL_VERSION_FORMAT: str = "v{major}.{minor}.{patch}"
SUPPORTED_EMBEDDING_MODELS: Set[str] = {
    "all-MiniLM-L6-v2",
    "all-mpnet-base-v2",
    "all-MiniLM-L12-v2"
}

# Monitoring Constants
METRICS_UPDATE_INTERVAL: int = 15  # seconds
HEALTH_CHECK_INTERVAL: int = 60  # seconds
BACKUP_RETENTION_DAYS: int = 30

# File Paths
DEFAULT_CONFIG_PATH: str = "/etc/ai_security/config.yaml"
DEFAULT_LOG_DIR: str = "/var/log/ai_security"
MODEL_CACHE_DIR: str = "/var/cache/ai_security/models"

# HTTP Status Codes (commonly used)
class StatusCode:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    RATE_LIMITED = 429
    SERVER_ERROR = 500
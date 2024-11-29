"""
Core configuration module using Param for the AI Security Platform.
Implements a hierarchical configuration system with security-first approach.
"""
import param
from pathlib import Path
from typing import Optional, Dict, Any

class SecurityConfig(param.Parameterized):
    """Security-related configuration parameters."""
    
    hsm_enabled = param.Boolean(default=True, doc="Enable Hardware Security Module integration")
    hsm_library_path = param.String(default="/usr/lib/softhsm/libsofthsm2.so", doc="Path to HSM PKCS#11 library")
    hsm_slot_id = param.Integer(default=0, bounds=(0, None), doc="HSM slot ID")
    
    ssl_cert_path = param.String(default=None, allow_None=True, doc="Path to SSL certificate")
    ssl_key_path = param.String(default=None, allow_None=True, doc="Path to SSL private key")
    
    session_timeout = param.Integer(default=3600, bounds=(300, 86400), 
                                  doc="Session timeout in seconds (5 min to 24 hours)")

class DatabaseConfig(param.Parameterized):
    """Database configuration parameters."""
    
    host = param.String(default="localhost", doc="Database host")
    port = param.Integer(default=5432, bounds=(1, 65535), doc="Database port")
    name = param.String(default="ai_security_db", doc="Database name")
    user = param.String(default=None, allow_None=True, doc="Database user")
    password = param.String(default=None, allow_None=True, doc="Database password")
    
    vector_dimension = param.Integer(default=768, bounds=(64, 2048), 
                                   doc="Dimension for vector embeddings")

class AIConfig(param.Parameterized):
    """AI model and processing configuration."""
    
    model_path = param.String(default="models/anomaly_detector", doc="Path to AI model directory")
    batch_size = param.Integer(default=32, bounds=(1, 512), doc="Batch size for inference")
    threshold = param.Number(default=0.85, bounds=(0, 1), doc="Anomaly detection threshold")
    
    embedding_model = param.String(default="all-MiniLM-L6-v2", doc="Model name for embeddings")
    update_frequency = param.Integer(default=3600, bounds=(60, 86400), 
                                   doc="Model update frequency in seconds")

class LoggingConfig(param.Parameterized):
    """Logging and monitoring configuration."""
    
    log_level = param.String(default="INFO", doc="Logging level")
    log_path = param.String(default="logs/ai_security.log", doc="Path to log file")
    
    enable_monitoring = param.Boolean(default=True, doc="Enable system monitoring")
    metrics_port = param.Integer(default=9090, bounds=(1024, 65535), 
                               doc="Metrics server port")

class AppConfig(param.Parameterized):
    """Main application configuration."""
    
    security = param.ClassSelector(class_=SecurityConfig, default=SecurityConfig(), 
                                 doc="Security configuration")
    database = param.ClassSelector(class_=DatabaseConfig, default=DatabaseConfig(), 
                                 doc="Database configuration")
    ai = param.ClassSelector(class_=AIConfig, default=AIConfig(), 
                           doc="AI configuration")
    logging = param.ClassSelector(class_=LoggingConfig, default=LoggingConfig(), 
                                doc="Logging configuration")
    
    debug_mode = param.Boolean(default=False, doc="Enable debug mode")
    environment = param.String(default="production", doc="Deployment environment")
    
    @property
    def as_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary format."""
        return {
            "security": self.security.param.get_param_values(),
            "database": self.database.param.get_param_values(),
            "ai": self.ai.param.get_param_values(),
            "logging": self.logging.param.get_param_values(),
            "debug_mode": self.debug_mode,
            "environment": self.environment
        }
    
    def validate(self) -> None:
        """Validate configuration settings."""
        if self.environment == "production":
            assert not self.debug_mode, "Debug mode cannot be enabled in production"
            assert self.security.hsm_enabled, "HSM must be enabled in production"
            assert self.security.ssl_cert_path, "SSL certificate required in production"
            assert self.security.ssl_key_path, "SSL key required in production"
        
        # Validate paths exist
        if self.security.ssl_cert_path:
            assert Path(self.security.ssl_cert_path).exists(), "SSL certificate not found"
        if self.security.ssl_key_path:
            assert Path(self.security.ssl_key_path).exists(), "SSL key not found"
        
        # Validate HSM configuration
        if self.security.hsm_enabled:
            assert Path(self.security.hsm_library_path).exists(), "HSM library not found"

# Create default configuration instance
config = AppConfig()
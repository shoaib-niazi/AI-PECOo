"""
Configuration module for AI-PECO application
"""
from pydantic_settings import BaseSettings
from pydantic import field_validator
from typing import Optional, List
import os


class Settings(BaseSettings):
    # Application
    APP_NAME: str = "AI-PECO"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # Database
    MONGODB_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "aipeco_db"
    
    # JWT
    SECRET_KEY: str = "change_me_in_production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS — stored as comma-separated string in .env
    CORS_ORIGINS: str = "http://localhost:3000,http://localhost:5173,https://ai-peco.vercel.app"
    
    # ESP32 / device API
    ESP32_POLLING_INTERVAL: int = 5  # seconds
    DATA_RETENTION_DAYS: int = 30
    DEVICE_API_KEY: Optional[str] = None
    
    # Energy Settings
    ENERGY_PRICE_PER_UNIT: float = 50  # PKR per unit
    ANOMALY_THRESHOLD_SIGMA: float = 2.0
    
    # Demo mode (when ESP32 hardware is not connected)
    DEMO_MODE: bool = True

    # Features
    ENABLE_AI_PREDICTIONS: bool = True
    ENABLE_AUTO_ALERTS: bool = True

    @property
    def cors_origins_list(self) -> List[str]:
        """Return CORS origins as a list."""
        return [o.strip() for o in self.CORS_ORIGINS.split(",") if o.strip()]
    
    class Config:
        env_file = ".env"
        extra = "ignore"


# Validate critical settings
_s = Settings()
if _s.SECRET_KEY == "change_me_in_production":
    import warnings
    warnings.warn("SECRET_KEY is using default value. Set it in .env for production.")

settings = _s
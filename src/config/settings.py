"""
Configuraciones de la aplicación.
"""
from pydantic_settings import BaseSettings
from typing import List, Union
from functools import lru_cache
import os

class Settings(BaseSettings):
    # Servidor
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    
    # Límites y parámetros
    MAX_IMAGE_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS: Union[str, List[str]] = "jpg,jpeg,png,bmp,tiff"
    MAX_WIDTH: int = 2048
    MAX_HEIGHT: int = 2048
    # Seguridad
    API_KEY_HEADER: str = "X-API-Key"
    DEFAULT_API_KEY: str = "development_key_change_me"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Convertir ALLOWED_EXTENSIONS de string a lista si es necesario
        if isinstance(self.ALLOWED_EXTENSIONS, str):
            self.ALLOWED_EXTENSIONS = [ext.strip() for ext in self.ALLOWED_EXTENSIONS.split(',')]
    
    model_config = {
        "env_file": ".env",
        "case_sensitive": True
    }

@lru_cache()
def get_settings() -> Settings:
    """
    Carga las configuraciones desde variables de entorno o archivo .env
    con caché LRU para optimizar el rendimiento.
    
    Returns:
        Objeto Settings con la configuración
    """
    return Settings()

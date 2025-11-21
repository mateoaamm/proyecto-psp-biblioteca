"""
Configuración de la aplicación
"""
import os

class Config:
    """Configuración base"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-mateo-2025'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///biblioteca.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuración de préstamos
    DIAS_PRESTAMO = 7
    MULTA_POR_DIA = 1000
    MAX_PRESTAMOS_SIMULTANEOS = 3

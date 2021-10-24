# config.py
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:passw0rd@localhost:3306/test'
    SQLALCHEMY_ECHO = True
    JWT_SECRET_KEY = "secret-key"

class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://test:passw0rd@10.131.0.177:3306/sampledb'
    SQLALCHEMY_ECHO = True
    JWT_SECRET_KEY = "secret-key"

config_options = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

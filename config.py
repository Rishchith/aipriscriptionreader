from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    # Database Settings
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
    
    # API Keys
    GOOGLE_MAPS_KEY = os.getenv('GOOGLE_MAPS_KEY')
    OPENAI_KEY = os.getenv('OPENAI_KEY')
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
    CDC_API_KEY = os.getenv('CDC_API_KEY')
    
    # Model Paths
    MODEL_DIR = os.path.join(os.path.dirname(__file__), '../static/models')
    VOICE_MODEL = os.path.join(MODEL_DIR, 'voice_analysis')
    FACE_MODEL = os.path.join(MODEL_DIR, 'face_analysis')
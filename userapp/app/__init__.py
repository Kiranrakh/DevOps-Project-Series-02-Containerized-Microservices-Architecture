from flask import Flask
from redis import Redis
#from userapp.app.config import Config
from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    try:
        app.redis = Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, decode_responses=True)
        app.redis.ping()
        print("✅ Redis connected.")
    except Exception as e:
        app.redis = None
        print(f"⚠️ Redis not available: {e}")

    from .routes import register_routes
    register_routes(app)

    return app

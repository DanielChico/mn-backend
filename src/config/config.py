import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    API_VERSION = os.getenv('API_VERSION')
    API_PREFIX = f"/api/{API_VERSION}"
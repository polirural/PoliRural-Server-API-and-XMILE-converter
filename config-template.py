import os 
APP_BASE_PATH = "/"

# Connection string
SQLALCHEMY_CONNSTR = "sqlite:///../../db/polirural.sqlite"

# Define path directory for models
MODEL_PATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'models')

# Setup serving of static files, if any
STATIC_PATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'static')
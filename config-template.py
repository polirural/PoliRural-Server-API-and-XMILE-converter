from os.path import dirname, join, abspath

# Base path that the app is served from
APP_BASE_PATH = "/"

# Connection string
SQLALCHEMY_CONNSTR = "sqlite:///%s" % (join(dirname(
    abspath(__file__)), 'db/polirural.sqlite'))

# Define path directory for models
MODEL_PATH = join(dirname(
    abspath(__file__)), 'models')

# Setup serving of static files, if any
STATIC_PATH = join(dirname(
    abspath(__file__)), 'static')
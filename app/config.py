from secrets import token_urlsafe

from environs import Env

env = Env()
env.read_env()


SECRET_KEY = env.str("SECRET_KEY", token_urlsafe(50))
DEBUG = env.bool("FLASK_DEBUG", default=False)

import os

# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xa1\xc74jhw\xce\x88]\xf42`\xdbX\x0c\x1d\x8en_\x8b\x03\xf2GJ'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False

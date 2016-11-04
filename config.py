import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """ Models the applicatiom configuration """

    DEBUG = False
    TESTING = False

    #SqlAlchemy
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
        'd57a322c-4fc1-4421-9155-9cfbb35f2baa'

    CSRF_SESSION_KEY = os.environ.get('CSRF_SESSION_KEY') or \
        '91c1dde9-bbd0-4cee-b2a6-ad4c4ab02818'

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    CSRF_ENABLED = True

    #Keep track of the life time of am mail
    TRACK_EVENTS = True

    # For production use Redis, Memcached, filesystem cache
    CACHE_TYPE = os.environ.get('CACHE_TYPE')

    #Celery, use Redis by default
    CELERY_ENABLE = True
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL') or\
        'redis://localhost:6379/0' 
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND') or \
        'redis://localhost:6379/0'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    """ The development configuration. """

    DEBUG = True
    CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

    CACHE_TYPE = 'simple'

class ProductionConfig(Config):
    """ The production configuration. """

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class TestingConfig(Config):
    """ The test configuration. """

    TESTING = True
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

    CACHE_TYPE = 'simple'
    CELERY_ENABLE = False
    TRACK_EVENTS = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
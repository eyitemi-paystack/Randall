from . import get_env

class EnvConfig(object):
    """Parent Configuration class """
    DEBUG = False
    FLASK_APP= 'randall'
    CSRF_ENABLED = True
    SECRET = get_env('SECRET')


class DevelopmentEnv(EnvConfig):
    """Configurations for Development."""
    DEBUG = True 


class TestingEnv(EnvConfig):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True


class StagingEnv(EnvConfig):
    """Configurations for Staging."""
    DEBUG = True


class ProductionEnv(EnvConfig):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False



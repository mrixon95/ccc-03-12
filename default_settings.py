import os
# We are going to have different configuration variables depending on whether
# whether we are in a testing, development or production environment

# We want a different db connection depending on whether we are testing or we are in development

# Robust configuration
class Config(object):
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.getenv("DB_URI")
        if not value:
            raise ValueError("DB_URI is not set")

        return value



# Inherit from Config
class DevelopmentConfig(Config):
    # Development environment specific configuration
    DEBUG = True

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True

environment = os.getenv("FLASK_ENV")

# Change the configurations depending on our Flask env

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()

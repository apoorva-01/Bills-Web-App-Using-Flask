import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'juejnrg!9m@fnjnj%^&*09844'
    # SESSION_TYPE = 'redis'
    SESSION_TYPE = 'filesystem'
    # Mail Configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'main.hu.demo@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'merkonhipta'
    BILL_MAIL_SUBJECT_PREFIX = 'Bills Reminder'
    BILL_MAIL_SENDER = 'Set & Get  <main.hu.demo@gmail.com>'
    FLASKY_MAIL_SENDER = 'Set & Get <main.hu.demo@gmail.com>'
    FLASKY_MAIL_SUBJECT_PREFIX = 'Bills Reminder'

    BILL_ADMIN ='main.hu.demo@gmail.com'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    POSTS_PER_PAGE = 9
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE=9
    BILL_COMMENTS_PER_PAGE=9

    ALLOWED_EXTENSIONS = { 'jpg'}
    UPLOAD_FOLDER='C:/Users/Sourav Verma/Desktop/Flask/Bills App/app/static/img/user-profile-pic/'

    # CELERY_BROKER_URL='redis://localhost:6379/0'
    # result_backend='redis://localhost:6379/0'

   
    # DETECT_BASE_URL = 'https://google-translate1.p.rapidapi.com/language/translate/v2/detect'
    # TRANSLATE_BASE_URL = 'https://google-translate1.p.rapidapi.com/language/translate/v2'
    # HEADERS = {
    #    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    #    'x-rapidapi-key': "YOUR-VERY-OWN-RAPID-API-KEY-GOES-HERE",
    #    'content-type': "application/x-www-form-urlencoded"
    #    }



    @staticmethod
    def init_app(app):
        pass

# Database Configuration
class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Apoo124@#@localhost:5432/postgres'
    DATABASE_URL = 'postgres://bfvsltjxhtskzq:028d07027c7ca05acbd1d7ad4e65b4ccf186810b38b359bc482a46e08d2c0b66@ec2-3-217-219-146.compute-1.amazonaws.com:5432/d9vglhdsm2qkds'
    SQLALCHEMY_DATABASE_URI  = 'postgres://bfvsltjxhtskzq:028d07027c7ca05acbd1d7ad4e65b4ccf186810b38b359bc482a46e08d2c0b66@ec2-3-217-219-146.compute-1.amazonaws.com:5432/d9vglhdsm2qkds'
    

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql://postgres:Apoo124@#@localhost:5432/postgres'
class HerokuConfig(ProductionConfig):
    SSL_REDIRECT = True if os.environ.get('DYNO') else False

    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # handle reverse proxy server headers
        from werkzeug.contrib.fixers import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
    
config = {
 'development': DevelopmentConfig,
 'production': ProductionConfig,
 'default': DevelopmentConfig,
  'heroku': HerokuConfig
}



    

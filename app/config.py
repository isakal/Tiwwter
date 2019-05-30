import os


class BaseConfig(object):
	"""base config"""
	MAIL_USERNAME = os.environ['TIWWTER_MAIL']
	MAIL_PASSWORD = os.environ['TIWWTER_PASSWORD']
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_SERVER = 'smtp.gmail.com'
	DEBUG_TB_ENABLED = False
	DEBUG_TB_PROFILER_ENABLED = True
	SECRET_KEY = os.environ['TIWWTER_SECRET_KEY']
	RECAPTCHA_PUBLIC_KEY = os.environ['TIWWTER_RECAPTCHA_PUBLIC_KEY']
	RECAPTCHA_PRIVATE_KEY = os.environ['TIWWTER_RECAPTCHA_PRIVATE_KEY']


class TestingConfig(BaseConfig):
	"""testing config"""
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	DEBUG = True


class DevelopmentConfig(BaseConfig):
	"""dev config"""
	DEBUG = True
	DEBUG_TB_ENABLED = True
	DEBUG_TB_INTERCEPT_REDIRECTS = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'


class ProductionConfig(BaseConfig):
	"""production config"""
	SQLALCHEMY_DATABASE_URI = os.environ['TIWWTER_DB_URI']

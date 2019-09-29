class Configuration(object):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/flask'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'Really really really secret and long key'
	SECURITY_PASSWORD_SALT = 'Abrakadabra'
	SECURITY_PASSWORD_HASH = 'sha512_crypt'



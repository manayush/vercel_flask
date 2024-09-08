import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY' , 'y')
    #SQLALCHEMY_DATABASE_URI = ('postgresql://postgres:Ayush%40123@localhost:5432/new') 
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','postgresql://default:jQsnbc7Go3kh@ep-tiny-unit-a1my71aw-pooler.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require') 

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') 
    # or 'a_very_secret_jwt_key'



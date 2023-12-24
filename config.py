class Config:
    SECRET_KEY = 'your_secret_key'  # Change this to a secure random value
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

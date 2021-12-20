import os

APP_DIR = os.getenv('APP_DIR')

LOCATIONS_DRIVERS = f'{APP_DIR}/webdrivers_for_selenium/'

'''driver For Firefox located by default. In my way -> 
C:/Users/LegionPC/AppData/Local/Programs/Python/Python39'''

LOCATIONS_SCREENSHOTS = f'{APP_DIR}/screenshots/'

URL = os.getenv('URL')

API_URL = os.getenv('API_URL')

MODERATOR_LOGIN = os.getenv('MODER_LOGIN')

MODERATOR_PASSWORD = os.getenv('MODER_PASSWORD')

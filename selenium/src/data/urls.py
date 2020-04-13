import os
from dotenv import load_dotenv


# parent_dir = os.pardir
# print('parent_dir', parent_dir)
# path_to_env = os.path.abspath(os.path.join(os.path, os.pardir))
dotenv_path = os.getcwd() + '/.env'
print('dot_ENV', dotenv_path)

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

BASE_URL = os.getenv('BASE_URL', 'http://localhost:4100')


class URLS:
    home = f'{BASE_URL}/'
    login = f'{BASE_URL}/login'
    # login = 'http://localhost:4100'
    register = f'{BASE_URL}/register'
    editor = f'{BASE_URL}/editor'
    settings =  f'{BASE_URL}/settings',
    profile = f'{BASE_URL}/@Str1ker'  # login
    user_favorite = f'{BASE_URL}/@Str1ker/favorites'

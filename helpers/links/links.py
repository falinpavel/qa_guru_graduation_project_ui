import os

from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')


class Links:
    def __init__(self):
        self.base_url = os.getenv(key="BASE_URL", default="https://cmstore.ru/")
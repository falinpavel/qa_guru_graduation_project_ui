import os

from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')


class Links:
    def __init__(self):
        self.base_page_url: str = os.getenv(key="BASE_URL", default="https://cmstore.ru/")
        self.cart_page_url: str = "{base_page_url}personal/cart/".format(base_page_url=self.base_page_url)
        self.smartphones_page_url: str = "{base_page_url}catalog/smartfony/".format(base_page_url=self.base_page_url)

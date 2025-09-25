import os

from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')


class Links:
    def __init__(self):
        self.base_page_url = os.getenv(key="BASE_URL", default="https://cmstore.ru/")
        self.cart_page_url = "{base_page_url}personal/cart/".format(base_page_url=self.base_page_url)
        
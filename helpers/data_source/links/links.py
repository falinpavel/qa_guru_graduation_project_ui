import os

from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')


class Links:
    def __init__(self):
        self.base_url = os.getenv(key="BASE_URL", default="https://sokolov.ru/")
        self.shop_maps_url = "{base_url}shops-map/".format(base_url=self.base_url)
        self.delivery_terms_url = "{base_url}delivery-terms/".format(base_url=self.base_url)
        self.favorites_url = "{base_url}favorites/".format(base_url=self.base_url)
        self.basket_url = "{base_url}basket/".format(base_url=self.base_url)
        self.gift_card = "{base_url}gift-card/".format(base_url=self.base_url)
        self.promotions_url = "{base_url}promotions/".format(base_url=self.base_url)
        self.collections_url = "{base_url}collections/".format(base_url=self.base_url)

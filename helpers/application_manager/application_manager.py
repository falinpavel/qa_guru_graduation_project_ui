from components.header_menu.header_bottom_menu import HeaderBottomMenu
from components.header_menu.header_top_menu import HeaderTopMenu
from pages.cart_page.cart_page import CartPage
from pages.home_page.home_page import HomePage


class CmStoreApplicationManager:
    def __init__(self):
        self.header_top_menu = HeaderTopMenu()
        self.header_bottom_menu = HeaderBottomMenu()
        self.home_page = HomePage()
        self.cart_page = CartPage()


cm_store = CmStoreApplicationManager()

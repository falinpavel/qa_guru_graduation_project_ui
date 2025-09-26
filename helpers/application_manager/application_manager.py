from components.auth_modal.auth_modal import AuthModal
from components.home_page_catalog_menu.home_page_catalog_menu import CatalogMenu
from components.header_menu.header_bottom_menu import HeaderBottomMenu
from components.header_menu.header_top_menu import HeaderTopMenu
from pages.cart_page.cart_page import CartPage
from pages.catalog_pages.smartphones_page.smartphones_page import SmartphonesPage
from pages.home_page.home_page import HomePage


class CmStoreApplicationManager:
    def __init__(self):
        self.header_top_menu = HeaderTopMenu()
        self.header_bottom_menu = HeaderBottomMenu()
        self.auth_modal = AuthModal()
        self.home_page = HomePage()
        self.cart_page = CartPage()
        self.home_page_catalog_menu = CatalogMenu()
        self.smartphones_page = SmartphonesPage()


cm_store = CmStoreApplicationManager()

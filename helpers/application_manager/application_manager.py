from components.auth_modal.auth_modal import AuthModal
from components.home_page_catalog_menu.home_page_catalog_menu import CatalogMenu
from components.header_menu.header_bottom_menu import HeaderBottomMenu
from components.header_menu.header_top_menu import HeaderTopMenu
from pages.cart_page.cart_page import CartPage
from pages.home_page.home_page import HomePage


class CmStoreApplicationManager:
    def __init__(self):
        self.header_top_menu: object = HeaderTopMenu()
        self.header_bottom_menu: object = HeaderBottomMenu()
        self.auth_modal: object = AuthModal()
        self.home_page: object = HomePage()
        self.cart_page: object = CartPage()
        self.home_page_catalog_menu: object = CatalogMenu()


cm_store = CmStoreApplicationManager()

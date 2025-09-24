from components.header_menu.header_bottom_menu import HeaderBottomMenu
from components.header_menu.header_top_menu import HeaderTopMenu
from pages.home_page.home_page import HomePage


class CmStoreApplicationManager:
    def __init__(self):
        self.header_top_menu = HeaderTopMenu()
        self.header_bottom_menu = HeaderBottomMenu()
        self.home_page = HomePage()


cm_store = CmStoreApplicationManager()

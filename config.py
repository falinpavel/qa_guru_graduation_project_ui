from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def options_management(context):
    if context == "chrome_local":
        options = ChromeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-gpu")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        return options

    if context == "firefox_local":
        options = FirefoxOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--purgecaches")
        options.add_argument("--disable-gpu")
        options.set_preference(name="browser.download.folderList", value=2)
        options.set_preference(name="browser.download.manager.showWhenStarting", value=False)
        options.set_preference(name="browser.helperApps.neverAsk.saveToDisk", value="application/octet-stream")
        options.set_preference(name="browser.download.manager.useWindow", value=False)
        options.set_preference(name="browser.download.manager.focusWhenStarting", value=False)
        options.set_preference(name="browser.download.manager.showAlertOnComplete", value=False)
        options.set_preference(name="browser.download.manager.closeWhenDone", value=True)
        options.set_preference(name="permissions.default.desktop-notification", value=2)
        options.set_preference(name="browser.safebrowsing.malware.enabled", value=True)
        options.set_preference(name="browser.safebrowsing.phishing.enabled", value=True)
        options.capabilities.update(
            {
                "browserName": "firefox",
                "browserVersion": "125.0",
                "selenoid:options": {
                    "enableVideo": False
                }
            })
        return options

    if context == "chrome_selenoid":
        options = ChromeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-gpu")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.capabilities.update(
            {
                "browserName": "chrome",
                "browserVersion": "128.0",
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": True,
                    "enableLog": True
                }
            }
        )
        return options

    if context == "firefox_selenoid":
        options = FirefoxOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--purgecaches")
        options.add_argument("--disable-gpu")
        options.set_preference(name="browser.download.folderList", value=2)
        options.set_preference(name="browser.download.manager.showWhenStarting", value=False)
        options.set_preference(name="browser.helperApps.neverAsk.saveToDisk", value="application/octet-stream")
        options.set_preference(name="browser.download.manager.useWindow", value=False)
        options.set_preference(name="browser.download.manager.focusWhenStarting", value=False)
        options.set_preference(name="browser.download.manager.showAlertOnComplete", value=False)
        options.set_preference(name="browser.download.manager.closeWhenDone", value=True)
        options.set_preference(name="permissions.default.desktop-notification", value=2)
        options.set_preference(name="browser.safebrowsing.malware.enabled", value=True)
        options.set_preference(name="browser.safebrowsing.phishing.enabled", value=True)
        return options

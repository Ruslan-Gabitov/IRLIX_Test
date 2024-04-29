from selenium.webdriver.firefox.options import Options as Options_firefox
from selenium.webdriver.chrome.options import Options as Options_chrome


class ConfDrivers:
    @classmethod
    def options_chrome(cls):
        chrome_options = Options_chrome()
        chrome_options.add_argument("--window-size=1980,1080")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--headless")
        return chrome_options

    @classmethod
    def options_firefox(cls):
        firefox_options = Options_firefox()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--width=1980")
        firefox_options.add_argument("--height=1080")
        return firefox_options

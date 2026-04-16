import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest:

    def setup_method(self):

        with open("config/config.json") as f:

            config = json.load(f)

        chrome_options = Options()

        if config["headless"]:

            chrome_options.add_argument("--headless=new")

        chrome_options.add_argument("--no-sandbox")

        chrome_options.add_argument("--disable-dev-shm-usage")

        chrome_options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(

            service=Service(ChromeDriverManager().install()),

            options=chrome_options

        )

        self.driver.get(config["base_url"])


    def teardown_method(self):

        self.driver.quit()
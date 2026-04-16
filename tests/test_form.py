import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.form_page import FormPage


def load_test_data():

    with open("testdata/form_data.json") as f:

        return json.load(f)


def test_form():

    data = load_test_data()

    chrome_options = Options()

    chrome_options.add_argument("--headless=new")

    chrome_options.add_argument("--no-sandbox")

    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(

        service=Service(ChromeDriverManager().install()),

        options=chrome_options

    )

    driver.get("https://testautomationpractice.blogspot.com/")

    form = FormPage(driver)

    form.enter_name(data["name"])

    form.enter_email(data["email"])

    form.enter_phone(data["phone"])

    form.select_gender()

    form.select_day()

    form.select_country(data["country"])

    form.select_date(data["date"])

    driver.quit()

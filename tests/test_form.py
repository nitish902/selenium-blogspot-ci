from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.form_page import FormPage

def test_form():

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

    form.enter_name("John")

    form.enter_email("test@gmail.com")

    form.enter_phone("9999999999")

    form.select_gender()

    form.select_day()

    form.select_country("India")

    form.select_date("04/16/2026")

    driver.quit()

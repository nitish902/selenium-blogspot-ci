from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class FormPage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.ID,"name")
    email = (By.ID,"email")
    phone = (By.ID,"phone")
    male_radio = (By.ID,"male")
    sunday_checkbox = (By.ID,"sunday")
    country_dropdown = (By.ID,"country")
    date_picker = (By.ID,"datepicker")

    def enter_name(self, text):
        self.driver.find_element(*self.name).send_keys(text)

    def enter_email(self, text):
        self.driver.find_element(*self.email).send_keys(text)

    def enter_phone(self, text):
        self.driver.find_element(*self.phone).send_keys(text)

    def select_gender(self):
        self.driver.find_element(*self.male_radio).click()

    def select_day(self):
        self.driver.find_element(*self.sunday_checkbox).click()

    def select_country(self, country):
        Select(self.driver.find_element(*self.country_dropdown)).select_by_visible_text(country)

    def select_date(self, date):
        self.driver.find_element(*self.date_picker).send_keys(date)
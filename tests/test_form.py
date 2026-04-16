from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

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

    wait = WebDriverWait(driver,10)

    wait.until(EC.presence_of_element_located((By.ID,"name"))).send_keys("Nitish")

    driver.find_element(By.ID,"email").send_keys("test@gmail.com")

    driver.find_element(By.ID,"phone").send_keys("9999999999")

    driver.find_element(By.ID,"male").click()

    driver.find_element(By.ID,"sunday").click()

    country = Select(driver.find_element(By.ID,"country"))
    country.select_by_visible_text("India")

    driver.find_element(By.ID,"datepicker").send_keys("04/16/2026")

    driver.execute_script("window.scrollBy(0,800)")

    alert_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Alert')]"))
    )

    alert_btn.click()

    alert = driver.switch_to.alert
    alert.accept()

    driver.execute_script("window.scrollBy(0,500)")

    table_value = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[2]/td[1]").text

    assert table_value == "Learn Selenium"

    driver.execute_script("window.scrollBy(0,500)")

    source = driver.find_element(By.ID,"draggable")
    target = driver.find_element(By.ID,"droppable")

    ActionChains(driver).drag_and_drop(source,target).perform()

    driver.quit()

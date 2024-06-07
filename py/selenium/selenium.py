from py.shared.logger import get_logger, error_message
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from py.shared.time import Time
from py.shared.data_reader import DataReader


class Selenium:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.data = DataReader("data.json").read_json()

    def check_visibility(self, by, value):
        try:
            return WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((by, value))
            )
        except Exception as e:
            error_message(f"Element not found: {e}")

    def click_element(self, by, value, wait=Time.random_sleep()):
        try:
            element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((by, value))
            )
            wait
            try:
                element.click()
            except Exception:  # JS click if regular click doesn't work
                self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            error_message(f"Element not clickable: {e}")

    def scrape_url(self):
        self.driver.get(self.data["url"])
        select_element = self.check_visibility(
            By.ID, self.data["checker"]["tramites_policia_nactional"]
        )
        Time.random_sleep()
        select = Select(select_element)
        select.select_by_value(
            self.data["checker"]["tramites_policia_nactional_select_value"]
        )
        Time.random_sleep()
        self.click_element(By.ID, self.data["checker"]["acceptar_1_id"])
        Time.random_sleep()
        self.click_element(By.ID, self.data["checker"]["entrar_1_id"])

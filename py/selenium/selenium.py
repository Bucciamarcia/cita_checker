from py.shared.logger import get_logger, error_message
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from py.shared.time import Time
from py.shared.data_reader import DataReader
from py.shared.random import Random


class Selenium:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.data = DataReader("data.json").read_json()
        self.service = Service(ChromeDriverManager().install())
        self.options = Options()
        user_agent = self.data["user_agent"]
        self.options.add_argument(f"user-agent={user_agent}")
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

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

    def fill_input(self, by, value: str, text: str) -> None:
        try:
            input_field = self.driver.find_element(by, value)
            input_field.clear()
            for c in text:
                input_field.send_keys(c)
                Time.random_sleep(0.05, 0.2)
        except Exception as e:
            error_message(f"Input field not found: {e}")

    def select_dropdown_by_visible_text(self, by, value: str, text: str) -> None:
        try:
            dropdown_element = self.driver.find_element(by, value)
            select = Select(dropdown_element)
            select.select_by_visible_text(text)
        except Exception as e:
            error_message(f"Dropdown not found: {e}")

    def compile_cita_previa(self) -> None:
        self.click_element(By.ID, self.data["checker"]["select_nie_id"])
        Time.random_sleep()
        pasaporte_number = f"IT{Random.random_number(1000000, 9999999)}"
        self.fill_input(By.ID, self.data["checker"]["input_nie_id"], pasaporte_number)
        Time.random_sleep()
        self.fill_input(
            By.ID,
            self.data["checker"]["input_name_id"],
            Random.random_name(path=self.data["names_path"]),
        )
        Time.random_sleep()
        self.fill_input(
            By.ID,
            self.data["checker"]["input_birth_id"],
            str(Random.random_number(1960, 2000)),
        )
        Time.random_sleep()
        self.select_dropdown_by_visible_text(
            By.ID, self.data["checker"]["country_dropdown_select_id"], "ITALIA"
        )
        Time.random_sleep()
        self.click_element(By.ID, self.data["checker"]["cita_previa_enviar_id"])

    def list_cita_options(self, by, value: str) -> list[str]:
        dropdown_element = self.driver.find_element(by, value)
        select = Select(dropdown_element)
        options = select.options
        return [option.text for option in options]

    def check_options(self, options: list[str]) -> bool | list[str]:
        viable_options = self.data["viable_options"]["asignacion_nie"]

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
        Time.random_sleep()
        self.compile_cita_previa()
        Time.random_sleep()
        self.click_element(By.ID, self.data["checker"]["solicitar_cita_id"])
        self.check_visibility(By.CLASS_NAME, self.data["checker"]["check_finale"])
        try:
            cita_options = self.list_cita_options(
                By.ID, self.data["checker"]["dropdown_selection_cita"]
            )
            if len(cita_options) > 1:
                print(f"OPZIONI TROVATE: {', '.join(cita_options)}")
            else:
                print("NESSUNA OPZIONE TROVATA")
        except Exception:
            print("NESSUNA OPZIONE TROVATA")

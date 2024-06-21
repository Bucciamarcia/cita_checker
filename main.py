from py.selenium.selenium import Selenium
from py.post_hander.post_hander import NieHander
from py.shared.time import TimeChecker
from datetime import time
from py.shared.logger import get_logger


def nie():
    scraper = Selenium()
    nie_options = scraper.check_nie()
    NieHander().handle_nie(nie_options)


def main():
    logger = get_logger(__name__)
    logger.warning("ATTENZIONE: Cambia indirizzi email destinatari in data_secret.json")
    while True:
        if TimeChecker.is_within_time(time(8, 0), time(17, 0)):
            nie()
            logger.info("Good night!")
            TimeChecker.random_sleep(3300, 3900)
        else:
            logger.info("Waiting for the next day...")
            TimeChecker.wait_until_time(time(8, 0))


if __name__ == "__main__":
    print("FROCIO CHI LEGGE")
    main()

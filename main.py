from py.selenium.selenium import Selenium
from py.post_hander.post_hander import NieHander
from py.post_hander.email_handler import EmailHandler
from py.shared.time import Time


def nie():
    scraper = Selenium()
    nie_options = scraper.check_nie
    NieHander().handle_nie(nie_options)


def main():
    while True:
        nie()
        Time.random_sleep(3300, 3900)


if __name__ == "__main__":
    print("FROCIO CHI LEGGE")
    EmailHandler("Option1 ||| Option2 ||| Option3").send_emails()
    # main()

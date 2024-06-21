from py.selenium.selenium import Selenium
from py.post_hander.post_hander import NieHander


def nie():
    scraper = Selenium()
    nie_options = scraper.check_nie
    NieHander().handle_nie(nie_options)


def main():
    nie()


if __name__ == "__main__":
    print("FROCIO CHI LEGGE")
    main()

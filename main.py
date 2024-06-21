from py.selenium.selenium import Selenium


def main():
    scraper = Selenium()
    nie_options = scraper.check_nie()


if __name__ == "__main__":
    print("FROCIO CHI LEGGE")
    main()

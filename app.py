#automação
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class CookieClicker:
    def __init__(self):
        self.SITE_LINK = "https://orteil.dashnet.org/cookieclicker/"
        self.SITE_MAP = {
            "buttons": {
                "cookie_obj": {
                    "xpath": "/html/body/div[2]/div[2]/div[15]/div[1]/button"
                },
                "upgrade": {
                    "xpath": "/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[$$NUMBER$$]"
                }
            }
        }

        service = Service()
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def open_website(self):

        self.driver.get(self.SITE_LINK) # pegando link da página
        time.sleep(10)

    def click_cookie(self):
        #self.driver.find_element_by_xpath(self.SITE_MAP["buttons"]["cookie_obj"]["xpath"])
        cookie = self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["cookie_obj"]["xpath"])
        cookie.click()

    def take_better_upgrade(self):

        find = False
        current_element = 2 # ondem como fosse um "array" nas compras das lojas

        while not find:
            obj = self.SITE_MAP["butttons"]["upgrade"]["xpath"].replace("$$NUMBER$$", str(current_element))
            obj_class = self.driver.find_element_by_xpath(obj).get_atribute("class")

            if not "enabled" in obj_class:
                find = True
            else: current_element += 1
        return current_element - 1


    def buy_upgrade(self):
        obj = self.SITE.MAP["buttons"]["upgrade"]['xpath'].replace("$$NUMBER$$", str(self.take_better_upgrade()))
        self.driver.find_element(obj).click()

    def run(self):
        self.open_website()
        i = 0
        while True:
            if i % 500 == 0 and i != 0:
                time.sleep(1)
                self.buy_upgrade()
                time.sleep(1)
            self.click_cookie()
            i += 1

        

    def __del__(self):
        self.driver.quit()

cookie = CookieClicker()
cookie.run()






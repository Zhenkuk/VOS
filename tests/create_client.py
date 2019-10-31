import names
import time

import random
from random import randint

import string

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\thekr\Downloads\coffe-master\coffe-master\drivers\chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_user_login(self):

        driver = self.driver
        driver.get("https://www.vetofficesuite.com/user/login")

        email_field = driver.find_element_by_xpath("//form[@id='frm']/p[3]/input")
        email_field.clear()
        email_field.send_keys("Yevtest")

        password_field = driver.find_element_by_xpath("//form[@id='frm']/p[4]/input")
        password_field.clear()
        password_field.send_keys("Test1234")

        button_login = driver.find_element_by_xpath("//form[@id='frm']/div/div[2]/input")
        button_login.click()

        create_client = driver.find_element_by_xpath("//div[2]/ul/li[3]/a")
        create_client.click()

        for i in range(0,300):

            def makeEmail():
                extensions = ['com','net','org','gov']
                domains = ['gmail','yahoo','comcast','verizon','charter','hotmail','outlook','frontier']

                winext = extensions[random.randint(0,len(extensions)-1)]
                windom = domains[random.randint(0,len(domains)-1)]

                acclen = random.randint(1,20)

                winacc = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(acclen))

                finale = winacc + "@" + windom + "." + winext
                return finale

            randemail = str(makeEmail())

            def random_with_N_digits(n):
                range_start = 10**(n-1)
                range_end = (10**n)-1
                return randint(range_start, range_end)

            randophone = str(random_with_N_digits(10))

            randoname = names.get_first_name()
            randolname = names.get_last_name()

            client_name = driver.find_element_by_xpath("//fieldset/p/input")
            client_name.send_keys("" + randoname + "")
            print("Name created: " + randoname + "")

            client_last_name = driver.find_element_by_xpath("//fieldset[2]/p/input")
            client_last_name.send_keys("" + randolname + "")
            print("Last Name created: " + randolname + "")

            client_address = driver.find_element_by_xpath("//p[4]/input")
            client_address.send_keys("Mechnikova 18")

            client_city = driver.find_element_by_xpath("//p[5]/input")
            client_city.send_keys("Dnipro")

            client_email = driver.find_element_by_xpath("//fieldset[2]/p[7]/input")
            client_email.send_keys("" + randemail + "")
            print("Email created: " + randemail + "")
            client_zip = driver.find_element_by_xpath("//p[6]/input")
            client_zip.send_keys("49008")

            client_phone = driver.find_element_by_xpath("//p[7]/input")
            client_phone.send_keys("" + randophone + "")
            print("Phone created: " + randophone + "")

            select = Select(driver.find_element_by_name('USA_state_client'))
            select.select_by_visible_text("Alabama")

            saveButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//form/p[2]/input")))
            saveButton.click()

            time.sleep(5)

            create_client = driver.find_element_by_xpath("//a[contains(text(),'Create new client')]")
            create_client.click()
            print("--- --- ---")

    def tear_down(self):
     if (self.driver!=None):
        print("END")
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

import logging
import os
import time,pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.HomePage import HomePage
from Utility.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Testclass(BaseClass):

    def test_e2e(self):
        #self.driver.find_element(By.XPATH, '(//input[@name="name" ])[1]').send_keys('sai')
        homePage = HomePage(self.driver)
        homePage.NameItem().send_keys('saikumar')

        #self.driver.find_element(By.XPATH, '//input[@name="email"]').send_keys('Saikumar@gmail.com')
        email = HomePage(self.driver)
        email.EmailItem().send_keys('Saikumar@gmail.com')

        #self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys('1234')
        EEmail=HomePage(self.driver)
        EEmail.EmailPWDItem().send_keys('1234')

        #self.driver.find_element(By.ID, 'exampleCheck1').click()
        CheckBox = HomePage(self.driver)
        # CheckBox.Checkitem.click()
        checkbox_element = CheckBox.Checkitem()  # Call the method to get the checkbox element
        checkbox_element.click()  # Click the checkbox element

        gender = Select(self.driver.find_element(By.ID, 'exampleFormControlSelect1'))
        gender.select_by_index(1)
        gender.select_by_visible_text("Female")

        self.driver.find_element(By.XPATH, '//input[@type="submit"]').click()
        message = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        for messages in message:
            try:
                if messages == "success":

                    print("'it's mtched")
                    assert self.driver.find_element(By.CLASS_NAME, "alert-success") == 'Success!'
                    break
                print(self.driver.find_element(By.CLASS_NAME, "alert-success").get_attribute('value'))
                break
            except:
                print('success is not there in alert')
                break

        print(message)
    def test_M2M(self):
        self.driver.find_element(By.LINK_TEXT, 'Shop').click()
        products = self.driver.find_elements(By.XPATH,'//div[@class="card h-100"]')

        for Product in products:
            ProductName = Product.find_element(By.XPATH, 'div/h4/a').text
            if ProductName == 'iphone X':
                Product.find_element(By.XPATH, 'div/button').click()

        products = self.driver.find_elements(By.XPATH,'//div[@class="card h-100"]')

        for product in products:
            productName = product.find_element(By.XPATH, 'div/h4/a').text
            if productName == 'Samsung Note 8':
                product.find_element(By.XPATH, 'div/button').click()

            if productName == 'Nokia Edge':
                product.find_element(By.XPATH, 'div/button').click()

            if productName == 'Blackberry':
                product.find_element(By.XPATH, 'div/button').click()

        self.driver.find_element(By.XPATH, '//a[@class="nav-link btn btn-primary"]').click()
        self.driver.find_element(By.XPATH, '//button[@class="btn btn-success"]').click()
        self.driver.find_element(By.ID, "country").send_keys('ind')
        element = WebDriverWait(self.driver, 10).until(
                     EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, 'India').click()


        self.driver.find_element(By.XPATH, '//div[@class="checkbox checkbox-primary"]').click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        succes = self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text

        assert "Success! Thank you! " in succes


        time.sleep(5)
        self.driver.close()

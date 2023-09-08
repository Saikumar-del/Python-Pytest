from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    Name = (By.XPATH, '(//input[@name="name" ])[1]')
    Eemail = (By.XPATH, '//input[@name="email"]')
    EPassword = (By.XPATH, '//input[@type="password"]')
    CheckBox = (By.ID, 'exampleCheck1')

    def NameItem(self):
        return self.driver.find_element(*HomePage.Name)

    def EmailItem(self):
        return self.driver.find_element(*HomePage.Eemail)

    def EmailPWDItem(self):
        return self.driver.find_element(*HomePage.EPassword)

    def Checkitem(self):
        return self.driver.find_element(*HomePage.CheckBox)

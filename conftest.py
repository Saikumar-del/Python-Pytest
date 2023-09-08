import os
import sys
import time
import logging
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest




@pytest.fixture(scope = "class")
def setup(request):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        service_obj = Service("C:\\Users\Sai Kumar\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)

        driver.get('https://qaclickacademy.github.io/protocommerce/')
        request.cls.driver = driver
        yield
        time.sleep(7)

def test_log():
        os.chdir('C:\\Users\Sai Kumar\PycharmProjects\pythonProject')
        timestr = time.strftime("%Y%m%d")
        Name = 'PythonCLI_' + timestr + '.txt'
        logging.basicConfig(format='%(asctime)s &(message)s',
                            datefmt='%d-%m-%Y:%H:%M:%s',
                            level=logging.DEBUG,
                            filename=Name)
        logger = logging.getLogger('my_app')
        logger.debug(':Failed; file does not exists')
        sys.exit(0)










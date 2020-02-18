import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.valA=7.5

    def test_search_in_python_org(self):
        for i in range(250):
            driver = webdriver.Firefox()
            self.driver=driver
            try:
                driver.get("https://academics.mnnit.ac.in/certificates")
                elem1 = driver.find_element_by_name("regno")
                #ENTER THE REGISTRATION NUMBER HERE.
                elem1.send_keys("REGISTRATION_NUMBER_HERE")
                elem2 = driver.find_element_by_name("cpi")
                elem2.send_keys(str(self.valA))
                elem2.send_keys(Keys.RETURN)
                time.sleep(1)
                if driver.find_elements_by_css_selector('#name'):
                    print ("Element exists at "+str(self.valA))
                    break
            except UnexpectedAlertPresentException:
                print ("It is not "+str(self.valA))
                self.driver.close()
                self.valA=self.valA+0.02

    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()


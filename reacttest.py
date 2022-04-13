import unittest
from selenium import webdriver
import HtmlTestRunner
import time
path = 'C:/Users/sekma/Desktop/python/chromedriver.exe'
class amazontest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver= webdriver.Chrome(path)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("http://localhost:3000/home")
    def test(self):
     try:
        self.driver.find_element_by_xpath('//*[@id="collasible-nav-dropdown"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="responsive-navbar-nav"]/div/div/div/a').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/form/div[1]/input').send_keys("souha@gmail.com")
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/form/div[2]/input').send_keys("souha123")
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/form/button').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/nav/div/a').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="cards"]/div[1]/div/button').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="responsive-navbar-nav"]/div/a').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/button[2]').click()

        
        
     except:
        self.driver.save_screenshot("C:\\Users\\sekma\\Desktop\\python\\screenshot\\reacttestcapture.png")
         
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")    

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/sekma/Desktop/python/reportforreacttest'))
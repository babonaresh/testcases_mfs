import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class MSA(unittest.TestCase):
   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_team(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       time.sleep(0)
       driver.get("https://mavfs.herokuapp.com/")# directing to the website
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li[1]/a').click() #
       time.sleep(0)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(0)
       elem.send_keys(Keys.RETURN)
       time.sleep(0)
       driver.get("https://mavfs.herokuapp.com/")
       time.sleep(0)
       assert "logged in "
       driver.get('https://mavfs.herokuapp.com/admin/')
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[1]/td[1]/a').click()  #
       time.sleep(0)
       elem = driver.find_element_by_id("id_cust_name")
       elem.send_keys("selenium")
       time.sleep(0)
       elem = driver.find_element_by_id("id_organization")
       elem.send_keys("seleniumhq")
       time.sleep(0)
       elem = driver.find_element_by_id("id_role")
       elem.send_keys("tester")
       time.sleep(0)
       elem = driver.find_element_by_id("id_email")
       elem.send_keys("se@gmail.com")
       time.sleep(0)
       elem = driver.find_element_by_id("id_bldgroom")
       elem.send_keys("111")
       time.sleep(0)
       elem = driver.find_element_by_id("id_address")
       elem.send_keys("seleniumHQ")
       time.sleep(0)
       elem = driver.find_element_by_id("id_account_number")
       elem.send_keys("111")
       time.sleep(0)
       elem = driver.find_element_by_id("id_city")
       elem.send_keys("Omaha")
       time.sleep(0)
       elem = driver.find_element_by_id("id_state")
       elem.send_keys("NE")
       time.sleep(0)
       elem = driver.find_element_by_id("id_zipcode")
       elem.send_keys("11111")
       time.sleep(0)
       elem = driver.find_element_by_id("id_phone_number")
       elem.send_keys("123426789")
       time.sleep(0)
       elem.send_keys(Keys.RETURN)
       time.sleep(5)
       driver.get("https://mavfs.herokuapp.com/")
       time.sleep(0)
       elem=driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a').click()
       time.sleep(0)
       #editing
       elem=driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/table/tbody/tr[4]/td[12]/a').click()
       time.sleep(0)
       elem = driver.find_element_by_id("id_cust_name")
       elem.send_keys(Keys.CONTROL+"a")
       elem.send_keys(Keys.DELETE)
       elem.send_keys("editedselenium")
       time.sleep(0)
       elem = driver.find_element_by_id("id_organization")
       elem.send_keys(Keys.CONTROL + "a")
       elem.send_keys(Keys.DELETE)
       elem.send_keys("editdseleniumhq")
       time.sleep(0)
       elem = driver.find_element_by_id("id_role")
       elem.send_keys(Keys.CONTROL + "a")
       elem.send_keys(Keys.DELETE)
       elem.send_keys("editedtester")
       time.sleep(0)
       elem.send_keys(Keys.RETURN)
       time.sleep(5)
       elem = driver.find_element_by_xpath(
           '//*[@id="app-layout"]/div/div/div/div[3]/table/tbody/tr[4]/td[13]/a').click()
       time.sleep(0)
       elem = driver.switch_to.alert.accept()
       time.sleep(5)
        #adding
       #service
       driver.get("https://mavfs.herokuapp.com/")
       elem = driver.find_element_by_xpath(
           '//*[@id="app-layout"]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a').click()
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/div/a/span').click()
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="id_cust_name"]').click()
       time.sleep(0)
       select = Select(driver.find_element_by_xpath('//*[@id="id_cust_name"]'))
       time.sleep(0)
       elem = select.select_by_index("1")
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="id_service_category"]')
       elem.send_keys("delivery")
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="id_description"]')
       elem.send_keys("delivery of 24 super cookies")
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="id_location"]')
       elem.send_keys("pki")
       time.sleep(0)
       elem = driver.find_element_by_xpath("//*[@id='id_setup_time']")
       elem.send_keys(Keys.CONTROL + "a")
       elem.send_keys(Keys.DELETE)
       elem.send_keys("2018-11-22 01:41:07")
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="id_cleanup_time"]')
       elem.send_keys(Keys.CONTROL + "a")
       elem.send_keys(Keys.DELETE)
       elem.send_keys("2018-11-22 0:41:07")
       time.sleep(0)
       elem = driver.find_element_by_xpath('// *[ @ id = "id_service_charge"]')
       elem.send_keys("120")
       time.sleep(0)
       elem.send_keys(Keys.RETURN)
       time.sleep(5)
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/table/tbody/tr[6]/td[8]/a').click()
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="id_description"]')
       elem.send_keys(Keys.CONTROL + 'a')
       elem.send_keys(Keys.DELETE)
       elem.send_keys("delivery of 24 super cookies without nuts")
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="id_location"]')
       elem.send_keys(Keys.CONTROL + 'a')
       elem.send_keys(Keys.DELETE)
       elem.send_keys("pki 172")
       time.sleep(0)
       elem.send_keys(Keys.RETURN)
       time.sleep(5)
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/table/tbody/tr[6]/td[9]/a').click()
       time.sleep(0)
       elem = driver.switch_to.alert.accept()
       time.sleep(5)
       driver.get("https://mavfs.herokuapp.com/")
       # Adding
       # Product
       elem = driver.find_element_by_xpath(
           '//*[@id="app-layout"]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/p[2]/a').click()
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/div/a/span').click()
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="id_cust_name"]').click()
       time.sleep(0)
       select = Select(driver.find_element_by_xpath('//*[@id="id_cust_name"]'))
       time.sleep(0)
       elem = select.select_by_index("1")
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="id_product"]')
       elem.send_keys("Super Cookies")
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="id_p_description"]')
       elem.send_keys("super cookies with chocolate chips and caramel soup added with sugar crystals")
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="id_quantity"]')
       elem.send_keys("24")
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="id_pickup_time"]')
       elem.send_keys(Keys.CONTROL + "a")
       elem.send_keys(Keys.DELETE)
       elem.send_keys("2018-11-22 12:00:00")
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="id_charge"]')
       elem.send_keys("120")
       time.sleep(0)
       elem.send_keys(Keys.RETURN)
       time.sleep(5)
       assert "added service"
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/table/tbody/tr[4]/td[7]/a').click()
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="id_product"]')
       elem.send_keys(Keys.CONTROL + "a")
       elem.send_keys(Keys.DELETE)
       elem.send_keys("Selenium Super Cookies")
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="id_p_description"]')
       elem.send_keys(Keys.CONTROL + "a")
       elem.send_keys(Keys.DELETE)
       elem.send_keys("Selenium super cookies with chocolate chips and caramel soup added with sugar crystals")
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="id_quantity"]')
       elem.send_keys(Keys.CONTROL + "a")
       elem.send_keys(Keys.DELETE)
       elem.send_keys("20")
       time.sleep(0)
       elem.send_keys(Keys.RETURN)
       time.sleep(5)
       assert "edited service"
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/table/tbody/tr[4]/td[8]/a').click()
       time.sleep(0)
       elem = driver.switch_to.alert.accept()
       time.sleep(5)
   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
       unittest.main()
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import csv

class MSA(unittest.TestCase):
   def setUp(self):
       self.driver = webdriver.Chrome()


   def test_team(self):
       data=open('user.csv')
       datareader=csv.reader(data)
       for row in datareader:
           if datareader.line_num == 1:
            continue
           else:
            user=row[0]
            pwd=row[1]
       driver = self.driver
       driver.maximize_window()
       time.sleep(0)
       driver.get("https://team3-8210-msa.herokuapp.com/")# directing to the website
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[2]/li[1]/a').click() #
       time.sleep(1)
       #select = Select(driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul[2]/div"))  #
       #select = Select(driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul[2]/div/div"))#
       #time.sleep(5)
       #select.select_by_visible_text("Login")
       #driver.get("https://team3-8210-msa.herokuapp.com/accounts/login/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(1)
       elem.send_keys(Keys.RETURN)
       time.sleep(1)
       elem = driver.find_element_by_xpath('//*[@id="navbarDropdownMenuLink"]').click()
       time.sleep(5)
       elem=driver.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[2]/li/div/a[2]').click()
       assert "Loggd out"
       time.sleep(1)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
       unittest.main()

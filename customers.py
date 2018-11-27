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
       driver = self.driver
       driver.maximize_window()
       time.sleep(0)
       driver.get("https://mavfs.herokuapp.com/")  # directing to the website
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li[1]/a').click()  #
       time.sleep(0)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys('instructor')
       elem = driver.find_element_by_id("id_password")
       elem.send_keys('instructor1a')
       time.sleep(0)
       elem.send_keys(Keys.RETURN)
       time.sleep(0)
       driver.get("https://mavfs.herokuapp.com/")
       time.sleep(2)
       assert "logged in "
       driver.get('https://mavfs.herokuapp.com/admin/')
       time.sleep(5)
       elem = driver.find_element_by_xpath(
           '//*[@id="content-main"]/div[2]/table/tbody/tr[1]/td[1]/a').click()  #
       time.sleep(5)
       data = open('customers.csv')
       datareader = csv.reader(data)
       for row in datareader:
           if datareader.line_num == 1:
               continue
           else:
               name = row[0]
               org = row[1]
               role = row[2]
               email = row[3]
               room = row[4]
               address = row[5]
               ac = row[6]
               city = row[7]
               state = row[8]
               zipcode = row[9]
               phone = row[10]
               time.sleep(15)
               elem = driver.find_element_by_id("id_cust_name")
               elem.send_keys(name)
               time.sleep(0)
               elem = driver.find_element_by_id("id_organization")
               elem.send_keys(org)
               time.sleep(0)
               elem = driver.find_element_by_id("id_role")
               elem.send_keys(role)
               time.sleep(0)
               elem = driver.find_element_by_id("id_email")
               elem.send_keys(email)
               time.sleep(0)
               elem = driver.find_element_by_id("id_bldgroom")
               elem.send_keys(room)
               time.sleep(0)
               elem = driver.find_element_by_id("id_address")
               elem.send_keys(address)
               time.sleep(0)
               elem = driver.find_element_by_id("id_account_number")
               elem.send_keys(ac)
               time.sleep(0)
               elem = driver.find_element_by_id("id_city")
               elem.send_keys(city)
               time.sleep(0)
               elem = driver.find_element_by_id("id_state")
               elem.send_keys(state)
               time.sleep(0)
               elem = driver.find_element_by_id("id_zipcode")
               elem.send_keys(zipcode)
               time.sleep(0)
               elem = driver.find_element_by_id("id_phone_number")
               elem.send_keys(phone)
               time.sleep(5)
               elem.send_keys(Keys.RETURN)
               time.sleep(10)
               elem=driver.find_element_by_xpath('//*[@id="content-main"]/ul/li/a').click()
       driver.get("https://mavfs.herokuapp.com/")
       time.sleep(0)
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a').click()  #
       time.sleep(15)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
    unittest.main()
              # print(name,org,role,email,address,ac,city,state,zipcode,phone)


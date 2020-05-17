from selenium import webdriver
import unittest
from All_Tests.SeleniumTests.PageObjectSample.page_objects.pg_Login import Page_Login

class LoginTest(unittest.TestCase):

    @classmethod
    def setupClass(self):
        self.dr = webdriver.Chrome(executable_path="C:/Users/Albert/PycharmProjects/TestProject/All_Tests/Selenium/chromedriver.exe")
        self.dr.implicitly_wait(10)
        self.dr.maximize_window()
        
        
    def test_login_is_valid(self):
        dr = self.dr
        login_pg = Page_Login(dr)
        login_pg.enter_user_name("Admin")
        login_pg.enter_password_name("admin123")
        login_pg.click_login_button()

        '''
        dr.get("https://opensource-demo.orangehrmlive.com/")
        dr.find_element_by_id("txtUsername").send_keys("Admin")
        dr.find_element_by_id("txtPassword").send_keys("admin123")
        dr.find_element_by_id("btnLogin").click()
        dr.find_element_by_id("txtUsername").send_keys("Admin")
        '''

    @classmethod
    def tearDown(self):
        self.dr.close()
        self.dr.quit()

if __name__ == "__main__":
    unittest.main()
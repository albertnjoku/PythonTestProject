class Page_Login():

    def __init__(self, driver):
        self.driver = driver
        self.User_Name_Text_Box_Id = "txtUsername"
        self.User_Password_Text_Box_Id = "txtPassword"
        self.Button_Login_Id = "btnLogin"
        self.Welcome_Page_Link = "welcome"

    def enter_user_name(self, username_entry):
        self.driver.find_element_by_id(self.User_Name_Text_Box_Id).clear()
        self.driver.find_element_by_id(self.User_Name_Text_Box_Id).send_keys(username_entry)

    def enter_user_password(self, userpassword_entry):
        self.driver.find_element_by_id(self.User_Password_Text_Box_Id).clear()
        self.driver.find_element_by_id(self.User_Password_Text_Box_Id).send_keys(userpassword_entry)

    def click_login_button(self):
        self.driver.find_element_by_id(self.Button_Login_Id).click()

    def Assert_Login_Successful(self):
        self.driver.find_element_by_id(self.Welcome_Page_Link).click()        
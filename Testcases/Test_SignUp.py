import pytest
from Testcases.BaseTest import BaseTest
from Pages.RegistrationPage import RegistrationPage

class Test_SignUp(BaseTest):

    def test_dosignup(self):
        regPage = RegistrationPage(self.driver)
        regPage.fillform("KV","123456789","email@gmail.com","India","Pune","KV@123","selenium")

    def test_signup_submit(self):
        regPageSubmit = RegistrationPage(self.driver)
        regPageSubmit.fillform("User","123456789","email@gmail.com","India","Pune","User@123","Pyselenium")
        regPageSubmit.submitform()
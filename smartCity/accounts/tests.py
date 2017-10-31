from django.test import TestCase
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
import unittest

class AdminTestCase(LiveServerTestCase):
    def setUp(self):
        # setUp is where you instantiate the selenium webdriver and loads the browser.
        User.objects.create_superuser(
            username='admin',
            password='admin',
            email='admin@example.com'
        )

        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        super(AdminTestCase, self).setUp()

    def tearDown(self):
        # Call tearDown to close the web browser
        self.selenium.quit()
        super(AdminTestCase, self).tearDown()

    def test_create_user(self):
        """
        Django admin create user test
        This test will create a user in django admin and assert that
        page is redirected to the new user change form.
        """
        # Open the django admin page.
        # DjangoLiveServerTestCase provides a live server url attribute
        # to access the base url in tests
        self.selenium.get(
            '%s%s' % (self.live_server_url,  "/admin/")
        )

        # Fill login information of admin
        username = self.selenium.find_element_by_id("id_username")
        username.send_keys("admin")
        password = self.selenium.find_element_by_id("id_password")
        password.send_keys("admin")

        # Locate Login button and click it
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/admin/auth/user/add/")
        )

        # Fill the create user form with username and password
        self.selenium.find_element_by_id("id_username").send_keys("test")
        self.selenium.find_element_by_id("id_password1").send_keys("test")
        self.selenium.find_element_by_id("id_password2").send_keys("test")

        # Forms can be submitted directly by calling its method submit
        self.selenium.find_element_by_id("user_form").submit()
        #self.assertIn("Change user", self.selenium.title)

class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/accounts/register')
        #find the form element
        username = selenium.find_element_by_id('id_username')
        email = selenium.find_element_by_id('id_email')
        first_name = selenium.find_element_by_id('id_first_name')
        last_name = selenium.find_element_by_id('id_last_name')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')
        dob = selenium.find_element_by_id('id_dob')
        contactNumber = selenium.find_element_by_id('id_contactNumber')
        address = selenium.find_element_by_id('id_address')
        userType = selenium.find_element_by_id('id_userTypeID')


        #Fill the form with data
        first_name.send_keys('test_Name')
        last_name.send_keys('test_Last')
        username.send_keys('test')
        email.send_keys('test@test.com')
        password1.send_keys('test5678')
        password2.send_keys('test5678')
        dob.send_keys('10/10/10')
        contactNumber.send_keys('0493758375')
        address.send_keys('1/2 selenium street')
        userType.send_keys('test_Type')

        self.selenium.find_element_by_xpath('//button').click()
from playwright.sync_api import expect

class LoginPage:
    # self is a convention in python to refer to the instance of the class itself. 
    # It allows us to access the attributes and methods of the class within its own definition. 
    # In this code, self.page is used to store the reference to the browser page,
    # and other methods in the class can use self.page to interact with the page.
    # if no self is used, the methods would not have access to the page instance, and we would not be able to perform actions on the page or access its elements.
    def __init__(self, page):
    #stores browser page inside the object 
    #self.page is an instance variable that holds the reference to the browser page, allowing other methods in the class to interact with the page
        self.page = page
    #locators for the elements on the login page are defined as instance variables, allowing other methods in the class to easily access 
    # interact with these elements when performing actions like filling in the username and password or clicking the login button.
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator("[data-test='error']")
    #self refers to the instance of the class, and it allows us to access the attributes 
    #methods of the class within its own definition.
    def goto(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username_input.fill(username) 
        self.password_input.fill(password)
        self.login_button.click()

    def expect_error_visible(self):
        expect(self.error_message).to_be_visible()
        return self.error_message.text_content()

    def expect_password_masked(self):
        expect(self.password_input).to_have_attribute("type", "password")

    def expect_successful_login(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def is_error_visible(self):
        return self.error_message.is_visible()

    def get_error_text(self):
        return self.error_message.text_content()

import time, yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

ids = dict()
with open("./locators.yaml") as f:
    locators = yaml.safe_load(f)
for locator in locators["xpath"].keys():
    ids[locator] = (By.XPATH, locators["xpath"][locator])
for locator in locators["css"].keys():
    ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send '{word}' to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operate with {locator}")
            return False
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=2)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def check_title_font(self, locator, parameter, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        get_element = self.find_element(locator)
        if not get_element:
            return None
        try:
            result = get_element.value_of_css_property(parameter)
        except:
            logging.exception("Text")
            return None
        logging.debug(f'Проверка {element_name}')
        return result

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(ids["LOCATOR_PASS_FIELD"], word, description="password form")

    def get_error_text(self):
        return self.get_text_from_element(ids["LOCATOR_ERROR_FIELD"], description="error label")


    def login_success(self):
        return self.get_text_from_element(ids["LOCATOR_HELLO"], description="username")

    def click_about_button(self):
        self.click_button(ids["LOCATOR_BUTTON_ABOUT"], description="send")

    def click_login_button(self):
        self.click_button(ids["LOCATOR_LOGIN_BTN"], description="login")

    def title_font(self) -> str:
        return self.check_title_font(ids['LOCATOR_FORM_NAME'], 'font-size',
                                     description='шрифта в заголовке на странице авторизации')
    def get_about_text(self):
        return self.get_text_from_element(ids["LOCATOR_FORM_NAME"], description="about text")

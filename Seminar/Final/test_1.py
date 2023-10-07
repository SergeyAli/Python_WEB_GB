from time import sleep

import yaml
from testpage import OperationsHelper
import logging

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_login_negative(browser):
    logging.info("Test login_negative Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401", "test_login_negative FAILED"


def test_login_positive(browser):
    logging.info("Test login_positive Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    assert testpage.login_success() == f"Hello, {testdata['login']}", "test_login_positive FAILED"

def test_abaut(browser, expected_text):
    logging.info("Test add_post Starting")
    testpage = OperationsHelper(browser)
    sleep(1)
    testpage.click_about_button()
    received_text = testpage.get_about_text()
    assert received_text == expected_text, "Test about fail"

def test_font_check(browser, expected_font):
    logging.info("Test add_post Starting")
    testpage = OperationsHelper(browser)
    sleep(1)
    resulting_font = testpage.title_font()
    assert expected_font == resulting_font, "Test font fail"


import yaml, time
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



def test_add_post(browser):
    logging.info("Test add_post Starting")
    testpage = OperationsHelper(browser)
    # testpage.go_to_site()
    # testpage.enter_login(testdata["login"])
    # testpage.enter_pass(testdata["pswd"])
    # testpage.click_login_button()
    testpage.click_add_post_button()
    testpage.add_title(testdata["title"])
    testpage.add_description(testdata["description"])
    testpage.add_content(testdata["content"])
    testpage.click_save_post_button()
    testpage.find_new_post_title()
    assert testpage.find_new_post_title() == f"{testdata['title']}", "test add post FAILED"

"""
Добавить в проект тест по проверке механики работы формы Contact Us. Должно проверятся открытие формы, 
ввод данных в поля, клик по кнопке и появление всплывающего alert.
"""

def test_step4(browser):
    logging.info('Test Starting')
    testpage = OperationsHelper(browser)
    # testpage.go_to_site()
    # testpage.enter_login(testdata["login"])
    # testpage.enter_pass(testdata["password"])
    # testpage.click_login_button()
    # testpage.click_contact_button()
    # time.sleep(4)
    testpage.enter_name('Dmitriy Leonov')
    testpage.enter_email('d.leonov@yandex.ru')
    testpage.enter_content_field('Test Text')
    time.sleep(4)
    testpage.click_contact_us_button()
    time.sleep(4)
    assert testpage.alert() == 'Form successfully submitted'
import yaml
from module import Site


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, error_code):

    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn = site.find_element("css", btn_selector)
    btn.click()
    err_label = site.find_element("xpath", x_selector3).text
    assert err_label == error_code, "test_step1 Failed"


def test_step2(x_selector1, x_selector2, x_selector4, btn_selector, account_name):

    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata["password"])
    btn = site.find_element("css", btn_selector)
    btn.click()
    code_label = site.find_element("xpath", x_selector4).text

    assert code_label == account_name, "test_step1 Failed"







    site.driver.close()


# import yaml
# from module import Site
#
# with open("./testdata.yaml") as f:
#     testdata = yaml.safe_load(f)
# site = Site(testdata["address"])
#
# def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, error_code):
#     input1 = site.find_element("xpath", x_selector1)
#     input1.send_keys("test")
#     input2 = site.find_element("xpath", x_selector2)
#     input2.send_keys("test")
#     btn = site.find_element("css", btn_selector)
#     btn.click()
#     err_label = site.find_element("xpath", x_selector3).text
#     assert err_label == error_code, "test_step1 False"
#
# def test_step2(x_selector1, x_selector2, x_selector4, btn_selector, accound_name):
#     input1 = site.find_element("xpath", x_selector1)
#     input1.clear()
#     input1.send_keys(testdata["login"])
#     input2 = site.find_element("xpath", x_selector2)
#     input2.clear()
#     input2.send_keys(testdata["password"])
#     btn = site.find_element("css", btn_selector)
#     btn.click()
#     code_label = site.find_element("xpath", x_selector4).text
#     assert code_label == accound_name, "test_step2 False"
#
#
#
#
#
#
#
#
#
# site.driver.close()
# # test_step1()
# # # if __name__ == "__main__":
# # #     pass
# # css_selector = "span.mdc-text-field__ripple"
# # print(site.get_element_property("css", css_selector, "height"))
# #
# # xpath = '//*[@id="login"]/div[3]/button/div'
# # print(site.get_element_property("xpath", xpath, "color"))
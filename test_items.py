from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_wastebucket_button(browser):
    browser.get(link)
    wastebucket_button = browser.find_element(
        By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')

    assert wastebucket_button.is_enabled()

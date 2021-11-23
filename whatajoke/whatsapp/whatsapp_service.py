import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

whatsapp_url: str = "https://web.whatsapp.com/"

input_search_xpath = "//*[@id=\"side\"]/div[1]/div/label/div/div[2]"
input_message_xpath = "//*[@id=\"main\"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]"
open_group_xpath = "//*[@id=\"main\"]/header/div[2]/div[1]/div/span"


def select_contact_xpath(contact) -> str:
    return '//span[@title="{}"]'.format(contact)


def assert_correct_contact(group: str, group_title_element):
    assert group_title_element.text == group


def send_message(group: str, message: str, headed: bool):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=./User_Data')

        if not headed:
            options.add_argument('--headless')

        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

        driver.get(whatsapp_url)

        input_box_search = WebDriverWait(driver, 50) \
            .until(lambda driver: driver.find_element_by_xpath(input_search_xpath))
        input_box_search.click()
        input_box_search.send_keys(group)

        selected_contact = WebDriverWait(driver, 50) \
            .until(lambda driver: driver.find_element_by_xpath(select_contact_xpath(group)))
        selected_contact.click()

        group_title_element = WebDriverWait(driver, 50) \
            .until(lambda driver: driver.find_element_by_xpath(open_group_xpath))
        assert_correct_contact(group, group_title_element)

        message_box = WebDriverWait(driver, 50) \
            .until(lambda driver: driver.find_element_by_xpath(input_message_xpath))
        # TODO: set text into element to not send multiple messages
        # driver.execute_script(f"arguments[0]\\.innerText = '{message}';", message_box)
        message_box.send_keys(message + Keys.ENTER)
        time.sleep(3)

    finally:
        driver.quit()

import random
import time

from conftest import driver
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage


def test_text_box(driver):
    text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
    text_box_page.open()
    input_data = text_box_page.fill_of_fields()
    output_data = text_box_page.check_filled_form()
    #assert input_data == output_data, "error"

def test_checkbox(driver):
    check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
    check_box_page.open()
    check_box_page.open_full_list()
    check_box_page.click_random_checkbox()
    input_result = check_box_page.get_checked_checkboxes()
    output_result = check_box_page.get_output_result()
    assert input_result == output_result, "checkboxes have not been selected"

def test_radio_button(driver):
    radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
    radio_button_page.open()
    radio_button_page.click_on_the_radio_button('impressive') # Input yes, impressive or no
    radio_button_page.get_output_result()
    assert radio_button_page.get_output_result() == 'Impressive', 'RadioButton has not been selected'

#Tests for Web Table

def test_web_table_add_person(driver):
    web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
    web_table_page.open()
    new_person = web_table_page.add_new_person()
    output_result = web_table_page.check_new_person()
    print(new_person)
    print(output_result)
    assert new_person in output_result, "New person has not been added"

def test_web_table_search_person(driver):
    web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
    web_table_page.open()
    key_word = web_table_page.add_new_person()[random.randint(0, 5)]
    web_table_page.search_person(key_word)
    table_result = web_table_page.check_search_person()
    assert key_word in table_result, 'Person is not found'

def test_web_table_edit_some_person(driver):
    web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
    web_table_page.open()
    var_for_search = web_table_page.add_new_person()[random.randint(0, 5)]
    web_table_page.search_person(var_for_search)
    data, edit_field = web_table_page.edit_person_info()
    assert edit_field in data, 'Person is not found'

def test_web_table_delete_person(driver):
    web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
    web_table_page.open()
    var_for_search = web_table_page.add_new_person()[random.randint(0, 5)]
    time.sleep(0.1)
    web_table_page.search_person(var_for_search)
    web_table_page.delete_person()
    text = web_table_page.check_deleted_person()
    assert text == 'No rows found', 'Person is not delete'

def test_change_table_rows(driver):
    web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
    web_table_page.open()
    data, count = web_table_page.select_up_to_rows()
    assert data == count

def test_buttons(driver):
    buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
    buttons_page.open()
    click = buttons_page.click_on_button()
    right = buttons_page.right_click_on_button()
    doubleclick = buttons_page.double_click_on_button()
    assert click == "You have done a dynamic click", "Button is not clicked"
    assert right == "You have done a right click", "Right Click is not clicked"
    assert doubleclick == "You have done a double click", "Double Click is not clicked"

def test_simple_links(driver):
    links_page = LinksPage(driver, "https://demoqa.com/links")
    links_page.open()
    href, url = links_page.check_new_tab_simple_link()
    assert href == url, "This link is broken or URL is incorrect"

def test_broken_links(driver):
    links_page = LinksPage(driver, "https://demoqa.com/links")
    links_page.open()
    response_code = links_page.check_broken_list("https://demoqa.com/bad-request")
    assert response_code == 400, "Broken link is not found"

def test_download_file(driver):
    download_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
    download_page.open()
    check = download_page.download_file()
    assert check is True, "The file has not been downloaded"


def test_upload_file(driver):
    upload_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
    upload_page.open()
    file_name, upload_file_name = upload_page.upload_file()
    assert file_name == upload_file_name, "The file has not been uploaded"
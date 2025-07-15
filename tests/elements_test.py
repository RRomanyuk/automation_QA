from conftest import driver
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


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
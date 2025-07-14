import time
from conftest import driver
from pages.elements_page import TextBoxPage

def test_text_box(driver):
    text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
    text_box_page.open()
    input_data = text_box_page.fill_of_fields()
    output_data = text_box_page.check_filled_form()
    #assert input_data == output_data, "error"
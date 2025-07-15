import random

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_of_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        cur_addr = person_info.current_address
        perm_addr = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(cur_addr)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(perm_addr)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, cur_addr, perm_addr

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address

class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 15
        while count !=0:
            item = item_list[random.randint(1, 15)]
            self.go_to_element(item)
            item.click()
            count -= 1
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for item in checked_list:
            title_item = item.find_element("xpath", self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('.doc', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        output_data = []
        for item in result_list:
            output_data.append(item.text)
        return str(output_data).replace(' ', '').lower()

class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        choices = {
            'yes': self.locators.RADIO_BUTTON_YES,
            'impressive': self.locators.RADIO_BUTTON_IMPRESSIVE,
            'no': self.locators.RADIO_BUTTON_NO,
        }
        self.element_is_clickable(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.RESULT).text


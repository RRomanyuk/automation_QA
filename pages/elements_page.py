import base64
import os
import random

import requests
from selenium.webdriver.common.by import By
from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadLocators
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
            title_item = self.get_element(item)
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

class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        self.element_is_visible(self.locators.ADD_BUTTON).click()
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
        self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

        return [first_name, last_name, str(age), email, str(salary), department]

    def check_new_person(self):
        person_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in person_list:
            if not item.text.strip():
                continue
            self.go_to_element(item)
            data.append(item.text.splitlines())
        return data

    def search_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(str(key_word))

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = self.get_element(delete_button)
        return row.text.splitlines()

    def edit_person_info(self):
        table = self.element_is_visible(self.locators.TABLE)
        self.go_to_element(table)
        self.element_is_visible(self.locators.EDIT_BUTTON).click()
        data = self.check_new_person()
        choice_field_for_edit = random.randint(0, 5)
        field_names = ["first_name", "last_name", "email", "age", "salary", "department"]
        locator = getattr(self.locators, field_names[choice_field_for_edit].upper() + "_INPUT")
        self.element_is_visible(locator).send_keys(data[choice_field_for_edit])
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return data, data[choice_field_for_edit]

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted_person(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    def select_up_to_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for rows in count:
            count_row_button = self.get_element_and_scroll_into_view(self.locators.COUNT_ROW_LIST)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f"option[value='{rows}']")).click()
            data.append(self.check_count_rows())
        return data, count

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)

class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_button(self):
        click_button = self.get_element_and_scroll_into_view(self.locators.CLICK_BUTTON)
        click_button.click()
        return self.check_clicked_on_button(self.locators.SUCCESS_CLICK_ME_BUTTON)

    def right_click_on_button(self):
        right_click_buttons = self.get_element_and_scroll_into_view(self.locators.RIGHT_CLICK_BUTTON)
        self.action_right_click(right_click_buttons)
        return self.check_clicked_on_button(self.locators.SUCCESS_RIGHT_CLICK_BUTTON)

    def double_click_on_button(self):
        double_click_buttons = self.get_element_and_scroll_into_view(
            self.locators.DOUBLE_CLICK_BUTTON)
        self.action_double_click(double_click_buttons)
        return self.check_clicked_on_button(self.locators.SUCCESS_DOUBLE_CLICK_BUTTON)

    def check_clicked_on_button(self, element):
        return self.element_is_present(element).text

class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.get_element_and_scroll_into_view(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute("href")
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            return link_href, self.driver.current_url
        else:
            return link_href, request.status_code
        
    def check_broken_list(self, url):
        request = requests.get(url)
        bad_request = self.get_element_and_scroll_into_view(self.locators.BAD_REQUEST)
        if request.status_code == 200:
            bad_request.click()
        else:
            return request.status_code

class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadLocators()

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        upload_path = self.element_is_present(self.locators.UPLOAD_FILE_PATH).text
        return os.path.basename(file_name), os.path.basename(upload_path)

    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute("href")
        link_b = base64.b64decode(link)
        path_name_file = rf'C:\dotret\filetest{random.randint(1, 1000)}.jpeg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
            os.remove(path_name_file)
        return check_file
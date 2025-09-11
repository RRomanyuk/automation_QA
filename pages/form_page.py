import os

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file, choice_subject
from locators.form_page_locators import PracticeFormPageLocators
from pages.base_page import BasePage


class PracticeFormPage(BasePage):
    locators = PracticeFormPageLocators

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)

        self.element_is_visible(self.locators.SUBJECT).send_keys(choice_subject())
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_visible(self.locators.FILE_INPUT).send_keys(path)

        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_present(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT).click()
        os.remove(path)
        return person

    def result_table(self):
        result_list = self.elements_are_present(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            data.append(item.text)
        return data
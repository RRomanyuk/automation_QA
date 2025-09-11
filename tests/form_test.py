from pages.form_page import PracticeFormPage
from conftest import driver


def test_practice_form(driver):
    practice_form_page = PracticeFormPage(driver, "https://demoqa.com/automation-practice-form")
    practice_form_page.open()
    person = practice_form_page.fill_form_fields()
    result = practice_form_page.result_table()
    #assert person.email is result[1]


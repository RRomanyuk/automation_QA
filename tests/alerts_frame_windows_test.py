from conftest import driver
from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage


def test_new_tab(driver):
    new_window = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
    new_window.open()
    title = new_window.check_opened_new_tab()
    assert title == "This is a sample page"

def test_new_window(driver):
    new_window = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
    new_window.open()
    title = new_window.check_opened_new_window()
    assert title == "This is a sample page"

def test_see_alert(driver):
    alerts = AlertsPage(driver, "https://demoqa.com/alerts")
    alerts.open()
    text = alerts.check_see_alert()
    assert text == "You clicked a button"

def test_timer_alert(driver):
    alerts = AlertsPage(driver, "https://demoqa.com/alerts")
    alerts.open()
    text = alerts.check_time_alert()
    assert text == "This alert appeared after 5 seconds"

def test_confirm_alert(driver):
    alerts = AlertsPage(driver, "https://demoqa.com/alerts")
    alerts.open()
    text = alerts.check_confirm_alert()
    assert text == "You selected Ok"

def test_prompt_alert(driver):
    alerts = AlertsPage(driver, "https://demoqa.com/alerts")
    alerts.open()
    text, text_result = alerts.check_prompt_alert()
    assert text in text_result
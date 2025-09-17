from selenium.webdriver.common.by import By

class AlertsFrameWindowsLocators:
    #Tab and window
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id=tabButton]')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id=windowButton]')
    TITLE_NEW_TAB = (By.CSS_SELECTOR, 'h1[id=sampleHeading]')

    #Alerts
    ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id=alertButton]')
    TIMER_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id=timerAlertButton]')
    CONFIRM_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id=confirmButton]')
    CONFIRM_RESULT = By.CSS_SELECTOR, 'span[id=confirmResult]'
    PROMPT_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id=promtButton]')
    PROMPT_RESULT = By.CSS_SELECTOR, 'span[id=promptResult]'
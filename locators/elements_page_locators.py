from selenium.webdriver.common.by import By

class TextBoxPageLocators:

    #form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    #created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')

class CheckBoxPageLocators:

    EXPAND_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")

class RadioButtonPageLocators:

    RADIO_BUTTON_YES = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    RADIO_BUTTON_IMPRESSIVE = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    RADIO_BUTTON_NO = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    RESULT = (By.CSS_SELECTOR, 'p span[class="text-success"]')

class WebTablePageLocators:
    #Add person form
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")

    #Table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    EDIT_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
    TABLE = (By.CSS_SELECTOR, "div[class='rt-table']")
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    COUNT_ROW_LIST = (By.CSS_SELECTOR, "select[aria-label='rows per page']")

class ButtonsPageLocators:

    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_BUTTON = (By.XPATH, "//div[3]/button")

    #result
    SUCCESS_DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    SUCCESS_RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    SUCCESS_CLICK_ME_BUTTON = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")

class LinksPageLocators:

    SIMPLE_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    BAD_REQUEST = (By.CSS_SELECTOR, "a[id='bad-request']")

class UploadAndDownloadPageLocators:

    UPLOAD_FILE = (By.CSS_SELECTOR, "input[id='uploadFile']")
    UPLOAD_FILE_PATH = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")

    DOWNLOAD_FILE = (By.CSS_SELECTOR, "a[id='downloadButton']")

class DynamicPropertiesPageLocators:

    ENABLE_BUTTON = (By.CSS_SELECTOR, "button[id='enableAfter']")
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "button[id='colorChange']")
    VISIBLE_BUTTON_5_SEC = (By.CSS_SELECTOR, "button[id='visibleAfter']")
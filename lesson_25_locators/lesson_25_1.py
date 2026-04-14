from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

# XPATH LOCATORS (25)


xpaths = [
    "//button[text()='Sign In']",
    "//button[contains(text(),'Sign')]",
    "//a[text()='Home']",
    "//h1[text()='Do more!']",
    "//input[@id='signinEmail']",
    "//input[@name='email']",
    "//input[@type='password']",
    "//button[@type='button' and text()='Register']",
    "//div[@class='modal-content']//input[@id='signinPassword']",
    "//form//input[@type='email']",
    "//form//input[@type='password']",
    "//button[contains(@class,'btn-primary')]",
    "//a[@routerlink='/contacts']",
    "//div[contains(@class,'header')]//button",
    "//nav//a[text()='About']",
    "//footer//a[contains(text(),'Support')]",
    "//div[@class='hero-descriptor']//p",
    "//button[text()='Guest log in']",
    "//input[contains(@class,'form-control')]",
    "//div[@class='modal-footer']//button[text()='Login']",
    "//button[@data-bs-dismiss='modal']",
    "//div[contains(@class,'modal')]//input[@id='signinEmail']",
    "//input[@id='signinEmail' and @type='email']",
    "//button[contains(text(),'Log')]",
    "//div//button[text()='Sign In']"
]

# CSS LOCATORS (25)

css_selectors = [
    "button.btn.btn-primary",
    "button[class*='primary']",
    "a.nav-link",
    "input#signinEmail",
    "input[name='email']",
    "input[type='password']",
    "form input.form-control",
    "div.modal-content input#signinPassword",
    "button[data-bs-dismiss='modal']",
    "button.btn-outline-white",
    "div.header button",
    "nav a[href='/about']",
    "footer a",
    "div.hero-descriptor p",
    "button.hero-descriptor_btn",
    "input.form-control[type='email']",
    "input.form-control[type='password']",
    "div.modal-footer button.btn-primary",
    "div.modal-content input",
    "div.container button",
    "button.btn.btn-outline-primary",
    "a.btn",
    "div.row input",
    "div.modal-dialog button",
    "header nav a"
]

print("XPath count:", len(xpaths))
print("CSS count:", len(css_selectors))

driver.quit()
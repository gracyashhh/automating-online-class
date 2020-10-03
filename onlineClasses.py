from selenium import webdriver
from time import sleep
from datetime import datetime
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option(
    "prefs",
    {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1,
    },
)


class LoginSession:
    def __init__(self, username, pwd, email, pas):
        self.driver = webdriver.Chrome(
            chrome_options=opt, executable_path="D:\chromedriver\chromedriver.exe"
        )
        self.username = username
        self.pwd = pwd
        self.email = email
        self.pas = pas
        self.driver.get(
            "https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier"
        )
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
        ).send_keys(email)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]"
        ).click()
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="password"]/div[1]/div/div[1]/input'
        ).send_keys(pas)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]"
        ).click()
        sleep(2)
        self.driver.get("https://online.karunya.edu/oauth/login")
        sleep(1)
        now = datetime.now()
        print(now)
        # current_time = now.strftime("%I:00 %p")
        current_time = now.strftime("12:00 PM")
        print("Current Time =", current_time)
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[1]/div[1]/div/select"
        ).click()
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[1]/div[1]/div/select/option[1]"
        ).click()
        sleep(5)
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[1]/form/div[1]/div/input"
        ).send_keys(username)
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[1]/form/div[2]/div/input"
        ).send_keys(pwd)
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[1]/form/div[3]/button"
        ).click()
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/main/div/div/div[2]/div/div/div/div[2]/label/input"
        ).send_keys(current_time)
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/main/div/div/div[2]/div/div/div/table/tbody/tr/td[4]/a"
        ).click()
        sleep(3)
        # self.driver.close()
        # #### NEED HELP CLOSING THE FIRST TAB AND SWITCHING TARGET TO THE SECOND TAB ### #
        sleep(7)
        self.driver.find_element_by_xpath("(//*[@role='button'])[1]").click()
        print("mike off")
        sleep(3)
        self.driver.find_element_by_xpath("(//*[@role='button'])[2]").click()
        print("cam off")
        sleep(2)
        self.driver.find_element_by_xpath("//*[text()='Ask to join']").click()
        print("joined the meet")


student = LoginSession(
    "##REG NO HERE##", "###Seraph PSWD###", "###CLG MAIL HERE##", "###EMAIL PSWD###"
)

import time

from selenium.webdriver.common.keys import Keys


class GuerrillaMail:
        @staticmethod
        def goto_site(driver):
                link = 'https://www.guerrillamail.com/'
                driver.goto(link)

        @staticmethod
        def put_user(driver,user):
                user_xpath = '//*[@id="inbox-id"]'
                user_textbox = '//*[@id="inbox-id"]/input'

                driver.click(user_xpath)
                driver.click(user_textbox)
                driver.send_keys(user_textbox, user)
                driver.send_keys(user_textbox, Keys.RETURN)
                time.sleep(1)

        @staticmethod
        def find_email(driver, title, max_attempts = 3):
                print('Searching for mail')
                mail_title = '/html/body/div[4]/div/div[3]/div[2]/form/table/tbody/tr[%d]/td[3]'  # /text()
                while True:
                        for i in range(1, max_attempts+1):
                                try:
                                        mail = mail_title % i
                                        if title in driver.get_value(mail, 'innerHTML'):
                                                driver.click(mail)
                                                return
                                except:
                                        print('Mail not found, waiting 10 s')
                                        time.sleep(10)
                                        break
                        print('Mail not found, waiting 10 s')
                        time.sleep(10)
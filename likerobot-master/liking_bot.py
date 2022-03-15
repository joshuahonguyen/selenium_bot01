from selenium import webdriver
from selenium.common.exceptions import *
from math import ceil

class IG_BOT:
    def __init__(self, driver, S_ID):
        self.driver = driver
        self.driver.get("http://www.instagram.com")
        self.driver.add_cookie({"name": "sessionid", "value": S_ID})
    
    def LIKE(self, links):
        for link in links:
            self.driver.get(link)
            c_len = self.driver.execute_script("return document.body.getElementsByClassName('wpO6b  ').length")
            for c in range(0, c_len):
                c_look = self.driver.execute_script("return document.body.getElementsByClassName('wpO6b  ')[{}].querySelector('._8-yf5 ').ariaLabel".format(c))
                c_height = self.driver.execute_script("return document.body.getElementsByClassName('wpO6b  ')[{}].querySelector('._8-yf5 ').height.baseVal.value".format(c))
                if "like" in str(c_look).lower() and not "unlike" in str(c_look).lower():
                    print(c_look)
                    if c_height == 24:
                        print(c_look)
                        print(c_look, c_height)
                        self.driver.find_elements_by_class_name('wpO6b  ')[c].click()
                        #throw error when it shows it failed
                    
    def load_acc(self, account):
        self.driver.get("http://www.instagram.com/{}".format(account))
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        links = []
        while True:
            sus = self.driver.execute_script("return document.body.getElementsByClassName('_-rjm')[0].getElementsByClassName('tA2fc ')[0].innerHTML")
            if sus != "":
                raise Exception('failed to load')
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            loader = self.driver.execute_script("return document.body.getElementsByClassName('  By4nA')[0]")

            try:
                boxes = self.driver.execute_script("return document.body.getElementsByClassName('Nnq7C weEfm').length")
                print(boxes)
                for box in range(0, boxes):
                    sub_len = self.driver.execute_script("return document.body.getElementsByClassName('Nnq7C weEfm')[{}].getElementsByClassName('v1Nh3 kIKUG  _bz0w').length".format(box))
                    for sub_num in range(0, sub_len):
                        sub = self.driver.execute_script("return document.body.getElementsByClassName('Nnq7C weEfm')[{}].getElementsByClassName('v1Nh3 kIKUG  _bz0w')[{}].getElementsByTagName('a')[0].href".format(box, sub_num))
                        if sub not in links:
                            links.append(sub)
            except Exception as e:
                print(e)
                continue
                
            if loader == None:
                break
        
        return links

try:
    driver = webdriver.Chrome(r".\chromedriver.exe")
    bot01 = IG_BOT(driver, "putasessionid")
    acc = "putaaccounhere"
    while True:
        try:
            bot01.LIKE(bot01.load_acc(acc))
        except Exception as e:
            print(e)
            break
        break

finally:
    driver.quit()

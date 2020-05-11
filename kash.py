from selenium import webdriver
import time
import random

BASE_URL = "https://www.instagram.com/explore/tags/"
tags = ['ui']
comments = [
    'Wow ! Nice Post.',
    'Keep it up !!',
    'Awesome Work',
    'Nice Work'
]
com_len=len(comments)-1
username="username@kash4xd"
password="password@kash4xd"

# options = webdriver.FirefoxOptions()
# options.add_argument('-headless') 
browser = webdriver.Firefox(executable_path=r"./geckodriver.exe")
browser.get('https://instagram.com/')
time.sleep(6)

# Entering username
flag = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
flag.send_keys(username)
time.sleep(2)

# Entering password
flag = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
flag.send_keys(password)
time.sleep(2)

# Clicking to log in
flag = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]")
flag.click()
time.sleep(8)

# Handling notification popup
flag = browser.find_element_by_css_selector('button.aOOlW:nth-child(2)')
flag.click()

for tag in tags:
    browser.get(f"{BASE_URL}{tag}/")
    time.sleep(5)
    temp = browser.find_elements_by_class_name("_bz0w")
    
    # For TOP Post
    # posts=temp[:10]

    # For RECENT Post
    posts=temp[9:]



    for i in range(5):
        # Opening Post
        posts[i].click()
        time.sleep(5)

        # Liking Post
        flag = browser.find_element_by_css_selector('.fr66n > button:nth-child(1)')
        flag.click()
        time.sleep(5)

        # Typing Comment
        flag = browser.find_element_by_css_selector('._15y0l > button:nth-child(1)')
        flag.click()
        time.sleep(2)
        flag = browser.find_element_by_css_selector('.Ypffh')
        flag.send_keys(comments[random.randint(0,com_len)])
        time.sleep(2)

        # Posting Comment
        flag = browser.find_element_by_css_selector('.X7cDz > button:nth-child(2)')
        flag.click()
        time.sleep(3)

        # Closing Post
        flag = browser.find_element_by_css_selector('.BI4qX > button:nth-child(1)')
        flag.click()

        time.sleep(4)


browser.quit()
